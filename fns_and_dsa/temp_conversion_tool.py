FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    '''This converts fahrenheit to celsius'''
    celsius = (fahrenheit - 32)*CELSIUS_TO_FAHRENHEIT_FACTOR
    return celsius

def  convert_to_fahrenheit(celsius):
    '''This converts celcius to fahrenheit'''
    
    fahrenheit = (celsius*FAHRENHEIT_TO_CELSIUS_FACTOR)-32
    return fahrenheit

temp_input = input("Enter the temperature to convert: ")
type1 = input("Is this temperature in Celsius or Fahrenheit? (C/F):")
try:
    temperature = float(temp_input)
except ValueError:
    print("Invalid temperature. Please enter a numeric value.")
    exit()

if type1.upper() == 'C':
    result = convert_to_fahrenheit(temperature)
    print(f"{temperature}°C is {result}°F")
elif type1.upper() == 'F':
    result = convert_to_fahrenheit(temperature)
    print(f"{temperature}°F is {result}°C")