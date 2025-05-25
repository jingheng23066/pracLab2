def calculate_bmi(height, weight):
    print("Height = " + str(height))
    print("Weight = " + str(weight))

    bmi = weight/(height*height)
    print("BMI = " +str(bmi))

    if(bmi < 18.5):
        print("Under weight")
        return -1
    elif(bmi >18.5 and bmi <= 25.0):
        print("Normal Weight")
        return 0
    elif(bmi > 25.0):
        print("Overweight")
        return 1