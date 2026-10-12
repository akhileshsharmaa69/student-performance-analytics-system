import numpy as np
import pandas as pd
#find each student each saubject marks total
def calculate_total(df,subject):
    marks=df[subject].to_numpy()
    total=np.sum(marks,axis=1)
    return total

data={
    "student_id":list(range(101,131)), #generate unic id all student using range fun and list

#name of student

"Name":[
    "akhil","rahul","nimesh","sirsa","aransh",
    "naman","aditi","ankit","soniya","aniket",
    "aman","neha","rohit","vansh","arjun",
    "shubham","aditya","riya","sahil","karan",
    "varun","isha","nikhil","meena","deepak",
    "akash","nisha","manish","payal","vedh",],

#all subject marks out of 100
"python":[85,80,72,60,88,76,91,68,82,74,
          89,93,65,69,80,75,65,68,88,77,
          78,80,75,58,89,76,95,62,81,70,],

"SQL":[   90,81,74,65,89,76,95,55,68,73,
          91,93,65,69,98,58,66,63,88,77,
          78,80,75,58,89,91,89,62,55,99,],

"C++":[   78,81,74,65,76,66,95,55,65,89,
          81,93,92,73,98,59,56,63,81,77,
          69,80,75,58,89,98,89,62,71,80,],

"DATA STRUCTURE":[90,85,74,65,71,56,98,59,86,75,
            71,95,91,75,91,69,76,43,81,77,
          69,50,95,58,79,98,71,78,73,81,],

"HTML":[   90,82,77,69,56,86,91,75,71,79,
          85,90,57,83,98,39,83,66,89,67,
          99,70,76,88,99,88,67,59,74,89,],

"CSS":[   88,70,96,65,90,75,95,92,68,77,
          91,71,92,70,98,55,61,65,88,99,
          66,80,49,61,83,91,59,66,70,89,],  

#attendance parcenetage
"Attendance":[
    92,85,98,75,94,88,96,78,90,83,
    91,95,73,66,84,88,99,88,70,93,
    96,89,95,77,87,89,96,74,92,99

] }

#convert dictionary data to table form
df=pd.DataFrame(data)

# to save a table data to csv file
df.to_csv("student.csv",index=False) # index false means do not save extra row number and column

# display the original student data
#print("->>>>>>>>>>> STUDENT DATA <<<<<<<<<<<<-")

#TO count of student in a data set using len function
print("\nTotal Student:",len(df))
print("\nSTUDENT PERFORMANCE ANALYTICS SYSTEM")

#read the csv file and store the dataframe
df=pd.read_csv("student.csv")
#display the csv data
print("->>>>>>>>>>>> STUDENT DATA <<<<<<<<<<<<-")
print(df.to_string(index=False))
#select the  all subject in a columns
subject=["python","SQL","C++","DATA STRUCTURE","HTML","CSS"]
#calculate total marks using our function
df['Total']=calculate_total(df,subject)
#select subject marks a numpy array
marks=df[subject].to_numpy()
#calculte average marks each student
df['Average']=np.round(np.mean(marks,axis=1),2)
#fun to calculate grade
def calculate_grade(average):
    if average>=90:
        return "A+"
    elif average>=80:
        return "A"
    elif average>=70:
        return "B"
    elif average>=60:
        return "C" 
    else:
        return "D"  
  
#calculate grade for each student
grades=[]
for average in df['Average']:
    grade=calculate_grade(average)
    grades.append(grade)
#add grade colomn
df['Grade']=grades 

#check wether each student has pass all or fail subject
results=[]
for i in range(len(df)):
    if all(df.loc[i,subject]>=40):
        results.append('Pass')
    else:
        results.append("Fail") 
# add the colomn to data frame
df["Result"]=results
#count pass or fail student
pass_count=0
fail_count=0
for result in df["Result"]:
    if result=="Pass":
        pass_count=pass_count+1
    else:
            fail_count=fail_count+1
print("\n************>PASS AND FAIL REPORT<**************")   
print("Total Pass Student:",pass_count)
print("Total Fail Student:",fail_count)         

#final performance table
print("\n->>>>>>>>>>>>> STUDENT PERFORMANCE <<<<<<<<<<<<<-")
print(df[["student_id","Name","Total","Average","Grade"]].to_string(index=False)) # display each student total average and grade

#find the highest and lowest total markss
highest=df['Total'].max()
lowest=df['Total'].min()
highest_student=df[df['Total']==highest]
lowest_student=df[df['Total']==lowest]
print("\n><><><><><><><><>-HIGHEST SCORE-<><><><><><><><><>")   
print(highest_student[['Name','Total']].to_string(index=False))
print("\n><><><><><><><><>-LOWEST SCORE-<><><><><><><><><>") 
print(lowest_student[['Name','Total']].to_string(index=False))

#class average calculate
total_average=0 #begin me total 0 haii
for average in df['Average']: #pick each student average
    total_average=total_average+average # add in total
class_average=total_average/len(df) #count the total student

print("\n<><><><><><><><><><>-CLASS AVERAGE-<><><><><><><><><><><><>")
print("Class Average:",round(class_average,2)) #avearge find all class

#subject wise average marks
print("\n=========== SUBJECT WISE AVEARAGE ==========")
for sub in subject: #select each subject
    average=df[sub].mean() #student ke marks average find 
    print(sub,"Average:",round(average,2)) #only show average value of decimal 2 places
      
#find top five student
top_student=df.sort_values(by="Total",ascending=False).head(5) # arrange the according of total marks and select the beginning 5 rows
print("\n**************>TOP 5 STUDENTS<**************")
print(top_student[['student_id','Name','Total','Average','Grade']].to_string(index=False)) # top 5 student list show

#attendance report
present_count=0
low_aattendance=0
for attendance in df['Attendance']:
    if attendance>=75:
        present_count=present_count+1
    else:
        low_aattendance=low_aattendance+1
print("\n<><><><><><><><> ATTENDANCE REPORT <><<><><><><><><><>")  
print("Attendance 75% or above:",present_count,"Student")
print("Attendance below 75% :",low_aattendance,"Student")

