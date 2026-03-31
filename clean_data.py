import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder, StandardScaler

# load the raw data we generated earlier
data = pd.read_csv("employee_salary_dataset.csv")

# drop any empty or duplicate rows just in case
data.dropna(inplace=True)
data.drop_duplicates(inplace=True)

# converting text columns to numbers coz sklearn models need numeric data
cat_cols = ['Education', 'JobLevel', 'Department', 'JobRole', 
            'EmploymentType', 'LocationType', 'CompanySize']

le = LabelEncoder()
for c in cat_cols:
    data[c] = le.fit_transform(data[c])

# print(data['Department'].unique()) # checking the encoded values

# scaling the numeric features so big values don't mess up the regression models
num_cols = ['Age', 'Experience', 'PerformanceRating', 'ProjectsCompleted', 
            'Certifications', 'WeeklyHours', 'OvertimeHours', 'TeamSize', 
            'LeadershipScore', 'SkillMatchScore', 'YearsInRole', 'Promotions', 
            'JobSatisfaction']

sc = StandardScaler()
# apply scaling and round off to 4 decimals so the csv isn't messy
data[num_cols] = np.round(sc.fit_transform(data[num_cols]), 4)

# save the final clean dataset
out_file = "cleaned_employee_dataset.csv"
data.to_csv(out_file, index=False)
#the dataset is cleaned

