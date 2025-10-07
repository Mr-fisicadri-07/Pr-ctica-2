# this is an object that calculates the motion of objects in a 2D space

# calcular posición (x), velocidad (v) y aceleración (a)

position_x = float(input("indica la posición en x (metros): "))

velocity_x = float(input("indica la velocidad en x (m/s): "))

aceleration_x = float(input("indica la aceleración en x (m/s²): "))

time = float(input("indica el tiempo (s): "))

position_x_end = position_x + velocity_x*time + (0.5 * aceleration_x*time**2)

velocity_x_end = velocity_x + aceleration_x*time

output_x = f"La posición en x es de {position_x_end} metros y la velocidad en x es de {velocity_x_end} m/s"

print(output_x)
