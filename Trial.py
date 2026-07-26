h = float(input("Enter your height in centimeters :- "))/100
w = float(input("Enter your weight in kilograms :- "))
BMI = w/h**2
print (BMI)
if BMI >= 30 :
    print ("You are categorised as medically obese.")
elif BMI >= 25 :
    print ("You are categorised as medically overweight.")
elif BMI >= 18.5 :
    print ("You are categorised as a healthy person.")
else :
    print ("You are categorised as medically underweight.")