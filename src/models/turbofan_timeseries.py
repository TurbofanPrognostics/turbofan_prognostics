# Imports
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import joblib


# Data import
DATA_DIR = "../../data/raw/CMAPSSData_small/"
sensor_colnames = [f"sensor{i}" for i in range(1,22, 1)]
engine_colnames = ["unit_number", "cycles", "operational_setting_1", "operational_setting_2", "operational_setting_3"] + sensor_colnames


train_fd001_raw = pd.read_csv(f"{DATA_DIR}train_FD001.txt", delim_whitespace=True, names=engine_colnames)
train_fd002_raw = pd.read_csv(f"{DATA_DIR}train_FD002.txt", delim_whitespace=True, names=engine_colnames)
train_fd003_raw = pd.read_csv(f"{DATA_DIR}train_FD003.txt", delim_whitespace=True, names=engine_colnames)
train_fd004_raw = pd.read_csv(f"{DATA_DIR}train_FD004.txt", delim_whitespace=True, names=engine_colnames)

test_fd001_raw = pd.read_csv(f"{DATA_DIR}test_FD001.txt", delim_whitespace=True, names=engine_colnames)
test_fd002_raw = pd.read_csv(f"{DATA_DIR}test_FD002.txt", delim_whitespace=True, names=engine_colnames)
test_fd003_raw = pd.read_csv(f"{DATA_DIR}test_FD003.txt", delim_whitespace=True, names=engine_colnames)
test_fd004_raw = pd.read_csv(f"{DATA_DIR}test_FD004.txt", delim_whitespace=True, names=engine_colnames)

rul_fd001_raw = pd.read_csv(f"{DATA_DIR}RUL_FD001.txt", names=["rul_fd001"], squeeze=True)
rul_fd002_raw = pd.read_csv(f"{DATA_DIR}RUL_FD002.txt", names=["rul_fd002"], squeeze=True)
rul_fd003_raw = pd.read_csv(f"{DATA_DIR}RUL_FD003.txt", names=["rul_fd003"], squeeze=True)
rul_fd004_raw = pd.read_csv(f"{DATA_DIR}RUL_FD004.txt", names=["rul_fd004"], squeeze=True)

rul_df = pd.DataFrame({"rul_fd001": rul_fd001_raw, "rul_fd002": rul_fd002_raw, "rul_fd003": rul_fd003_raw, "rul_fd004": rul_fd004_raw}, dtype=int)

rul_df["unit_number"] = list(range(1, rul_df.shape[0] + 1))

cols = rul_df.columns.tolist()
cols = cols[-1:] + cols[:-1]
rul_df = rul_df[cols]

rul_df = rul_df.set_index("unit_number")

# Model data transformation
train_fd001 = train_fd001_raw.copy()
train_fd002 = train_fd002_raw.copy()
train_fd003 = train_fd003_raw.copy()
train_fd004 = train_fd004_raw.copy()

test_fd001 = test_fd001_raw.copy()
test_fd002 = test_fd002_raw.copy()
test_fd003 = test_fd003_raw.copy()
test_fd004 = test_fd004_raw.copy()

# assuming linear reduction on remaining useful life
train_fd001["rul"] = train_fd001.groupby(["unit_number"], group_keys=False).apply(lambda g: max(g.cycles) - g.cycles)
train_fd002["rul"] = train_fd002.groupby(["unit_number"], group_keys=False).apply(lambda g: max(g.cycles) - g.cycles)
train_fd003["rul"] = train_fd003.groupby(["unit_number"], group_keys=False).apply(lambda g: max(g.cycles) - g.cycles)
train_fd004["rul"] = train_fd004.groupby(["unit_number"], group_keys=False).apply(lambda g: max(g.cycles) - g.cycles)

train_fd001["train_data"] = "fd001"
train_fd002["train_data"] = "fd002"
train_fd003["train_data"] = "fd003"
train_fd004["train_data"] = "fd004"

test_fd001["test_data"] = "fd001"
test_fd002["test_data"] = "fd002"
test_fd003["test_data"] = "fd003"
test_fd004["test_data"] = "fd004"

train = pd.concat([train_fd001, train_fd002, train_fd003, train_fd004], axis=0)
train = train.set_index([ "train_data", "unit_number", "cycles"])

test = pd.concat([test_fd001, test_fd002, test_fd003, test_fd004], axis=0)
test = test.set_index([ "test_data", "unit_number", "cycles"])

# Using clipped RUL
train["rul_clipped"] = train.rul.clip(upper=125)

# Feature selection from EDA
drop_sensors = ['sensor1','sensor5','sensor6','sensor10','sensor16','sensor18','sensor19']
drop_settings =  ["operational_setting_1", "operational_setting_2", "operational_setting_3"]
drop_targets = ["rul"] # ["rul", rul_clipped"]
drop_labels = drop_sensors + drop_settings + drop_targets
drop_test_labels = drop_sensors + drop_settings

Xtrain = train.loc[("fd001")].drop(drop_labels, axis=1)
remaining_sensors = list(Xtrain.columns.difference(["rul", "rul_clipped"]))

# Set up lag 1 features
lag1 = [col + '_lag_1' for col in remaining_sensors]

Xtrain[lag1] = Xtrain[remaining_sensors].shift(1)

Xtrain.dropna(inplace=True)
ytrain = Xtrain.pop('rul_clipped')

# model
lm = LinearRegression()
lm.fit(Xtrain, ytrain)


def evaluate(y_true, y_hat, label='test'):
    mse = mean_squared_error(y_true, y_hat)
    rmse = np.sqrt(mse)
    variance = r2_score(y_true, y_hat)
    print('{} set RMSE:{}, R2:{}'.format(label, rmse, variance))

Xtest = test.loc[("fd001")].drop(drop_test_labels, axis=1)
Xtest[lag1] = Xtest[remaining_sensors].shift(1)
Xtest.dropna(inplace=True)

y_hat_test = lm.predict(Xtest)

# store serialized pipeline
pipeline_name = 'timeseries_regression_pipeline.gz'
file_path = f'../../models/{pipeline_name}'

joblib.dump(lm, file_path)