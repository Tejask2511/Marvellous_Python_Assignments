# celsius to ferenite converter
# Accept temperature in clesius and conver it into ferenhite using the formula
# F = ( c * 9/5 ) + 32 
# Expected output:
# Enter temperature in celsius:25 
# Expected Output:
# Temperature in ferenite is:77.0f

def main():
    Celsius=int(input("Enter the temperature in celsius"))
    Fahrenheit=(Celsius * 9/5) + 32
    print("the Temperature in faherenheit:",Fahrenheit)
    

if __name__=="__main__":
    main()