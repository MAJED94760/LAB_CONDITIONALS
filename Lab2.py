wieght= float(input("Enter you wieght "))

height = float(input ("Enter you height "))

sequer_height = height**2

bmi = wieght/sequer_height
if bmi >=25:
    print ("You are overwieght you need to work out more and watch your diet.")
    
elif bmi >=18.5:
    print("You are fit & healthy")
elif bmi <18.5:
    print ("You are underweight. Watch your health")


