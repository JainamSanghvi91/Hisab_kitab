from email_verify import Email_verify
from sqliteHelper import Sqlite
from Face_Recognise import Face_Recognize
import uuid
import os

class Sign_up():
    def sign_up(self,user_name,email):
        
        # 1) Functions variables
        ob=Sqlite()
        x=Email_verify()
        face=Face_Recognize()
                
        # 2) User name verification
        y=ob.check_user(user_name)
        if y==0:
            return "Username Already Exists"
                

        # 3) Email Id Verification
        t=x.verify_email(email)
        if t==-1:
            return "Invalid Formate of Email"
        elif t==0:
            return "Email doesn't exists"
            email=input("Email_Id")
            t=x.verify_email(email)
            
        # 4) Face_Recognition Verification
        data_path='./user_photo/'
        flag=0

        #Creating folder for new_user
        os.mkdir(data_path+user_name)

        #Taking photos and storing in folder created
        u=face.Signup(user_name)
        
        if u==1:
            #Generating Id for new_user
            user_id=str(uuid.uuid4())
            li=[]
            li.append(user_id)
            li.append(user_name)
            li.append(email)

            #Inserting user data in table
            ob.insert_user(li)
            return ""
        else:
            return "Try Again"