
weight = float(input("Enter Weight:"))
height = float(input("Enter height:"))
bmi = weight / (height ** 2)
bmi = 18
if bmi < 18:
    print("under weight")

elif bmi < 25:
    print("Normal")

else:
    print("Overweight")
