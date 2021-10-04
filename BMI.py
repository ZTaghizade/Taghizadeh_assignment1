h=float(input('Please enter your height(m): '))
w=float(input('Please enter your weight(Kg): '))
bmi=w/(h*h)
print('BMI: ',bmi)
if(bmi<18.5):
    print('UNDERWEIGHT')
elif (bmi<=24.9 and bmi>=18.5):
    print('NORMAL')
elif(bmi<=29.9 and bmi>=25):
    print('OVERWEIGHT')
elif(bmi<=34.9 and bmi>=30):
    print('OBESE')
else:
    print('EXTREMLY OBESE')
        