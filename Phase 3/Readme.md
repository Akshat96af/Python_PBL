# Phase 3: Final Training & Deployment

This is the final phase of our project. After comparing all the models from the previous phases, we selected Ridge Regression as our most stable and reliable model for this specific dataset.

In this phase, we performed a final training run and saved the model using Python's pickle library. We then created a standalone deployment notebook that loads the saved model and allows a user to input an employee's details to instantly get a predicted salary.

**Files in this folder:**
* `Phase3_Final_Training.ipynb` - The backend script that trains and saves the final model.
* `Phase3_Deployment.ipynb` - The frontend interactive script for live salary predictions.
* `cleaned_employee_dataset.csv` - The dataset used for the final training.
* `Phase_3_Report.docx` - Our final project report.