# this is a Farenheit degree calculator

temperature_celsius = float(input("indica la temperatura en grados celsius: "))

temperature_farenheit = (temperature_celsius * 9/5) + 32

print(temperature_farenheit)

temperature_kelvin = float(input("indica la temperatura en grados kelvin: "))

temperature_farenheit = (temperature_kelvin - 273.15) * 9/5 + 32

print(temperature_farenheit)