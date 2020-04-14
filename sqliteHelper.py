import sqlite3

from sqlite3 import Error

class Sqlite():
    def __init__(self):
        try:
            self.con = sqlite3.connect('mydatabase.db')
        except Error:
            print(Error)

    def sql_table(self):

       cursorObj = self.con.cursor()

       cursorObj.execute("CREATE TABLE personal_details(p_id text PRIMARY KEY, user_name text, user_email text)")

       self.con.commit()

    def insert_user(self,entities):
        cursorObj = self.con.cursor()
        
        cursorObj.execute('INSERT INTO personal_details(p_id, user_name , user_email ) VALUES(?, ?, ?)', entities)
        
        self.con.commit()

    def find_id_by_username(self,username):
        cursorObj = self.con.cursor()
        names=cursorObj.execute('Select p_id from personal_details where user_name=?',(username,))
        for i in names:
            return i[0]
        self.con.commit()

    def find_username_by_id(self,p_id):
        cursorObj = self.con.cursor()
        names=cursorObj.execute('Select user_name from personal_details where p_id=?',(p_id,))
        for i in names:
            return i[0]
        self.con.commit()

    def find_email_by_username(self,username):
        cursorObj = self.con.cursor()
        names=cursorObj.execute('Select user_email from personal_details where user_name=?',(username,))
        for i in names:
            return i[0]
        self.con.commit()

    def find_if_username_exist(self,username):
        cursorObj = self.con.cursor()
        names=cursorObj.execute('Select user_name from personal_details')
        for i in names:
            for j in i:
                if username==j:
                    return True
        return False
        self.con.commit()

    def check_user(self,name):
        cursorObj = self.con.cursor()
        names=cursorObj.execute('Select user_name from personal_details')
        flag=0
        for i in names:
            for j in i:
                print(j)
                if name==j:
                    print("here")
                    flag=-1
                    break
            if flag==-1:
              break
        if flag==-1:
            return 0
        else:
            return 1
        self.con.commit()
