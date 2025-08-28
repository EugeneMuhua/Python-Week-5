# OOP Assignments 🚀

This repository contains simple Python programs to practice **Object-Oriented Programming (OOP)** concepts such as **classes, constructors, inheritance, encapsulation, and polymorphism**.

---

## 📱 Assignment 1: Design Your Own Class

We created a `Smartphone` class with attributes and methods.  
Then, we extended it into a `GamingSmartphone` class to demonstrate **inheritance** and **polymorphism**.

### Features:

- `phone_info()` → Displays phone details.  
- `charge(amount)` → Adds to battery capacity.  
- `install_app(app_size)` → Installs an app if there’s enough storage.  
- `play_game(game_size, battery_usage)` → (Gaming phone only) plays a game by reducing storage & battery.  

👉 Concepts used: **class, constructor (`__init__`), inheritance, method overriding, encapsulation**.

---

## 🚗 Assignment 2: Vehicles with Polymorphism

We implemented multiple vehicle classes (`Car`, `Plane`, `Bicycle`, `Boat`) that all define a `move()` method differently.

### Example:

- `Car.move()` → "Roadtripping in the car"  
- `Plane.move()` → "Enjoying the birds flying"  
- `Bicycle.move()` → "Riding on the bike lane"  
- `Boat.move()` → "Sailing along the mulky waters"  

👉 This shows **polymorphism**: the same method name (`move()`) produces different behaviors depending on the class.

---

## 🎯 Key Takeaways

- **Encapsulation** → Managing attributes via methods.  
- **Inheritance** → `GamingSmartphone` extends `Smartphone`.  
- **Polymorphism** → `move()` behaves differently across `Car`, `Plane`, etc.  
- **Reusability** → Classes make it easier to expand and manage code.  

---

## ▶️ How to Run

1. Clone the repo or copy the files.  
2. Run the scripts in Python:
   
   ```bash
   python Smartphone.py
   python Polymorphism.py
   ```
