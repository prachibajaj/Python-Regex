import re 

e = input("Enter the e-mail address")
if(re.search("[\w_%-+.]{1,20}\@w{2,20}\.\w{2,3}",e)):
    print("valid input")
else:
    print("invalid input")