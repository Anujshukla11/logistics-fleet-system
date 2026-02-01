# Logistics Fleet Management System 🚛 🚁

A modular delivery simulation engine built with Python, demonstrating core Object-Oriented Programming (OOP) principles.

## 🚀 Features
* **Polymorphic Vehicle Behavior:** distinct logic for `Trucks` (high capacity) vs. `Drones` (weight constraints).
* **Memory Efficiency:** Uses **Python Generators (`yield`)** to dispatch fleets without loading all objects into memory at once.
* **Scalable Architecture:** Designed with inheritance to easily add new vehicle types (e.g., Ships, Bikes) without breaking existing logic.

## 🛠️ Concepts Applied
* **Inheritance:** Base `Vehicle` class extended by specialized subclasses.
* **Encapsulation:** Managing vehicle state (cargo, capacity) internally.
* **Generators:** Optimized iteration for dispatch systems.

## 💻 How to Run
```bash
python main.py
