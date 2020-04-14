from sqliteHelper import Sqlite
from sqlite_transaction import Sqlite_trans
from Send_mail import Send_Email
import uuid
import datetime
from email.message import EmailMessage

class Add_transaction():
    def __init__(self):
        self.sq = Sqlite()
        self.mail=Send_Email()
        self.sq_trans = Sqlite_trans()

    def add_transaction(self,user_name,transaction_to,amount,description,transaction_type):
        if self.sq.find_if_username_exist(transaction_to):
            print("User found")
            amount_owe = -1
            lis = []
            if not str(amount).isdigit:
                return "Invalid input in Amount"
            elif description=="":
                return "Details is empty"
            elif transaction_type == 1 or transaction_type ==2:
                #Generating id for transaction
                trans_id = str(uuid.uuid4())
                if transaction_type==1:
                    amount_owe=amount/2
                else:
                    amount_owe=amount

                lis=(trans_id,self.sq.find_id_by_username(user_name),self.sq.find_id_by_username(transaction_to),amount,amount_owe,description, datetime.datetime.now(),'N')
                
                #Storing transaction in table
                self.sq_trans.insert_transaction(lis)
                print("transaction done")
                #Sending mail   
                message="Detail: "+description+"\nFrom: "+user_name+"\nTotal Amount:"+str(amount)+"\nAmount to pay:"+str(amount_owe);
                self.mail.send_mail(self.sq.find_email_by_username(transaction_to),user_name,message)
                print("Message sent")
                return "Successfully done"
            else:
                return "Invalid input"
        else:
            return "User not Found"