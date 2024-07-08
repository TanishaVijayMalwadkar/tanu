import csv
roll=input("enter roll=")
name=input("enter name=")
mark=input("enter mark=")
stud_details=[roll,name,mark]
with open("student.csv","a",newline='') as file:
    writer=csv.writer(file)
    writer.writerow(stud_details)
with open("student.csv","r") as file:
    reader=csv.reader(file)
    for row in reader:
        print(row)    