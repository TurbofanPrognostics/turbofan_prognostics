# Turbofan Prognostics Final Model Report

_Report describing the final model to be delivered - typically comprised of one or more of the models built during the life of the project_

## Analytic Approach
* What is target definition
![Test sets RUL distribution](figures/rul_distribution.png "Test sets RUL distribution")

* What are inputs (description)
* What kind of model was built?

## Solution Description
* Simple solution architecture (Data sources, solution components, data flow)
* What is output?

## Data
* Source
* Data Schema
* Sampling

| **Model**               |**Dataset** |**RMSE (cycles)** |**R2**  |
|-------------------------|------------|------------------|--------|
|Base (Linear Regression) |FD001       |31.62             |0.42    |
|                         |FD002       |34.40             |0.59    |
|                         |FD003       |57.47             |-0.93   |
|                         |FD004       |53.84             |0.02    |
|Timeseries               |FD001       |21.76             |0.73    |
|                         |FD002       |32.00             |0.65    |
|                         |FD003       |22.53             |0.70    |
|                         |FD004       |39.27             |0.48    |
|LSTM                     |FD001       |17.28             |0.83    |
|                         |FD002       |28.22             |0.72    |
|                         |FD003       |18.34             |0.80    |
|                         |FD004       |27.37             |0.75    |
* Selection (dates, segments)
* Stats (counts)

## Features
* List of raw and derived features 
* Importance ranking.

## Algorithm
* Description or images of data flow graph
* What learner(s) were used?
* Learner hyper-parameters

## Results
* ROC/Lift charts, AUC, R^2, MAPE as appropriate
* Performance graphs for parameters sweeps if applicable

| **Model**               |**Dataset** |**RMSE (cycles)** |**R2**  |
|-------------------------|------------|------------------|--------|
|Base (Linear Regression) |FD001       |31.62             |0.42    |
|                         |FD002       |34.40             |0.59    |
|                         |FD003       |57.47             |-0.93   |
|                         |FD004       |53.84             |0.02    |
|Timeseries               |FD001       |21.76             |0.73    |
|                         |FD002       |32.00             |0.65    |
|                         |FD003       |22.53             |0.70    |
|                         |FD004       |39.27             |0.48    |
|LSTM                     |FD001       |17.28             |0.83    |
|                         |FD002       |28.22             |0.72    |
|                         |FD003       |18.34             |0.80    |
|                         |FD004       |27.37             |0.75    |