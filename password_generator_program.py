import string
import random
import pickle

info = {}

with open("game.txt2","br") as filread:
    info = pickle.load(filread)

a = string.ascii_lowercase
# print(a)
b = string.ascii_uppercase
# print(b)
c = string.digits
# print(c)
d = string.punctuation
# print(d)
while True:
    try:
        plen = int(input("Enter the length of your password:\n"))
        break
    except ValueError:
        print("oops sorry!! you entered wrong input")

s = []
s.extend(list(a))
s.extend(list(b))
s.extend(list(c))
s.extend(list(d))

password = "".join(random.sample(s,plen))
print(password)

answer = input("would you like to keep this password: ")
if "yes" in answer:
    account_name = input("Enter account name: ")
    info[account_name] = password
    with open("game.txt2","bw") as filewrite:
        pickle.dump(info,filewrite)
else:
    print("ok!!")

#-----------------2nd part--------------------#

import pickle

m_password = input("Enter master password:")
if m_password == "Abssssss1753":
    account_name = input("Enter the account name:")
    with open("game.txt2","br") as fileread:
        info = pickle.load(fileread)

    if account_name in info:
        print("password=",info[account_name])
    else:
        print("Sorry!! password not found")
else:
    print("password doesn't match.Please try again!!")







