#Question 2
question= input("Aya Metric hast?")
if question=="bale":
    weight = float(input("weight?:"))
    height= float(input("height?:"))
    bmi = weight / (height * height)
    print(bmi)
    if bmi < 18.5: print("underweight")

    if 18.5 < bmi < 25: print("normal")

    if 25 < bmi < 30: print("overwight")

    if bmi > 30: print("obesity")
    elif question == "kheir":
        weight = float(input("weight ?:"))
        height = float(input("height ?:"))
        bmi = (weight * 703) / (height * height)
        print(bmi)

        if bmi < 18.5: print("underweight")

        if 18.5 < bmi < 25: print("normal")

        if 25 < bmi < 30: print("overwight")

        if bmi > 30: print("obesity")