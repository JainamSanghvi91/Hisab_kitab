# PSC Project - Hisab_Kitab

PSC project submission repository.
Students:

1. Savan Matariya (18BCE213)
2. Jainam Sanghvi (18BCE208)
3. Sagar Chovatiya (18BCE203)

# Introduction

In this modern city as we all use to spent lot of money in our day to day life and thus, for keeping records and perfect **Hisab_Kitab** with other peoples. So, we have developed a project on it that contains many functions as:

1.Face Recognition<br/>
2.Adding Trasaction<br/>
3.Customize Transaction<br/>
4.Delete Transaction<br/>
5.Settle Up<br/>
6.E-mail Verification<br/>
7.User_name Verification<br/>

# Description

## 1.Add_Transaction.py
This file is of form .py i.e, python file and this contains the function code of adding the individual transactions between 2 or more peoples.

This would require the person to add the transactions between whom he wants to and after addinf the details just click on the **Add Transaction** and after this automaticaly mail will forwared to all the person.

## 2.Face_Recognise.py
This file is of form .py i.e, python file and this contains the function code in which we can do 2 major things as: 
1.Add the photo as a part of sign up ans store to the folder
2.Recognize the face from the stored photos from 0-200 range if found then login will be successful or else Failed.

So, this is the code for login and signup purpose so that we can access further things

## 3.Send_mail.py
This file is of form .py i.e, python file and this contains the function code in which we use to send the **E-Mail** to all person who are involved in the Transaction and that contains details of the total payment and details of why it was added and the amount he needs to pay back or take from others.

## 4.email_verify.py
This file is of form .py i.e, python file and this contains the function code in which when the e-mail is added by the person it shoul require **@**,**.com**,**.in** etc things and also same e-mail is considered.

E-mail verification if is not perfect as per the requirement then **WARNING** will be displayed. It is used for sign-up and Login purpose.

## 5.haarcascade_frontalface_default.xml
This is the file of .xml format it is used for Face Recognition, frontalface_default means out of many other haarcascade we used this one to project the front part and not something particularly like eyes, nose, ears etc.

## 6.login.py
This is the starting page which includes user name and then it will start recognizing the face upto 200 photos if he found correct photo it will successfully login else Failed and can retry again.
After this page we can access other pages.

## 7.sign_up.py
This is the starting page which includes user name and email id and then it will start taking photos of the person and store in the folder which is uploaded here.
And during login the photos will be scaneed from that folder only and will successfully login if found correct.

## 8. mydatabase.db
This is the main part of the progrom because this includes all the data that we are using to get store in this like user name, email, amount and etc. 
Thus accessed all over the code to scan from this and c=make changes in this and store back.

## 9.sqliteHelper.py and sqlite_transaction.py
This both .py files are used to run the SQL queries as to make changes in the database and thus accessing from the database as well, so it is the library that we have used in the project.

## 10.Hisab_Kitab.py
This is **Main Code** in which we have included the GUI part and the accessing all the functions and the running of the code is this.
And all other files accessed in this we have discussed above individually.

## Limitations
Only one limitation is found that we can add many peoples transactions but can't make a group rather we need to select individual person who are part of that transaction.

# Libraries Used:
1.Pandas<br/>
2.OpenCV<br/>
3.Numpy<br/>
4.Tkitner<br/>
5.Datetime<br/>
6.uuid<br/>
7.dns.resolver<br/>
8.re<br/>
9.socket<br/>
10.smtplib<br/>
11.sqlite3<br/>
12.os<br/>

# Video
Here we have attached one video which explains whole output with individual parts like how to signup, login, recognize the face, add transaction, delete transaction, settle up, displaying all transaction.
