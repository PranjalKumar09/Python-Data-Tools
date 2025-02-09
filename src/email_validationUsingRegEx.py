""" 
First Condtion -> a-z 
Second Condtion -> 0-9 
Third Condtion -> only one (dot (.) and underscore (_) and @)

"""
import re
email_condtion = "^[a-z]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$"


""" 
[] -> is set any one in this should ... 
^[a-z] -> tells that it starts from lowercase letter
\	Signals a special sequence (can also be used to escape special characters)

? Matches zero or one repetition

+-> -> 1 or more repetitions

\w	Returns a match where the string contains any word characters 

$ for ed

"""
user_email = input("Enter email address: ")

if (re.search(email_condtion, user_email)):
    print( " Right email ")
# else:
    print( " Wrong email ")
