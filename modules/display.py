#This module displays record taken from the farmer without access to modify

import tkinter as tk
from tkinter import ttk

from modules.inventory import records


def display_page(content_frame):

    # Clear current page
    for widget in content_frame.winfo_children():
        widget.destroy()

    # ================= TITLE =================

    title = tk.Label(
        content_frame,
        text="Display Records",
        font=("Arial", 18, "bold"),
        bg="white"
    )

    title.pack(pady=10)

    # ================= TREEVIEW =================

    columns = (
        "Record ID",
        "Crop Name",
        "Date Harvested",
        "Amount Harvested",
        "Profit",
        "Loss"
    )

    tree = ttk.Treeview(
        content_frame,
        columns=columns,
        show="headings",
        height=15
    )

    for col in columns:

        tree.heading(col, text=col)

        tree.column(
            col,
            width=150,
            anchor="center"
        )

    tree.pack(
        fill="both",
        expand=True,
        padx=20,
        pady=20
    )

    # ================= SCROLLBAR =================

    scrollbar = ttk.Scrollbar(
        content_frame,
        orient="vertical",
        command=tree.yview
    )

    tree.configure(
        yscrollcommand=scrollbar.set
    )

    scrollbar.pack(
        side="right",
        fill="y"
    )

    # ================= DISPLAY RECORDS =================

    for record in records:

        tree.insert(
            "",
            "end",
            values=(
                record[0],   # Record ID
                record[1],   # Crop Name
                record[3],   # Date Harvested
                record[4],   # Amount Harvested
                record[9],   # Profit
                record[10]   # Loss
            )
        )

    # ================= NOTE =================

    note = tk.Label(
        content_frame,
        text="Read Only Page - Records cannot be edited here.",
        bg="white",
        fg="gray",
        font=("Arial", 10, "italic")
    )

    note.pack(pady=5)