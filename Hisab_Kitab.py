import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from sign_up import Sign_up
from login import Log_in
from Add_Transaction import Add_transaction
from sqlite_transaction import Sqlite_trans
from sqliteHelper import Sqlite
import datetime
import pandas as pd
from functools import partial

LARGE_FONT=("bold",20)
M_FONT=("Verdana",12)
A_FONT=("Verdana",16)
sign=Sign_up()
log=Log_in()
add_t=Add_transaction()
sqlite_trans=Sqlite_trans()
sq=Sqlite()
class Hisaab_kitaab(tk.Tk):
    def __init__(self,*args,**kwargs):
        tk.Tk.__init__(self,*args,**kwargs)
       
        tk.Tk.wm_title(self,"Hisaab-kitaab")
        container=tk.Frame(self)

        container.pack(side="top",fill="both",expand=True)

        container.grid_rowconfigure(0,weight=1)
        container.grid_columnconfigure(0,weight=1)

        self.frames={}
        for F in (StartPage,SignUp,LogIn,Add_transaction,Customized,Show_All,All_Transactions,Completed_trans):
            frame=F(container,self)
            self.frames[F]=frame
            frame.grid(row=0,column=0,sticky="nsew")
        self.show_frame(StartPage)

    def show_frame(self,cont):
        frame=self.frames[cont]
        frame.tkraise()

class StartPage(tk.Frame):
    def __init__(self,parent,controller):
        self.controller=controller
        tk.Frame.__init__(self,parent)

        #Heading
        label=ttk.Label(self,text="Hisaab-kitaab",font=LARGE_FONT,foreground="black")
        label.pack(pady=50,padx=10)

        #Move to LogIn Page 
        self.button2=ttk.Button(self,text="Login",width=30,
                          command=lambda: controller.show_frame(LogIn))
        self.button2.pack(pady=10)

        #Move to SignUp page
        self.button2=ttk.Button(self,text="Sign in",width=30,
                          command=lambda: controller.show_frame(SignUp))
        self.button2.pack(pady=10)

class LogIn(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        self.controller=controller
       
        #Heading
        self.label=tk.Label(self,text="Login",font=LARGE_FONT)
        self.label.place(y=50,x=700)
       
        #Username
        self.label=tk.Label(self,text="Username",font=M_FONT)
        self.label.place(y=150,x=550)
        self.username=tk.Entry(self,bd=1,width=50)
        self.username.place(x=650,y=150)
       
        #Password of your id
        button1=ttk.Button(self,text="Face-Recognization",
                          command=lambda: self.log_in())
        button1.place(x=700,y=200)

        #Bcak to main screen
        button1=ttk.Button(self,text="Back to Home",
                          command=lambda: self.controller.show_frame(StartPage))
        button1.place(x=715,y=250)

    def log_in(self):
        #Calling function Log_in 
        t=log.log_in(self.username.get())

        #Checking if any warning occurs
        if t!="":
            messagebox.showwarning("Warning",t)
        else:
            self.controller.user_name=self.username.get()
            self.username.delete(0,100)
            self.controller.frames[Customized].list_of_Customized()
            self.controller.show_frame(Customized)


           
class SignUp(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        self.controller=controller

        #Heading
        self.label=tk.Label(self,text="Sign-in",font=LARGE_FONT)
        self.label.place(y=50,x=650)

        #Username
        self.label=tk.Label(self,text="Username",font=M_FONT)
        self.label.place(y=150,x=500)
        self.username=tk.Entry(self,bd=1,width=50)
        self.username.place(x=600,y=150)

        #Email id
        self.label=tk.Label(self,text="E-mail",font=M_FONT)
        self.label.place(y=200,x=500)
        self.email=tk.Entry(self,bd=1,width=50)
        self.email.place(x=600,y=200)

        #To store photos and sign_up
        self.button3=ttk.Button(self,text="Take photos",width=25,command=lambda: self.sign_up())
        self.button3.place(x=660,y=250)

        #Back to main screen
        button1=ttk.Button(self,text="Back to Home",
                          command=lambda: self.controller.show_frame(StartPage))
        button1.place(x=700,y=300)

    def sign_up(self):
        #To sign_up
        t=sign.sign_up(str(self.username.get()),str(self.email.get()))

        #Check if any invalid input
        if t=="":
            self.controller.user_name=self.username.get()
            self.username.delete(0,100)
            self.email.delete(0,100)
            self.controller.frames[Customized].list_of_Customized()
            self.controller.show_frame(Customized)
        else:
            messagebox.showwarning("Warning",t)

   

class Add_transaction(tk.Frame):
    def __init__(self,parent,controller):
        self.controller=controller
        tk.Frame.__init__(self,parent)

        #Heading and Menu Table
        label=ttk.Label(self,text="Hisaab-kitaab",font=LARGE_FONT)
        label.pack(pady=20,padx=10)
        label=ttk.Label(self,text="Add-Transaction",font=A_FONT)
        label.pack(pady=20,padx=10)
        self.button3=ttk.Button(self,text="Customized Transactions",width=20,command=lambda:self.move_to_customize())
        self.button3.place(x=300,y=150)
        self.button3=ttk.Button(self,text="All Transactions",width=20,command=lambda:self.move_to_all_trans())
        self.button3.place(x=500,y=150)
        self.button3=ttk.Button(self,text="Add Transactions",width=20,command=lambda:self.move_to_add_trans())
        self.button3.place(x=700,y=150)
        self.button3=ttk.Button(self,text="Completed Transactions",width=20,command=lambda:self.move_to_complete())
        self.button3.place(x=900,y=150)
        self.button3=ttk.Button(self,text="Log out",width=20,command=lambda:self.logout())
        self.button3.place(x=1100,y=150)

        #Name of person 
        self.label=tk.Label(self,text="With you and:",font=M_FONT)
        self.label.place(y=200,x=475)
        self.with_you_and=tk.Entry(self,bd=1,width=50)
        self.with_you_and.place(x=650,y=200)

        #Amount of transaction
        self.label=tk.Label(self,text="Amount:",font=M_FONT)
        self.label.place(y=250,x=475)
        self.amount=tk.Entry(self,bd=1,width=50)
        self.amount.place(x=650,y=250)

        #Detail of transaction
        self.label=tk.Label(self,text="Details",font=M_FONT)
        self.label.place(y=300,x=475)
        self.description=tk.Entry(self,bd=1,width=50)
        self.description.place(x=650,y=300)

        #Type of transaction
        self.label=tk.Label(self,text="Type:",font=M_FONT)
        self.label.place(y=350,x=475)
        self.v=tk.IntVar()
        self.v.set(1)

        #First option
        R1=tk.Radiobutton(self, text="Your opponent owes the full Amount",variable=self.v,value="1")
        R1.place(x=650,y=380)

        #second button
        R2 = tk.Radiobutton(self, text="50-50",variable=self.v,value="2")
        R2.place(x=650,y=350)

        #To add transaction
        self.button3=ttk.Button(self,text="Add",width=25,command=lambda: self.add_trans())
        self.button3.place(x=660,y=440)


    def add_trans(self):
        #To add transaction to table
        t=add_t.add_transaction(self.controller.user_name,self.with_you_and.get(),int(self.amount.get()),self.description.get(),self.v.get())
        
        #To check if any wrong with transaction
        if t=="":
            self.with_you_and.delete(0,100)
            self.amount.delete(0,100)
            self.description.delete(0,100)
            self.v.set(1)
            messagebox.showwarning("Completed","Transaction added")
        else:
            messagebox.showwarning("Warning",t)

    def logout(self):
        self.controller.show_frame(StartPage)

    def move_to_customize(self):
        self.controller.frames[Customized].list_of_Customized()
        self.controller.show_frame(Customized)
   
    def move_to_add_trans(self):
        self.controller.show_frame(Add_transaction)

    def move_to_all_trans(self):
        self.controller.frames[All_Transactions].all_trans()
        self.controller.show_frame(All_Transactions)
    
    def move_to_complete(self):
        self.controller.frames[Completed_trans].list_of_Completed()
        self.controller.show_frame(Completed_trans)

class Customized(tk.Frame):
    def __init__(self,parent,controller):
        self.controller=controller
        tk.Frame.__init__(self,parent)

    def list_of_Customized(self):
        for i in self.winfo_children():
            i.destroy()

        #variables
        x1=150
        y1=200
        k=1

        #Fetching data from table
        self.t=sqlite_trans.customized_transaction(sq.find_id_by_username(self.controller.user_name),'N')
        
        #Heading and Menu Buttons
        label=ttk.Label(self,text="Hisaab-kitaab",font=LARGE_FONT)
        label.pack(pady=20,padx=10)
        label=ttk.Label(self,text="Customized Transactions",font=A_FONT)
        label.pack(pady=20,padx=10)
        self.button3=ttk.Button(self,text="Customized Transactions",width=20,command=lambda:self.move_to_customize())
        self.button3.place(x=300,y=150)
        self.button3=ttk.Button(self,text="All Transactions",width=20,command=lambda:self.move_to_all_trans())
        self.button3.place(x=500,y=150)
        self.button3=ttk.Button(self,text="Add Transactions",width=20,command=lambda:self.move_to_add_trans())
        self.button3.place(x=700,y=150)
        self.button3=ttk.Button(self,text="Completed Transactions",width=20,command=lambda:self.move_to_complete())
        self.button3.place(x=900,y=150)
        self.button3=ttk.Button(self,text="Log out",width=20,command=lambda:self.logout())
        self.button3.place(x=1100,y=150)
        
        #Checking if list of transaction is empty
        if not bool(self.t):
            label=ttk.Label(self,text="No Transactions Pending",font=("Helvetica", 16))
            label.place(x=650,y=400)
        else:
            #Heading for list of transaction 
            label=ttk.Label(self,text="Username")
            label.place(x=x1+250,y=200)
            label=ttk.Label(self,text="Amount owe")
            label.place(x=x1+450,y=200)
            label=ttk.Label(self,text="Total Amount")
            label.place(x=x1+550,y=200)

            #All the trasactions
            for i in self.t.keys():
                #Username
                label=ttk.Label(self,text=sq.find_username_by_id(i))
                label.place(x=x1+250,y=y1+30*k)

                #Check if user have to pay money if so then red fonts
                if self.t[i]['Amount_owe']<0:
                    self.t[i]['Amount_owe']=0-self.t[i]['Amount_owe']
                    label=ttk.Label(self,foreground="red",text=self.t[i]['Amount_owe'])
                else:
                    label=ttk.Label(self,foreground="green",text=self.t[i]['Amount_owe'])
                label.place(x=x1+450,y=y1+30*k)

                #Total Amount of transaction
                label=ttk.Label(self,text=self.t[i]['Amount'])
                label.place(x=x1+550,y=y1+30*k)

                #To show all the transactions related to these entry
                button2=ttk.Button(self,text="Show All",width=10,command=partial(self.move_to_all,i))
                button2.place(x=x1+650,y=y1+30*k)

                #To settle up the transactions
                button3=ttk.Button(self,text="Settle up",width=10,command=partial(self.settle_up,i))
                button3.place(x=x1+750,y=y1+30*k)
                k+=1;

    def settle_up(self,i):
        sqlite_trans.settle_up(sq.find_id_by_username(self.controller.user_name),i)
        self.list_of_Customized()

    def move_to_all(self,i):
        self.controller.type='N'
        self.controller.show_username=sq.find_username_by_id(i)
        self.controller.frames[Show_All].show()
        self.controller.show_frame(Show_All)

    def move_to_complete(self):
        self.controller.frames[Completed_trans].list_of_Completed()
        self.controller.show_frame(Completed_trans)
    def logout(self):
        self.controller.show_frame(StartPage)

    def move_to_customize(self):
        self.controller.frames[Customized].list_of_Customized()
        self.controller.show_frame(Customized)
   
    def move_to_add_trans(self):
        self.controller.show_frame(Add_transaction)

    def move_to_all_trans(self):
        self.controller.frames[All_Transactions].all_trans()
        self.controller.show_frame(All_Transactions)
    

class Show_All(tk.Frame):
    def __init__(self,parent,controller):
        self.controller=controller
        tk.Frame.__init__(self,parent)
       
    def go_back(self):
        if self.controller.type=='N':
            self.controller.frames[Customized].list_of_Customized()
            self.controller.show_frame(Customized)
        else:
            self.controller.frames[Completed_trans].list_of_Completed()
            self.controller.show_frame(Completed_trans)

    def show(self):
        for i in self.winfo_children():
            i.destroy()

        #variables
        x1=150
        y1=200
        k=1

        #Fetching data from table
        t=sqlite_trans.particular_trans(sq.find_id_by_username(self.controller.user_name),sq.find_id_by_username(self.controller.show_username),self.controller.type)
        
        #Heading
        label=ttk.Label(self,text="Hisaab-kitaab",font=LARGE_FONT)
        label.pack(pady=20,padx=10)
        label=ttk.Label(self,text="Transaction with "+self.controller.show_username,font=A_FONT)
        label.pack(pady=20,padx=10)
       
        #Going back to Customized Transactions
        button3=ttk.Button(self,text="Back",width=20,command=lambda:self.go_back())
        button3.pack(pady=20,padx=10)
        button3.place(x=350,y=150)
        

        #Heading for list of transactions
        self.label=ttk.Label(self,text="From")
        self.label.place(x=x1+200,y=200)
        self.label=ttk.Label(self,text="To")
        self.label.place(x=x1+300,y=200)
        self.label=ttk.Label(self,text="Amount owe")
        self.label.place(x=x1+400,y=200)
        self.label=ttk.Label(self,text="Total Amount")
        self.label.place(x=x1+500,y=200)
        self.label=ttk.Label(self,text="Detail")
        self.label.place(x=x1+600,y=200)
        self.label=ttk.Label(self,text="Time")
        self.label.place(x=x1+700,y=200)

        #List of transactions
        for i in t:
            #From
            self.label=ttk.Label(self,text=sq.find_username_by_id(i[1]))
            self.label.place(x=x1+200,y=y1+30*k)

            #To
            self.label=ttk.Label(self,text=sq.find_username_by_id(i[2]))
            self.label.place(x=x1+300,y=y1+30*k)

            #Amount owe
            if sq.find_username_by_id(i[2])==self.controller.user_name:
                self.label=ttk.Label(self,text=i[4],foreground="red")
            else:
                self.label=ttk.Label(self,text=i[4],foreground="green")
            self.label.place(x=x1+400,y=y1+30*k)

            #Total Amount
            self.label=ttk.Label(self,text=i[3])
            self.label.place(x=x1+500,y=y1+30*k)

            #Details
            self.label=ttk.Label(self,text=i[5])
            self.label.place(x=x1+600,y=y1+30*k)

            #Time
            s=str((datetime.datetime.now()-pd.to_datetime(i[6])).days)
            if(s=="0"):
                self.label=ttk.Label(self,text="today")
            else:
                self.label=ttk.Label(self,text=(s+" days ago"))
            self.label.place(x=x1+700,y=y1+30*k)

            #For deleting chosen transaction
            self.button3=ttk.Button(self,text="Delete",width=10,command=partial(self.delete_it,i))
            self.button3.place(x=x1+850,y=y1+30*k)
            k+=1;
   
    def delete_it(self,i):
        sqlite_trans.delete_trans(i[0])
        self.show()
   
class Completed_trans(tk.Frame):
    def __init__(self,parent,controller):
        self.controller=controller
        tk.Frame.__init__(self,parent)

    def list_of_Completed(self):
        for i in self.winfo_children():
            i.destroy()

        #variables
        x1=150
        y1=200
        k=1

        #Fetching list of transaction from table
        self.t=sqlite_trans.customized_transaction(sq.find_id_by_username(self.controller.user_name),'C')
        
        #Gui for Heading and Menu Buttons
        label=ttk.Label(self,text="Hisaab-kitaab",font=LARGE_FONT)
        label.pack(pady=20,padx=10)
        label=ttk.Label(self,text="Customized Transactions",font=A_FONT)
        label.pack(pady=20,padx=10)
        self.button3=ttk.Button(self,text="Customized Transactions",width=20,command=lambda:self.move_to_customize())
        self.button3.place(x=300,y=150)
        self.button3=ttk.Button(self,text="All Transactions",width=20,command=lambda:self.move_to_all_trans())
        self.button3.place(x=500,y=150)
        self.button3=ttk.Button(self,text="Add Transactions",width=20,command=lambda:self.move_to_add_trans())
        self.button3.place(x=700,y=150)
        self.button3=ttk.Button(self,text="Completed Transactions",width=20,command=lambda:self.move_to_complete())
        self.button3.place(x=900,y=150)
        self.button3=ttk.Button(self,text="Log out",width=20,command=lambda:self.logout())
        self.button3.place(x=1100,y=150)
        

        #Chceking if the list of transaction is empty
        if not bool(self.t):
            label=ttk.Label(self,text="No Transactions Completed",font=("Helvetica", 16))
            label.place(x=650,y=400)
        else:
            label=ttk.Label(self,text="Username")
            label.place(x=x1+250,y=200)
            label=ttk.Label(self,text="Amount owe")
            label.place(x=x1+450,y=200)
            label=ttk.Label(self,text="Total Amount")
            label.place(x=x1+550,y=200)

            #List of Transactions
            for i in self.t.keys():
                label=ttk.Label(self,text=sq.find_username_by_id(i))
                label.place(x=x1+250,y=y1+30*k)

                #If amount is to be paid then it is shown in red otherwise green
                if self.t[i]['Amount_owe']<0:
                    self.t[i]['Amount_owe']=0-self.t[i]['Amount_owe']
                    label=ttk.Label(self,foreground="red",text=self.t[i]['Amount_owe'])
                else:
                    label=ttk.Label(self,foreground="green",text=self.t[i]['Amount_owe'])
                label.place(x=x1+450,y=y1+30*k)
                label=ttk.Label(self,text=self.t[i]['Amount'])
                label.place(x=x1+550,y=y1+30*k)

                #Move to screen Show_All
                button2=ttk.Button(self,text="Show All",width=10,command=partial(self.move_to_all,i))
                button2.place(x=x1+650,y=y1+30*k)
                k+=1;

    def move_to_all(self,i):
        self.controller.show_username=sq.find_username_by_id(i)
        self.controller.type='C'
        self.controller.frames[Show_All].show()
        self.controller.show_frame(Show_All)

    def move_to_complete(self):
        self.controller.frames[Completed_trans].list_of_Completed()
        self.controller.show_frame(Completed_trans)
    def logout(self):
        self.controller.show_frame(StartPage)

    def move_to_customize(self):
        self.controller.frames[Customized].list_of_Customized()
        self.controller.show_frame(Customized)
   
    def move_to_add_trans(self):
        self.controller.show_frame(Add_transaction)

    def move_to_all_trans(self):
        self.controller.frames[All_Transactions].all_trans()
        self.controller.show_frame(All_Transactions)

class All_Transactions(tk.Frame):
    def __init__(self,parent,controller):
        self.controller=controller
        tk.Frame.__init__(self,parent)
   
    def all_trans(self):
        for i in self.winfo_children():
            i.destroy()

        #variables
        x1=150
        y1=200
        k=1

        #Fetching information of transaction from table
        t=sqlite_trans.my_transactions(sq.find_id_by_username(self.controller.user_name))
        
        #Gui for Common Buttons and Heading
        self.label=ttk.Label(self,text="Hisaab-kitaab",font=LARGE_FONT)
        self.label.pack(pady=20,padx=10)
        self.label=ttk.Label(self,text="All-Transaction",font=A_FONT)
        self.label.pack(pady=20,padx=10)
        self.button3=ttk.Button(self,text="Customized Transactions",width=20,command=lambda:self.move_to_customize())
        self.button3.place(x=300,y=150)
        self.button3=ttk.Button(self,text="All Transactions",width=20,command=lambda:self.move_to_all_trans())
        self.button3.place(x=500,y=150)
        self.button3=ttk.Button(self,text="Add Transactions",width=20,command=lambda:self.move_to_add_trans())
        self.button3.place(x=700,y=150)
        self.button3=ttk.Button(self,text="Completed Transactions",width=20,command=lambda:self.move_to_complete())
        self.button3.place(x=900,y=150)
        self.button3=ttk.Button(self,text="Log out",width=20,command=lambda:self.logout())
        self.button3.place(x=1100,y=150)
        
        #Checking if the list of transactions is empty 
        if not bool(t):
            label=ttk.Label(self,text="No Transactions Pending",font=("Helvetica", 16))
            label.place(x=650,y=400)
        else:
            self.label=ttk.Label(self,text="From")
            self.label.place(x=x1+200,y=200)
            self.label=ttk.Label(self,text="To")
            self.label.place(x=x1+300,y=200)
            self.label=ttk.Label(self,text="Amount owe")
            self.label.place(x=x1+400,y=200)
            self.label=ttk.Label(self,text="Total Amount")
            self.label.place(x=x1+500,y=200)
            self.label=ttk.Label(self,text="Detail")
            self.label.place(x=x1+600,y=200)
            self.label=ttk.Label(self,text="Time")
            self.label.place(x=x1+700,y=200)

            #List of All transactions
            for i in t:
                self.label=ttk.Label(self,text=sq.find_username_by_id(i[1]))
                self.label.place(x=x1+200,y=y1+30*k)
                self.label=ttk.Label(self,text=sq.find_username_by_id(i[2]))
                self.label.place(x=x1+300,y=y1+30*k)
                self.label=ttk.Label(self,text=i[3])
                self.label.place(x=x1+500,y=y1+30*k)

                #If the user have to pay then it is shown in red otherwise green
                if sq.find_username_by_id(i[2])==self.controller.user_name:
                    self.label=ttk.Label(self,text=i[4],foreground="red")
                else:
                    self.label=ttk.Label(self,text=i[4],foreground="green")
                self.label.place(x=x1+400,y=y1+30*k)
                self.label=ttk.Label(self,text=i[5])
                self.label.place(x=x1+600,y=y1+30*k)
                
                #Finding the number of days after the transaction
                s=str((datetime.datetime.now()-pd.to_datetime(i[6])).days)
                if(s=="0"):
                    self.label=ttk.Label(self,text="today")
                else:
                    self.label=ttk.Label(self,text=(s+" days ago"))
                self.label.place(x=x1+700,y=y1+30*k)

                #For deleting the chosen transaction
                self.button3=ttk.Button(self,text="Delete",width=10,command=partial(self.delete_it,i))
                self.button3.place(x=x1+800,y=y1+30*k)
                k+=1;
    
    def delete_it(self,i):
        sqlite_trans.delete_trans(i[0])
        self.all_trans()

    def logout(self):
        self.controller.show_frame(StartPage)

    def move_to_customize(self):
        self.controller.frames[Customized].list_of_Customized()
        self.controller.show_frame(Customized)
   
    def move_to_add_trans(self):
        self.controller.show_frame(Add_transaction)

    def move_to_complete(self):
        self.controller.frames[Completed_trans].list_of_Completed()
        self.controller.show_frame(Completed_trans)

    def move_to_all_trans(self):
        self.controller.frames[All_Transactions].all_trans()
        self.controller.show_frame(All_Transactions)


app=Hisaab_kitaab()
app.mainloop()