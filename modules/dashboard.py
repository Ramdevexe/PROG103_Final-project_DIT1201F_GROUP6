#dashboard

import tkinter as tk
from modules.inventory import inventory_page
from modules.display import display_page


def show_home(content_frame, first_name, last_name):

    # Clear content area
    for widget in content_frame.winfo_children():
        widget.destroy()

    welcome_label = tk.Label(
        content_frame,
        text=f"Welcome {first_name} {last_name}",
        font=("Arial", 20, "bold"),
        bg="white"
    )

    welcome_label.pack(pady=20)

    info_label = tk.Label(
        content_frame,
        text="",
        font=("Arial", 12),
        bg="white",
        justify="left"
    )

    info_label.pack(pady=20)


def dashboard_window(first_name, last_name):

    root = tk.Tk()
    root.title("Farmer Inventory Management System")
    root.geometry("1200x700")
    root.configure(bg="white")

    # ================= SIDEBAR =================

    sidebar = tk.Frame(
        root,
        bg="#1e3a5f",
        width=220
    )

    sidebar.pack(
        side="left",
        fill="y"
    )

    sidebar.pack_propagate(False)

    # ================= CONTENT FRAME =================

    content_frame = tk.Frame(
        root,
        bg="white"
    )

    content_frame.pack(
        side="right",
        fill="both",
        expand=True
    )

    # ================= MENU TITLE =================

    menu_title = tk.Label(
        sidebar,
        text="MENU",
        font=("Arial", 18, "bold"),
        fg="white",
        bg="#1e3a5f"
    )

    menu_title.pack(pady=20)

    # ================= HOME BUTTON =================

    home_btn = tk.Button(
        sidebar,
        text="Home",
        width=18,
        height=2,
        command=lambda: show_home(
            content_frame,
            first_name,
            last_name
        )
    )

    home_btn.pack(pady=10)

    # ================= INVENTORY BUTTON =================

    inventory_btn = tk.Button(
        sidebar,
        text="Inventory",
        width=18,
        height=2,
        command=lambda: inventory_page(
            content_frame
        )
    )

    inventory_btn.pack(pady=10)

    # ================= DISPLAY BUTTON =================

    display_btn = tk.Button(
        sidebar,
        text="Display",
        width=18,
        height=2,
        command=lambda: display_page(
            content_frame
        )
    )

    display_btn.pack(pady=10)

    # ================= EXIT BUTTON =================

    exit_btn = tk.Button(
        sidebar,
        text="Exit",
        width=18,
        height=2,
        bg="red",
        fg="white",
        command=root.destroy
    )

    exit_btn.pack(pady=10)

    # Show Home page first

    show_home(
        content_frame,
        first_name,
        last_name
    )

    root.mainloop()