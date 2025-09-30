#this is a kinetic energy calculator

mass = float(input("indica la masa en kg: "))

velocity = float(input("indica la velocidad en m/s: "))

kinetic_energy = (0.5 * mass * velocity ** 2)

message = f"la energia cinetica es de {kinetic_energy} julios: "

print(message)