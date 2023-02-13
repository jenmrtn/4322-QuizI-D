'''
Due the outstanding performance of the Customer Service Represetatives (CSRs) in the marketing department, management
has decided to reward them with a 10% increase in their salary. To evaluate the impact on the budget, you have been
asked to run a report on the employee file and display the results of BEFORE AND AFTER the salary increase.

You will create a dictionary that has the full employee name as the key and ONLY their new salary as the value.

Iternate through the dictionary to print out their name and thier new salary (as in image)
'''

import csv

#open the file
infile=open('employee_data.csv', 'r')
employee_file= csv.reader(infile, delimiter=',')
next(employee_file)

#create an empty dictionary
employeedict={}

#use a loop to iterate through the csv file
for i in employee_file:
    if i[4]=='CSR' and i[3]== 'Marketing':
        x=format(float(i[5]), ".2f")
        x=format(float(x), ',')
        print(f'Manager Name: {i[1]} {i[2]} Current Salary: ${x}0')
        employeedict[i[1]+' '+i[2]]=(i[5])
    #check if the employee fits the search criteria


    

print()
print('=========================================')
print()

for i, v in employeedict.items():
    v=(format(float(v)*1.1, '.2f'))
    v=format(float(v), ',')
    print(f'Manager Name: {i} New Salary: ${v}0')
#iternate through the dictionary and print out the key and value as per printout



          
        

        
    






