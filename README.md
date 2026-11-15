Python-Based IoT Temperature Monitoring System

* Course Code: LENS-COS 324
* Course Title: Internet of Things (IoT)
* Project Topic: Python-Based IoT Temperature Monitoring System
* Student Name:Bouraima Faysol Adeshina 
* Matriculation Number:252007CYB007

1. Introduction

This project involves developing a simple Internet of Things (IoT) Temperature Monitoring System using Python.

The system simulates temperature readings without requiring physical IoT devices or sensors. It collects temperature readings, stores them in a CSV file, analyses the data, calculates the average temperature, and displays a graph using Matplotlib.

2. Project Objectives

The objectives of this project are to:

* Generate at least 50 simulated temperature readings.
* Store temperature readings in a CSV file.
* Read and analyse temperature data using Python.
* Calculate and display the average temperature.
* Identify and handle missing or invalid data.
* Generate a temperature graph using Matplotlib.
* Display a warning when the temperature exceeds 35°C.

3. Technologies Used

* Python: For programming and data processing.
* CSV: For storing temperature readings.
* Matplotlib: For creating temperature graphs.
* Random Module: For generating simulated temperature readings.

4. Project Files

The project contains the following files:

* main.py – Contains the Python source code.
* temperature_readings.csv – Stores the generated temperature readings.
* temperature_graph.png – Displays the temperature monitoring graph.
* README.md – Provides information about the project.

5. How the System Works

1. The program generates 50 random temperature readings.
2. The readings are saved in a CSV file.
3. Python reads the stored temperature data.
4. Missing and invalid data are identified and handled.
5. The program calculates the average temperature.
6. A warning is displayed when a temperature exceeds 35°C.
7. Matplotlib generates a graph showing the temperature readings.

6. Installation Requirements

Install Python on your computer.

Install Matplotlib using the following command:

pip install matplotlib

7. How to Run the Program

Open your terminal and navigate to the project folder.

Run the program using:

python main.py

If necessary, use:

python3 main.py

8. Expected Output

When the program runs successfully, it:

* Generates 50 simulated temperature readings.
* Saves the readings in a CSV file.
* Displays the average temperature.
* Identifies missing or invalid readings.
* Displays warnings for temperatures above 35°C.
* Generates and displays a temperature graph.

9. Conclusion

This project demonstrates how Python can be used to simulate a basic IoT temperature monitoring system.

It shows how temperature data can be generated, stored, processed, analysed, and visualised. The project also demonstrates how temperature warnings can help identify unusually high temperatures.

Although physical sensors are not used, the simulation represents the basic operations of a real IoT temperature monitoring system.