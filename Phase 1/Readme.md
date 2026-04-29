# Phase 1: Data Preparation & Base Models

This folder contains the foundation of our salary prediction project. 

Since real HR data is strictly confidential, we started with a raw synthetic dataset of 500 employees. We used a dedicated notebook to clean the data, apply standard scaling, and get it ready for machine learning. 

After preparing the data, we used forward feature selection to identify the top 8 most important variables and trained three baseline models to see how they perform:
* Linear Regression
* Ridge Regression
* Lasso Regression

**Files in this folder:**
* `clean_data.ipynb` - Our notebook for cleaning the raw data, handling encoding, and scaling.
* `phase1_models.ipynb` - The main code for feature selection and training the baseline models.
* `employee_salary_dataset2.csv` - The raw, original synthetic dataset.
* `cleaned_employee_dataset.csv` - The improved dataset after preprocessing.
* `Phase_1_Report.docx` - Our detailed report for this phase.