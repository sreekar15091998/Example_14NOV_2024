import threading
import time
import subprocess , os
import operator


class Threading:

    def __init__(self):
        pass
        
    def logcat_logs(self,cmd):
        res=subprocess.check_output(cmd)
        
        
        
    def application_launch(self,adbcmd,expres):
        res=subprocess.check_output(adbcmd)
        expres=str(res)
        print("expected result",expres)
        
        if operator.contains(expres,res):
            print("Pass")  
            
        else:
            print("Faile")
        