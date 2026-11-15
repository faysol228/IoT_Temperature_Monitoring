import random
import csv
import matplotlib.pyplot as plt


temperatures = []

for i in range(50):
    temperature = round(random.uniform(20, 40), 2)
    temperatures.append(temperature)


with open("temperature_readings.csv", "w", newline="") as file:
    writer = csv.writer(file)

    writer.writerow(["Reading", "Temperature"])

    for i, temp in enumerate(temperatures, start=1):
        writer.writerow([i, temp])

    # Add sample missing and invalid data for testing
    writer.writerow([51, ""])
    writer.writerow([52, "invalid"])


print("Temperature readings saved successfully!")



valid_temperatures = []

with open("temperature_readings.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        try:
            temp = float(row["Temperature"])

            if 0 <= temp <= 100:
                valid_temperatures.append(temp)

                # STEP 4: Check for high temperatures
                if temp > 35:
                    print(
                        f"WARNING! High temperature detected: {temp}°C"
                    )

            else:
                print("Invalid temperature detected:", row["Temperature"])

        except (ValueError, TypeError):
            print("Missing or invalid temperature data detected.")



if valid_temperatures:

    average = sum(valid_temperatures) / len(valid_temperatures)

    print("\nTemperature Monitoring Results")
    print("--------------------------------")
    print("Total valid readings:", len(valid_temperatures))
    print("Average temperature:", round(average, 2), "°C")

else:
    print("No valid temperature readings available.")



if valid_temperatures:

    plt.figure(figsize=(10, 5))

    plt.plot(
        range(1, len(valid_temperatures) + 1),
        valid_temperatures,
        marker="o"
    )

    plt.axhline(
        y=35,
        linestyle="--",
        label="Warning Limit (35°C)"
    )

    plt.title("IoT Temperature Monitoring System")
    plt.xlabel("Reading Number")
    plt.ylabel("Temperature (°C)")

    plt.legend()
    plt.grid(True)

    plt.savefig("temperature_graph.png")

    plt.show()

    print("\nTemperature graph created successfully!")