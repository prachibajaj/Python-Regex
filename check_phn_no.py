import re

p = input("Enter a phone number")
if(re.search("\+\w{2}-\w{3}-\w{4}",p)):
   print('It\'s a phone number')  