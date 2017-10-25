#!/usr/bin/env python3
# Dynamic IP Upstream and Reverse Proxy Nginx (dynipnginx)
# Use this script if you have a upsetram server with a dynamic ip address
# And using nginx as reverse Proxy

Domain='myserver-with-dynamic-ip-address.dyndns.org' #Domain to monitor (Make sure is the same that you have configured on nginx)
nginxBIN='/opt/nginx/sbin/nginx'    #Nginx Process path
logFile='/var/log/dynipcheck.log'
reCheck=30  #Seconds to monitor
################################################################################################################
import socket
import logging
import time
import sys
from subprocess import Popen,PIPE
LastIP=None
logging.basicConfig(filename=logFile,level=logging.DEBUG)

# Check if the computer can resolve IP Address or the domain name is correct
try:
        CurrentIP=socket.gethostbyname(Domain)
except:
        logging.error ("Please check the domain name " +  Domain)
        print ("Unable to validate domain " + Domain + " make sure the domain exists or this computer can resolve the address.")
        sys.exit(1)

while True:
        try:
                CurrentIP=socket.gethostbyname(Domain)
        except:
                logging.error ("Something is wrong while trying to validate the domain " +  Domain)
        if CurrentIP != LastIP:
                logging.info("IP of domain "+ Domain + " has changed.")
                logging.info ("Executing " + nginxBIN)
                process = Popen([nginxBIN,"-s","reload"],stdout=PIPE)
                (output, err) = process.communicate()
                exit_code = process.wait()
                LastIP = CurrentIP
        else:
                time.sleep (reCheck)



