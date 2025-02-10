"""The smtplib module in Python allows you to send email using the Simple Mail Transfer Protocol (SMTP). SMTP is a protocol for sending and receiving email over the internet. The smtplib module defines an SMTP client session object that can be used to connect to an SMTP server, authenticate, and send mail messages. Some of the methods and functions of the smtplib module are:

smtplib.SMTP(host, port, local_hostname, source_address) - This creates an SMTP object that represents a connection to an SMTP server. The arguments are the host name, port number, local host name, and source address of the client. If the host and port are not specified, the default values are used. The local host name is used in the HELO/EHLO command, and the source address is used to bind the socket to a specific address and port.

SMTP.connect(host, port) - This establishes a connection to the host and port specified in the SMTP object. It returns a tuple of the server response code and message. If the connection fails, an SMTPConnectError is raised.

SMTP.login(user, password) - This logs in to the SMTP server using the user name and password provided. It returns a tuple of the server response code and message. If the login fails, an SMTPAuthenticationError is raised.

SMTP.sendmail(from_addr, to_addrs, msg) - This method sends a mail message to one or more recipients. The arguments are the sender address, a list of recipient addresses, and the message as a string or bytes object. The message should include the headers and the body, separated by a blank line. The method returns a dictionary of failed recipients and the corresponding error codes. If the message is successfully sent, the dictionary is empty.

SMTP.quit() - This method terminates the SMTP session and closes the connection. It returns a tuple of the server response code and message. If the connection is already closed, an SMTPServerDisconnected is raised."""
import smtplib

sender = ""
receiver = ""

password = ""

subject = "Python email sent"
body  = "I wrote a jbgfkmn"

#header
message= f"""From: Pranjal Kumar Shukla{sender}
To: Pranjal Kumar Shukla{receiver}
Subject: {subject}\n
{body}
"""
try:
    server = smtplib.SMTP(sender ,587)
    status_code , respone = smtplib().ehlo()
    print(f"Encchosing the server: {status_code} ,{respone}")
    status_code , respone = smtplib.starttls()
    print(f"Starting the TLS connection: {status_code} ,{respone}")

    status_code , respone = smtplib.login(sender, password)
    print(f"Logging in : {status_code} ,{respone}")

    smtplib.sendmail(sender, message)

    smtplib.quit()  
except smtplib.SMTPConnectError as e:
    print("Connection error:", e)
except smtplib.SMTPAuthenticationError as e:
    print("Authentication error:", e)
except smtplib.SMTPSenderRefused as e:
    print("Sender refused:", e)
except smtplib.SMTPRecipientsRefused as e:
    print("Recipients refused:", e)
except smtplib.SMTPDataError as e:
    print("Data error:", e)
except smtplib.SMTPHeloError as e:
    print("HELO error:", e)
except smtplib.SMTPNotSupportedError as e:
    print("Not supported error:", e)
except smtplib.SMTPServerDisconnected as e:
    print("Server disconnected:", e)
except Exception as e:
    print("Other error:", e)