def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9


user_input = float(input("Enter temperature in Celsius: "))

converted_fahrenheit = celsius_to_fahrenheit(user_input)

print(f"{user_input:.2f}°C is equivalent to {converted_fahrenheit:.2f}°F")

