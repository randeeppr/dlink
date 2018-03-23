#!/usr/bin/python3.4
# Written by Randeep P R randeeep123@gmail.com
# www.linuxhelp.in
import requests, urllib, json, hmac, re

# Declare variables
userid = "Admin"
password = b"xyz"

# Create session
session = requests.Session()

# initial call to generate cookie
req1 = session.get('http://xx.xx.xx.xx/authentication.cgi?captcha=&dummy=1522056612289',verify=False)
res1 = req1.text

# Get the values of cookie and challenge
d = json.loads(res1)
cookie = {"uid": d['uid']}
challenge = d['challenge']

# Generate the digest
mix = userid + challenge;
digest = hmac.new(password,mix.encode('utf-8')).hexdigest()
digest = digest.upper()

# Create the payload
payload = {'id':'Admin','password':digest}

# set the header
headers = {'Cookie': 'uid={0}'.format(d['uid']),'Content-Type': 'application/x-www-form-urlencoded'}

# Second call to log ino the device
res2 = session.post('http://xx.xx.xx.xx/authentication.cgi',data=payload,cookies=cookie)
#print(res2.text)

# Once logged in call the Wireless page
req3 = session.get('http://xx.xx.xx.xx/bsc_wlan.php',cookies=cookie)
res3 = req3.text

#print(res3)
if re.search("""<div id="div_24G" class="blackbox">""",res3,re.IGNORECASE):
   print("Found")
else:
   print("Not found")
# "TODO"
# Write the code to check the required configuration
