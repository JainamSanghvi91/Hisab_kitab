import sqlite3
import datetime
from sqlite3 import Error
from sqliteHelper import Sqlite

class Sqlite_trans():
    def __init__(self):
        self.sq=Sqlite()
        try:
            self.con = sqlite3.connect('mydatabase.db')
        except Error:
            print(Error)

    def sql_table(self):
        cursorObj = self.con.cursor()
        cursorObj.execute(
            "CREATE TABLE transactions_detail(t_id text PRIMARY KEY, from_p_id text,to_p_id text,total_amount real,amount_owe real,description_trans text,date_trans datetime,status_tran char)")

        self.con.commit()

    def insert_transaction(self, entities):
        cursorObj = self.con.cursor()

        cursorObj.execute(
            "INSERT INTO transactions_detail(t_id, from_p_id ,to_p_id,total_amount,amount_owe,description_trans,date_trans,status_tran) VALUES(?, ?, ?,?,?,?,?,?)", entities)

        self.con.commit()

    def customized_transaction(self,user_id,type):
        cursorObj = self.con.cursor()
        names=cursorObj.execute('Select * from transactions_detail where (from_p_id=? or to_p_id=?) and status_tran=?',(user_id,user_id,type,))
        di={}
        for i in names: 
            if i[1]==user_id: 
                if i[2] in di.keys():
                    di[i[2]]['Amount']+=i [3]
                    di[i[2]]['Amount_owe' ]+=i[4]
                else: 
                    di[i[2]]={} 
                    di[i[2]]['Amount']=i[3]
                    di[i[2]]['Amount_owe']=i[4]
            elif i[2]==user_id: 
                if i[1] in di.keys(): 
                    di[i[1]]['Amount']+=i[3]
                    di[i[1]]['Amount_owe']-=i[4]
                else:
                    di[i[1]]={}
                    di[i[1]]['Amount']=i[3]
                    di[i[1]]['Amount_owe']=0-i[4]
        return di
        self.con.commit()

    def my_transactions(self,user_id):
        cursorObj = self.con.cursor()
        names=cursorObj.execute('Select * from transactions_detail where (from_p_id=? or to_p_id=?) and status_tran=?',(user_id,user_id,'N',))
        na=list(names)
        na.reverse()
        return na
        self.con.commit()

    def particular_trans(self,user_id,to_id,type):
        cursorObj = self.con.cursor()
        names=cursorObj.execute('Select * from transactions_detail where (from_p_id=? or from_p_id=? )and (to_p_id=? or to_p_id=? ) and status_tran=?',(to_id,user_id,to_id,user_id,type,))
        na=list(names)
        na.reverse()
        return na
        self.con.commit()

    def settle_up(self,user_id,to_id):
        cursorObj = self.con.cursor()
        cursorObj.execute('UPDATE transactions_detail set status_tran=? where (from_p_id=? or from_p_id=? )and (to_p_id=? or to_p_id=? )',("C",user_id,to_id,user_id,to_id))
        self.con.commit()

    def delete_trans(self,t_id):
        cursorObj = self.con.cursor()
        cursorObj.execute('DELETE from transactions_detail where t_id=?',(t_id,))
        print("deleted")
        self.con.commit()

