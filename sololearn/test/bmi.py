weight = float(input('Enter your weight:'))
height = float(input('Enter your height:'))
ibm = weight / (height*height)
if ibm <= 18.5:
    print('Underweight')
elif ibm > 18.5 and ibm < 25:
    print('Normal')
elif ibm > 25 and ibm < 30:
    print('Overweight')
elif ibm > 30:
    print('Obesity')
