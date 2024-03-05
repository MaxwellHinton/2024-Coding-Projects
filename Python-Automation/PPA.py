'''
This Python-Automation file will serve as a base for multiple personal Python scripts
aimed at improving quality of life for myself on my PC.
   
First script - Line 15: Program to restrict access to a specific folder according to the current sytems time.
'''

import os
import sched
import time
import datetime
import subprocess
import threading

''' Script outline:

    Need to gather the systems current time and check for a condition

    --The condition--

    If the current time is within 09:00 and 19:00, do not allow access to the folder. 
    Run on computer start up.

'''

games_folder = r"C:\Users\maxhi\OneDrive\Desktop\test_folder"

def restrict_access():
    current_system_time = datetime.datetime.now().time()

    if datetime.time(9,0) <= current_system_time <= datetime.time(19,0):
        # Restrict access to the folder
        subprocess.run(['icacls', games_folder, "/deny", "Everyone:(R)"], shell=True, check=True)

    else:
        subprocess.run(['icacls', games_folder, "/reset"], shell=True, check=True)

def run_function():
    thread = threading.Timer(60.0, run_function)
    thread.start()
    restrict_access()

run_function()

