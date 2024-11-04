# CS506_Project
# Boston Bus Route 57 Designated Station Arrival Prediction
## TeamMember
<p>Jiangjian Xie (xjj2023@bu.edu)</p>
<p>Zhekai Zhu (zzk@bu.edu)</p>
<p>Wenyuan Cui (wycui@bu.edu)</p>
<p>Mohan Guo (gmh926@bu.edu)</p>

## Description
The Boston 57 bus passes through multiple stops at Boston University and is one of the transportation options for Boston University students to get to school. This project will record the arrival time of bus route 57 at a designated station within a certain period of time. Due to weather factors, changes in the number of commuters on weekdays, and different commuting time points, there may be deviations in the arrival time of the bus. 

## Goal
Predict the most likely time point for the bus to arrive each day based on records.

## Data and Methods
The preliminary plan requires collecting data such as weather, week day, and bus arrival time. Due to the possibility of early and late bus departure times, it is necessary to record the accurate departure time of buses. The number of passengers on the bus is also a key data information, which affects the boarding and alighting time at each station. Therefore, in an ideal situation, we should record a rough estimate of the number of passengers arriving at the designated station. The collection method will arrange for each team member to take turns responsible for one day, which can be recorded on-site at the bus stop or through bus query software or Google Maps to record the arrival time of the bus. When there is a special situation where the recorded value of a certain time is missing, linear interpolation can be used to estimate the missing time. In predicting the arrival time of public transportation, we can estimate the time of unrecorded trips by using the arrival times of previous and subsequent trips. We can handle it by setting a time window, such as centered around 9:00, allowing a deviation of 10 minutes before and after. 

<p><a href="https://docs.google.com/forms/d/e/1FAIpQLSd8utxViE5V_fWjTpm7axMdXCRiE4OoGGntMK6CDoeIUio47Q/viewform?usp=sf_link" target="_blank"><strong>Form »</strong></a></p>

## Data Modeling
<p><b>Linear regression model:</b> Can be used as an initial model to predict bus arrival time.</p>
<p><b>Decision trees or random forests:</b> These models can handle complex nonlinear relationships and are suitable for situations involving multiple influencing factors, such as weather, traffic, and the difference between weekdays and weekends.</p>


## Data Visualization
<p><b>Time Arrival Time Distribution Chart:</b> A line chart can be used to display the distribution of arrivals at each time point of the day, showing peak and off peak periods.</p>
<p><b>The impact of weather on arrival time:</b> Box plots can be used to display the distribution of bus arrival time under different weather conditions (sunny, rainy, snowy).</p>
<p><b>Comparison between weekdays and weekends:</b> A bar chart can be used to compare the differences in arrival times between weekdays and weekends during the same time period.</p>

## Test
The project plans to record data from October 7th to December 1st, and use October's data as the training set and November's data as the testing set.
