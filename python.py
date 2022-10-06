import pandas as pd

print("-------\nA. Load data and display it.\n")
df = pd.read_csv(r"C:\\Users\\admin\\Desktop\\dishwa\\dmw\\Practical 3\\employees.csv", delimiter = ';', on_bad_lines='skip')
print(df.head(5))

print("-------\nB. Describe the dataset.\n")
print(df.describe())

print("-------\nC. List information about columns of dataset.\n")
print(df.info())

print("-------\n1. How many entries are there in the employee dataset?\n")
print(len(df))

print("-------\n2. How many departments are there in Zee organization?\n")
print(len(df.groupby('DEPARTMENT_ID')))

print("-------\n3. Find out the maximum salary that is given in each department.\n")
print((df.groupby('DEPARTMENT_ID').SALARY.agg([max])))

print("-------\n4. Find out the detail of the employee who have got the minimum salary in the entire organization.\n")
print(df.loc[df['SALARY'] == df['SALARY'].min()])

print("-------\n5. Find out the total salary amount that is given in each department. (Salary of employee working in the same department should be added and displayed)\n")
print(df.groupby('DEPARTMENT_ID')['SALARY'].sum())

print("-------\n6. Find out how many managers work in the organization.\n")
print(len(df.groupby('MANAGER_ID')))

print("-------\n7. Find out that how many employee works in each department.\n")
print(df.groupby('DEPARTMENT_ID')['EMPLOYEE_ID'].count())

print("-------\n8. Find out what is the maximum salary that is given to employee in this organization.\n")
print(df['SALARY'].max())

print("-------\n9. Find the details of all the employees whose Job_id is SA_MAN.\n")
print(df.loc[df['JOB_ID']=='SA_MAN'])

print("-------\n10. Find the average salary of each department.\n")
print(df.groupby('DEPARTMENT_ID').SALARY.mean())

print("-------\n11. Find the number of employees working under every manager in the organization.")
print(df.groupby('MANAGER_ID')['EMPLOYEE_ID'].count())
