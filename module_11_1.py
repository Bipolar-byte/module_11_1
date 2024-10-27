import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = {
    "Day": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"],
    "Temperature": [20, 21, 22, 20, 19, 18, 21]
}
df = pd.DataFrame(data)

temperatures = np.array(df["Temperature"])

mean_temperature = np.mean(temperatures)
max_temperature = np.max(temperatures)
min_temperature = np.min(temperatures)
std_dev = np.std(temperatures)

random_increase = np.random.uniform(0, 3, size=temperatures.shape)
increased_temperatures = temperatures + random_increase

df["Increased Temperature"] = increased_temperatures

print(f"Средняя температура: {mean_temperature:.1f}°C")
print(f"Максимальная температура: {max_temperature}°C")
print(f"Минимальная температура: {min_temperature}°C")
print(f"Среднеквадратичное отклонение температур: {std_dev:.2f}°C")
print(f"Случайные увеличения температур: {random_increase.round(1)}")
print(f"Увеличенные, Температуры : {increased_temperatures.round(1)}")

plt.figure(figsize=(10, 6))
plt.plot(df["Day"], df["Temperature"], marker='o', color='b', label="Temperature (°C)")
plt.plot(df["Day"], df["Increased Temperature"], marker='o', color='c', linestyle='--',
         label="Increased Temperature (°C)")

plt.axhline(mean_temperature, color='g', linestyle='--', label=f"Mean Temperature ({mean_temperature:.1f}°C)")
plt.axhline(max_temperature, color='r', linestyle='--', label=f"Max Temperature ({max_temperature}°C)")
plt.axhline(min_temperature, color='orange', linestyle='--', label=f"Min Temperature ({min_temperature}°C)")

plt.xlabel("Day of the Week", fontsize=12, color="darkblue")
plt.ylabel("Temperature (°C)", fontsize=12, color="darkblue")
plt.title("Temperature Trends Over the Week", fontsize=14, color="darkgreen")
plt.legend()
plt.grid(True)

plt.savefig("temperature_trends.png")

plt.show()
