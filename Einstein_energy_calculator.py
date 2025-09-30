#this is a Einstein energy calculator

mass = float(input("indica la masa en kg: "))
speed_of_light = 3 * 10**8 #m/s

energy = mass * speed_of_light ** 2

message = f"la energía es de {energy} julios"

print(message)