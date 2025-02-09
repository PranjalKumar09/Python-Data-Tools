"""
Write a python program to translate a message into secret code language. 

Use the rules below to translate normal language

Coding:

if the word contains atleast 3 characters, remove the first letter and append at end
now append three random characters at starting and end

else simply reverse the string


myalgo -<<< 
coding 
remove first from starting and append first one at end
reverse 
add this much random in starting and end (len(string)/2)
add + len(all_stirng) to each character

decoding


>>>>

Decoding

if word less than 2 character 3 charcter reverse it
else
remove 3 random 
"""
import string
import random

def encoding(ip):
    ip = ip[1:] + ip[0]
    print(ip)
    ip = ip[::-1]
    print(ip)
    for i in range(0,int(len(ip)/2)):
        ip = random.choice(string.ascii_letters + string.digits ) + ip + random.choice(string.ascii_letters + string.digits )
    print(ip)
        
    for i in range(0,len(ip)):
        if ip[i] == " ": continue
        ip = ip[:i] + chr(ord(ip[i]) + len(ip)) + ip[i+1:]
        print(f"{i+1}-> {ip} ")
    print(ip)
    return ip

def decoding(op):
    for i in range(0,len(op)):
        op = op[:i] + chr(ord(op[i]) - len(op)) + op[i+1:]
    op = op[int(len(op) / 4) : len(op) - int(len(op) / 4) ] 
    op = op[::-1]
    
    op = op[-1] +op[:-1]
    return op


op = "frDDDkZqhml"
for i in range(0,len(op)):
        op = op[:i] + chr(ord(op[i]) - len(op)) + op[i+1:]
print(op)
choice = input("Whether you want to Encoing or Decoding Press(E or D) : ").upper()
if choice == "E":
    str = input("Enter the text you want to encode: ") 
    print(encoding(str))
elif choice == "D":
    str = input("Enter the text you want to decode: ") 
    print(decoding(str))
else: print("Invalid choice.")   




