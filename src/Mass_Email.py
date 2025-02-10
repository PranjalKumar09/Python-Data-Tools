
# NOT RUNNING dont know reason 

import smtplib as smt

ob = smt.SMTP('smtp.gmail.com', 587)

email_i = input("Enter the email address : ")
password = input("Enter the password : ")

ob.ehlo()
ob.starttls()
ob.login(email_i, password)

subject = input("Enter the subject : ")
body = input("Enter the body : ")
message = "Subject:{}\n\n{}".format(subject, body)

listadd = []
while True:
    i = input("Enter the Email Address (type 'e' to end the list): ")
    if i.lower() == "e":
        break
    listadd.append(i)

ob.sendmail(email_i, listadd, message)

print("Mail Sent")

ob.quit()
