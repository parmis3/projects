#Question 1
weight = float(input("Enter Weight:"))
height = float(input("Enter height:"))
bmi= weight / (height**2)
if bmi<18.5:
    print("underwright")
elif 18.5<bmi<25:
    print("normal")
elif 25<bmi<30:
    print("overweight")
else:
    print("obesity")



