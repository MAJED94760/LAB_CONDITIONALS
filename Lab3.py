name = input ("Enter you name ")
email = input ("Enter you email ")

if len(name)>=2 and email.endswith ("@gmail.com"):
    print (name,"you registered ", email)
elif len(name)<2:
    print ("the name length must be more than 2 characters, please provide a valid name")
else:
    print (" the email is not valid , please provide a valid email")
