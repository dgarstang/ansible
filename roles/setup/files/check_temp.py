#!/usr/bin/env python

import os
import smtplib
import platform
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

critical = False
high = 50
too_high = 80

def getCPUtemperature():
  res = os.popen('vcgencmd measure_temp').readline()
  return(res.replace("temp=","").replace("'C\n",""))

def main():
  temp = float(getCPUtemperature())
  if (temp > high):

    smtp_user = 'doug.garstang@gmail.com'
    smtp_password = 'dwengloszeotnapf'
    server = 'smtp.gmail.com'
    port = 587
    msg = MIMEMultipart("alternative")
    msg["From"] = smtp_user
    msg["To"] = "doug.garstang@gmail.com"
    node = platform.node()

    if temp > too_high:
      critical = True
      msg['subject'] = f"Critical warning! The temperature is: {temp} on node {node}."
      msg['body'] = f"Critical warning! The actual temperature is: {temp} \n\n."
    else:
      msg['subject'] = f"Warning! The temperature is: {temp} on node {node}."
      msg['body'] = f"Warning! The actual temperature is: {node}."

    s = smtplib.SMTP(server, port)
    s.ehlo()
    s.starttls()
    s.login(smtp_user, smtp_password)
    s.sendmail(smtp_user, "doug.garstang@gmail.com", msg.as_string())
    s.quit()

if __name__ == "__main__":
  main()
