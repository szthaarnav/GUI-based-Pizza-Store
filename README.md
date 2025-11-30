# 🍕 Python GUI Pizza Store Application

This project is a standalone **desktop Graphical User Interface (GUI) application** that simulates a pizza ordering system. It is built entirely in **Python 3** using the built-in **tkinter** library.

The application runs completely **offline** on a local machine and does not require an internet connection to function. It serves as a practical demonstration of building interactive, single-window desktop applications using fundamental Python programming concepts.

## ✨ Key Features (Functional)

The application simulates a complete ordering flow within a single desktop window, featuring the following operational elements:

* **Menu and Item Display:** Pizzas are displayed using clickable image buttons.
* **Item Detail View:** Clicking a pizza button loads its details, allowing the user to select a quantity using a spinbox.
* **Cart Management:** Items are successfully added to a dynamic order list with line totals.
* **Receipt Feature:** Automatically calculates and displays the final grand total upon order confirmation.
* **User Order Control:** Includes clear buttons for 'Show Pizzas', 'Add to Cart', 'Cancel Order', and 'Confirm Order'.
* **Core Technology:** Purely functional implementation using basic Python commands and core `tkinter` widgets (`Frame`, `Button`, `Label`, `Spinbox`, etc.).

## 🛠️ Technology Used

* **Type:** Offline Desktop Application
* **Language:** Python 3
* **GUI Library:** `tkinter` (Standard Python library)

## 🚧 Future Scope & Work In Progress

* **Menu Editing:** The **'Add New'** and **'Delete'** buttons are currently non-functional placeholders. They are intended for a future update where the user (or administrator) can dynamically edit the list of available pizzas and their details.

## 🚀 How to Run

To get the application running on your local machine, follow these steps:

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/szthaarnav/GUI-based-Pizza-Store
    ```
2.  **Navigate to the project directory:**
    ```bash
    cd "Pizza Store GUI"
    ```
3.  **Ensure all required image and data files** (e.g., pizza images) are present in the project directory.
4.  **Run the main script:**
    ```bash
    python main.py
    ```
