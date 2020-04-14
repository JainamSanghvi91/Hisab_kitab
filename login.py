from sqliteHelper import Sqlite
from Face_Recognise import Face_Recognize

class Log_in():
    def log_in(self,user_name):
        #variables
        ob=Sqlite()
        o=Face_Recognize()

        #checking if username is present in table
        x=ob.check_user(user_name)

        if x==0:
            #username is present and verifing face
            g=o.login(user_name)
            return g
        return "Username not found"
