import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation

# Define the parameters of your simulation
plant_type = "Snake Plant"
oxygen_production_rate = 10
simulation_hours = 24

# Create the figure and the lines
fig = plt.figure()
line, = plt.plot([], [], label=plant_type)
plt.xlabel("Hour")
plt.ylabel("Oxygen Production (units)")
plt.title("Oxygen Production Over Time")
plt.legend()

# Define the function to update the graph
def update(frame):
    hour = frame + 1
    line.set_data(np.arange(1, hour + 1), oxygen_production[:hour])
    return line,

# Generate the oxygen production data
oxygen_production = np.arange(oxygen_production_rate * (simulation_hours + 1))

# Create the animated graph
ani = animation.FuncAnimation(fig, update, frames=simulation_hours, interval=1000)

# Save the animation as an animated GIF
ani.save("oxygen_production.gif", writer='imagemagick', fps=1)

# Show the graph
plt.show()