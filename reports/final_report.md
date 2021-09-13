# Turbofan Prognostics Final Model Report

_Report describing the final model to be delivered - typically comprised of one or more of the models built during the life of the project_

## Analytic Approach
* What is target definition (&#x2714;)
* What are inputs (description) (&#x2714;)
* What kind of model was built?

The expected value to be gained from this project lies in effective predictive maintenance of turbofan engines. To explain the analytical approach taken, we  first describe the experimental scenario, as outlined in the NASA's turbofan engine degradation simulation dataset (CMAPSS). The project leverages four (4) multivariate time series (see the Data Schema section for details).  For the training data, the ultimate demise of the fleet engine will be due to some combination to two plausible failure modes (HPC Degradation and/or Fan Degradation). For the test set, the time series provided terminates at a point in time prior to fleet engine failure, and, the objective of the investigation is to predict this time of failure. To facilitate this prediction, we are provided a vector of ground truth Remaining Useful life (RUL) values as our test set target value.  


| **Dataset**  | **Fault modes**                 |**Training set size** |**Test set size** |
|--------------|---------------------------------|----------------------|------------------|
|FD001         |HPC Degradation                  |100                   |100               |
|FD002         |HPC Degradation                  |260                   |259               |
|FD003         |HPC Degradation/Fan Degradation  |100                   |100               |
|FD004         |HPC Degradation/Fan Degradation  |248                   |249               |


![Test sets RUL distribution](figures/rul_distribution.png "Test sets RUL distribution")


## Solution Description
* Simple solution architecture (Data sources, solution components, data flow)
* What is output?

## Data
* Source
* Data Schema
* Sampling
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