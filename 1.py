a = 10
b = 20
c = 30
d = 40
num = 31

test =(a < num < b) or (c < num < d)
print(test)

#----------
weight = 60
height = 180
BMI = weight / (height * height)
if  BMI < 18 :
    print("under weight")


if  18 < BMI < 25 :
        print("Normal")
if BMI>25 :
    print("Overweight")
