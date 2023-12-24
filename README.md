# House-prices-usa

Process followed:
•	Individual feature’s data from past 20 years was scraped from multiple sites and compiled into one master file.
•	Some of the data was only collected quarterly, so I have created a python script convert the data from quarterly to monthly to create a standard interval of data points.
•	Further preprocessing was done to remove null values and perform feature selection using correlation matrix.
•	Dataset was finally split into training and testing data after which the dataset was normalized except for the target variable as we would like to retain the original scale of home prices.
•	I have picked random forest for this regression type problem which was tuned using GridSearchCV and trained on the training dataset using the best parameters found from GridSearchCV.
•	Finally some scikit learn metrics libraries were used to get the metrics and performance of the model which were displayed using and matplotlib.
