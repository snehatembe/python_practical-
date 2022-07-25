import mysql.connector

db=mysql.connector.connect(host="localhost",user="sneha",passwd="3000",database="snehast08")
cursor=db.cursor()
cursor.execute("DROP TABLE IF EXISTS stud")

query="""CREATE TABLE stud(
PRN VARCHAR(20),First_Name VARCHAR(20),Middle_Name VARCHAR(20),
Last_Name VARCHAR(20),Address VARCHAR(30),
Mobile_Number VARCHAR(20), Email_ID VARCHAR(30),DOB VARCHAR(10))"""
cursor.execute(query)

#TAKING INPUT FROM USER FOR ONLY ONE USER
query="""INSERT INTO stud(PRN, First_Name, Middle_Name, Last_Name, Address, Mobile_Number, Email_ID, DOB)
                VALUES(%s, %s, %s, %s, %s, %s, %s, %s)"""
records=[
    input("ENTER PRN: "),
    input("FIRST NAME: "),
    input("MIDDLE NAME: "),
    input("LAST NAME: "),
    input("ADDRESS: "),
    input("MOBILE NUMBER: "),
    input("EMAIL ID: "),
    input("DOB: ")]

cursor.execute(query,records)
db.commit()
# OR YOU CAN TAKE MULTIPLE INPUTS BY USING LOOP
# OR YOU CAN INSERT BY TYPING THIS COMMANDS INDIVISUALLY.

query="""INSERT INTO stud(PRN, First_Name, Middle_Name, Last_Name, Address, Mobile_Number, Email_ID, DOB)
                VALUES('21303312455053', 'Sneha','Sanjay', 'Tembe','Lonere','0000','snehatembe@gmail.com','08-08-2003')"""
cursor.execute(query)
db.commit()
query="""INSERT INTO stud(PRN, First_Name, Middle_Name, Last_Name, Address, Mobile_Number, Email_ID, DOB)
                VALUES('21303312455055', 'Trupti','Rakesh', 'Mahabale','Kolad','0000','trupti@gmail.com','19-08-2002')"""
cursor.execute(query)
db.commit()
query="""INSERT INTO stud(PRN, First_Name, Middle_Name, Last_Name, Address, Mobile_Number, Email_ID, DOB)
                VALUES('21303312455023', 'Pooja','Pradeep', 'Deokar','Mangaon','0000','pooja@gmail.com','26-10-2002')"""
cursor.execute(query)
db.commit()
query="""INSERT INTO stud(PRN, First_Name, Middle_Name, Last_Name, Address, Mobile_Number, Email_ID, DOB)
                VALUES('21303312455063', 'Shravani','Vilas', 'Chavan','Mangaon','0000','shravani@gmail.com','20-08-2002')"""
cursor.execute(query)
db.commit()
query="""INSERT INTO stud(PRN, First_Name, Middle_Name, Last_Name, Address, Mobile_Number, Email_ID, DOB)
                VALUES('21303312455002', 'Ayesha','AAA', 'Hote','Vahur','0000','ayesha@gmail.com','12-10-2002')"""
cursor.execute(query)
db.commit()
query="""INSERT INTO stud(PRN, First_Name, Middle_Name, Last_Name, Address, Mobile_Number, Email_ID, DOB)
                VALUES('21303312455006', 'Gauri','Gajanan', 'Bhojane','Goregaon','0000','gauri@gmail.com','06-02-2002')"""
cursor.execute(query)
db.commit()
#UPDATE
P = input("ENTER PRN OF STUDENT: ") #We need to get prn from user to update value.
A= input("ENTER NEW PHONE NUMBER: ")
query = "update stud set Mobile_Number ={0} where PRN={1}".format(A,P)
cursor.execute(query)
db.commit()
#DELETE
P=int(input("ENTER PRN OF STUDENT TO BE DELETED: "))
query="delete from stud where PRN={0}".format(P)
cursor.execute(query)
db.commit()
#ADD_COL CGPA AND AGE
count = 6 #Number of students.
query = "ALTER TABLE stud \
                    ADD CGPA VARCHAR(20) DEFAULT '8.67'  AFTER DOB" #DEFAULT VALUE
cursor.execute(query)
query = "ALTER TABLE stud \
                    ADD AGE VARCHAR(20) DEFAULT '15'  AFTER CGPA" 
cursor.execute(query)
while count !=0:
    
    
    P = input("ENTTER PRN OF STUDENT TO ASSIGN CGPA and AGE: ")
    CGPA = input("ENTER CGPA FOR {0}: ".format(P))
    query = "update stud set CGPA ={0} where PRN={1}".format(CGPA,P)
    cursor.execute(query)

    AGE = input("ENTER AGE FOR {0}: ".format(P))
    query = "update stud set AGE ={0} where PRN={1}".format(AGE,P)
    cursor.execute(query)
    print("ADDED")
    db.commit()
    count-=1
#Completed Quetion...
