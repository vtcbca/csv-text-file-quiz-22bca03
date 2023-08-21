# writing salary csv file
count=0
import csv
with open("salary.csv",'r',newline='') as f:
    data= csv.writer(f)
    header=['sid','sname','salary']
    record=[[1,'jay',10000],[2,'vishal',9000],[3,'amit',15000],[4,'sumit',11000],[5,'sai',8000]]
    data.writerow(header)
    data.writerows(record)
# reading salary csv file     
    data=csv.reader(f)
    for i in data :
        print(i)
        
