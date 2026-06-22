#This page deals with farmer/user registration

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from modules.dashboard import dashboard_window

#creates a function that validates user before given access to the inventory
def register_farmer():

    if first_name_entry.get() == "":
        messagebox.showerror(
            "Error",
            "Enter First Name"
        )
        return

    if last_name_entry.get() == "":
        messagebox.showerror(
            "Error",
            "Enter Last Name"
        )
        return

    if age_combo.get() == "":
        messagebox.showerror(
            "Error",
            "Select Age"
        )
        return

    if district_combo.get() == "":
        messagebox.showerror(
            "Error",
            "Select District"
        )
        return

    if gender_var.get() == "":
        messagebox.showerror(
            "Error",
            "Select Gender"
        )
        return
    first_name = first_name_entry.get(),
    last_name = last_name_entry.get()

    root.destroy()

    dashboard_window(
        first_name,
        last_name
    )

#creates the widgets for the entire registration page
def registration_window():

    global root
    global first_name_entry
    global last_name_entry
    global age_combo
    global district_combo
    global gender_var

    root = tk.Tk()
    root.title("Farmer Registration System")
    root.geometry("700x500")
    root.configure(bg="#f4f6f9")

    title = tk.Label(
        root,
        text="Farmer Registration Form",
        font=("Arial", 20, "bold"),
        bg="#f4f6f9"
    )

    title.pack(pady=20)

    form_frame = tk.Frame(
        root,
        bg="white",
        bd=2,
        relief="solid"
    )

    form_frame.pack(
        padx=20,
        pady=20
    )

    # First Name

    tk.Label(
        form_frame,
        text="First Name",
        bg="white"
    ).grid(row=0, column=0, padx=10, pady=10)

    first_name_entry = tk.Entry(
        form_frame,
        width=30
    )

    first_name_entry.grid(
        row=0,
        column=1
    )

    # Last Name

    tk.Label(
        form_frame,
        text="Last Name",
        bg="white"
    ).grid(row=1, column=0, padx=10, pady=10)

    last_name_entry = tk.Entry(
        form_frame,
        width=30
    )

    last_name_entry.grid(
        row=1,
        column=1
    )

    # Age

    tk.Label(
        form_frame,
        text="Age",
        bg="white"
    ).grid(row=2, column=0, padx=10, pady=10)

    age_combo = ttk.Combobox(
        form_frame,
        values=list(range(18, 100)),
        state="readonly",
        width=27
    )

    age_combo.grid(
        row=2,
        column=1
    )

    # District

    districts = [
        "Bo",
        "Bombali",
        "Falaba",
        "Kailahun",
        "Kambia",
        "Karene",
        "Kenema",
        "Koinadugu",
        "Kono",
        "Moyamba",
        "Port Loko",
        "Pujehun",
        "Tonkolili",
        "Western Area Rural",
        "Western Area Urban",
        "Bonthe"
    ]

    tk.Label(
        form_frame,
        text="District",
        bg="white"
    ).grid(row=3, column=0, padx=10, pady=10)

    district_combo = ttk.Combobox(
        form_frame,
        values=districts,
        state="readonly",
        width=27
    )

    district_combo.grid(
        row=3,
        column=1
    )

    # Gender

    tk.Label(
        form_frame,
        text="Gender",
        bg="white"
    ).grid(row=4, column=0, padx=10, pady=10)

    gender_var = tk.StringVar()

    tk.Radiobutton(
        form_frame,
        text="Male",
        variable=gender_var,
        value="Male",
        bg="white"
    ).grid(
        row=4,
        column=1,
        sticky="w"
    )

    tk.Radiobutton(
        form_frame,
        text="Female",
        variable=gender_var,
        value="Female",
        bg="white"
    ).grid(
        row=4,
        column=1,
        padx=80,
        sticky="w"
    )

    register_btn = tk.Button(
        root,
        text="Register",
        bg="#2d89ef",
        fg="white",
        font=("Arial", 12, "bold"),
        width=20,
        command=register_farmer
    )

    register_btn.pack(pady=20)

    root.mainloop()