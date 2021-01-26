#!/usr/bin/env python3

import paramiko
import time

hostname = input("remote host ip: ")
username = input("remote host username: ")
password = ""
scriptname = input("script name: ")

start_time = time.time()

print("")
print("*******************START*******************")
print("")

# initialize the SSH client
client = paramiko.SSHClient()
# add to known hosts
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
try:
    client.connect(hostname=hostname, username=username, password=password)
except:
    print("[!] Cannot connect to the SSH Server")
    exit()

# read the BASH script content from the file
bash_script = open(scriptname).read()
# execute the BASH script
stdin, stdout, stderr = client.exec_command(bash_script)
time.sleep(5)
# read the standard output and print it
print(stdout.read().decode())
# print errors if there are any
err = stderr.read().decode()
if err:
    print(err)
# close the connection
client.close()

print("********************END********************")

print("")

print("execution time: %s seconds" % (time.time() - start_time))