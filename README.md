# Boston Bus Route 57 Designated Station Arrival Prediction

## Team Members

- Jiangjian Xie ([xjj2023@bu.edu](mailto:xjj2023@bu.edu))
- Zhekai Zhu ([zzk@bu.edu](mailto:zzk@bu.edu))
- Wenyuan Cui ([wycui@bu.edu](mailto:wycui@bu.edu))
- Mohan Guo ([gmh926@bu.edu](mailto:gmh926@bu.edu))

## Project Overview

The Boston 57 bus passes through multiple stops at Boston University and serves as one of the transportation options for Boston University students. This project aims to predict the arrival time of bus route 57 at designated stations based on factors such as weather conditions, weekday patterns, and passenger numbers.

## Data Collection

Data was collected from October 7th to October 31st. The collected data includes:

- Date
- Weekday
- Weather conditions (e.g., sunny, rainy, snowy)
- Bus arrival time

Team members took turns recording bus arrival times either through on-site observation or using bus query applications such as Google Maps.

## Preliminary Data Processing

### Data Cleaning

- We ensured proper data types for each column:
  - "Date" was converted to datetime format for easier manipulation.
  - "Arrival Time" was processed to ensure accurate extraction of hour and minute values.
- For any missing values, we used linear interpolation to ensure the dataset remained complete.

### Feature Engineering

- "Arrival Time" was transformed into "Arrival Time (Minutes)", representing the time of arrival in terms of minutes since midnight. This transformation simplifies analysis and aids in numerical modeling.

## Preliminary Visualizations

### Bus Arrival Count by Weekday

We visualized the distribution of bus arrival counts for each weekday using a bar chart. This helps identify patterns in bus frequency across different days of the week.

![image](https://github.com/user-attachments/assets/b09a1ae4-0024-456c-bcf8-c3626ce659d3)


### Distribution of Arrival Times

We visualized the distribution of bus arrival times throughout the day using a histogram. This provides insights into peak arrival times and helps understand the general trend of bus schedules.

![image](https://github.com/user-attachments/assets/91db2e2c-dc9a-4287-8299-26b0a166f0b1)


## Current Data Modeling Methods

### Linear Regression

We implemented a linear regression model as an initial approach to predict bus arrival times based on features like weekday and weather conditions. We used data from October for training, and the model's performance showed moderate correlation upon initial evaluation. Linear regression established a baseline for model performance.

- **Model Evaluation Metrics**: The initial model had an R² value of 0.45 and a Mean Absolute Error (MAE) of 5.2 minutes, indicating a moderate predictive capability for the relationship between weekday, weather, and arrival time.

### Decision Trees and Random Forests (Upcoming)

We plan to implement decision tree-based models, such as Random Forests, to account for complex, non-linear relationships between features. These models will better capture the influence of factors such as traffic, weather, and weekday type on bus arrival times.

- **Hyperparameter Tuning**: We will use cross-validation to tune hyperparameters, such as tree depth and the number of trees, to improve model generalization.

## Preliminary Results

- We successfully processed the dataset to create a clean version suitable for modeling.
- Initial visualizations indicate distinct weekday patterns in bus arrival frequency and a notable clustering of arrival times during peak hours.
- The linear regression model is currently being trained, and preliminary results show promising trends, suggesting a moderate correlation between weekday and arrival time.

## Next Steps

- **Implement Decision Tree and Random Forest Models**: Complete the implementation of decision trees and random forests to compare against the linear regression baseline.
- **Incorporate Additional Features**: Add more features, such as passenger numbers, to further improve model accuracy. We plan to estimate passenger numbers to evaluate their impact on arrival time.
- **Model Evaluation**: Perform a more comprehensive analysis of model performance using metrics such as Mean Absolute Error (MAE) and Root Mean Squared Error (RMSE) to assess prediction effectiveness.
