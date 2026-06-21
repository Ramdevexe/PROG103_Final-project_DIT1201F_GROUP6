#this module deals with the inventory page  where farmers/users input information for storing

import tkinter as tk
from tkinter import ttk, messagebox

# Stores all inventory records
records = []


def inventory_page(content_frame):

    # Clear page
    for widget in content_frame.winfo_children():
        widget.destroy()

    # ================= TITLE =================

    title = tk.Label(
        content_frame,
        text="Inventory Management",
        font=("Arial", 18, "bold"),
        bg="white"
    )

    title.pack(pady=10)

    # ================= FORM FRAME =================

    form_frame = tk.Frame(
        content_frame,
        bg="white"
    )

    form_frame.pack(
        fill="x",
        padx=10,
        pady=10
    )

    # ================= VARIABLES =================

    record_id_var = tk.StringVar()
    crop_var = tk.StringVar()
    planted_var = tk.StringVar()
    harvested_var = tk.StringVar()
    amount_var = tk.StringVar()
    spoiled_var = tk.StringVar()
    unit_var = tk.StringVar()
    cost_var = tk.StringVar()
    selling_var = tk.StringVar()

    # ================= COMBOBOX VALUES =================

    crops = [
        "Rice",
        "Cassava",
        "Maize",
        "Groundnut",
        "Cocoa",
        "Coffee",
        "Palm Oil",
        "Pepper",
        "Tomato",
        "Okra"
    ]

    units = [
        "Kg",
        "Bag",
        "Ton",
        "Basket",
        "Litre"
    ]

    # ================= ROW 1 =================

    tk.Label(
        form_frame,
        text="Record ID",
        bg="white"
    ).grid(row=0, column=0, padx=5, pady=5)

    record_id_entry = tk.Entry(
        form_frame,
        textvariable=record_id_var
    )

    record_id_entry.grid(row=0, column=1)

    tk.Label(
        form_frame,
        text="Crop Name",
        bg="white"
    ).grid(row=0, column=2)

    crop_combo = ttk.Combobox(
        form_frame,
        values=crops,
        state="readonly",
        textvariable=crop_var
    )

    crop_combo.grid(row=0, column=3)

    tk.Label(
        form_frame,
        text="Date Planted",
        bg="white"
    ).grid(row=0, column=4)

    planted_entry = tk.Entry(
        form_frame,
        textvariable=planted_var
    )

    planted_entry.grid(row=0, column=5)

    # ================= ROW 2 =================

    tk.Label(
        form_frame,
        text="Date Harvested",
        bg="white"
    ).grid(row=1, column=0)

    harvested_entry = tk.Entry(
        form_frame,
        textvariable=harvested_var
    )

    harvested_entry.grid(row=1, column=1)

    tk.Label(
        form_frame,
        text="Amount Harvested",
        bg="white"
    ).grid(row=1, column=2)

    amount_entry = tk.Entry(
        form_frame,
        textvariable=amount_var
    )

    amount_entry.grid(row=1, column=3)

    tk.Label(
        form_frame,
        text="Amount Spoiled",
        bg="white"
    ).grid(row=1, column=4)

    spoiled_entry = tk.Entry(
        form_frame,
        textvariable=spoiled_var
    )

    spoiled_entry.grid(row=1, column=5)

    # ================= ROW 3 =================

    tk.Label(
        form_frame,
        text="Unit",
        bg="white"
    ).grid(row=2, column=0)

    unit_combo = ttk.Combobox(
        form_frame,
        values=units,
        state="readonly",
        textvariable=unit_var
    )

    unit_combo.grid(row=2, column=1)

    tk.Label(
        form_frame,
        text="Production Cost",
        bg="white"
    ).grid(row=2, column=2)

    cost_entry = tk.Entry(
        form_frame,
        textvariable=cost_var
    )

    cost_entry.grid(row=2, column=3)

    tk.Label(
        form_frame,
        text="Selling Price",
        bg="white"
    ).grid(row=2, column=4)

    selling_entry = tk.Entry(
        form_frame,
        textvariable=selling_var
    )

    selling_entry.grid(row=2, column=5)

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
        height=12
    )

    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, width=140)

    tree.pack(
        fill="both",
        expand=True,
        padx=10,
        pady=10
    )

    # Scrollbar

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

    # ================= FUNCTIONS =================

    def clear_fields():

        record_id_var.set("")
        crop_var.set("")
        planted_var.set("")
        harvested_var.set("")
        amount_var.set("")
        spoiled_var.set("")
        unit_var.set("")
        cost_var.set("")
        selling_var.set("")

    def add_record():

        if record_id_var.get() == "":
            messagebox.showerror(
                "Error",
                "Enter Record ID"
            )
            return

        if crop_var.get() == "":
            messagebox.showerror(
                "Error",
                "Select Crop Name"
            )
            return

        try:
            harvested_amount = float(amount_var.get())
            spoiled_amount = float(spoiled_var.get())
            cost = float(cost_var.get())
            selling = float(selling_var.get())

        except ValueError:

            messagebox.showerror(
                "Error",
                "Enter valid numbers"
            )
            return

        if spoiled_amount > harvested_amount:

            messagebox.showerror(
                "Error",
                "Spoiled amount cannot exceed harvested amount"
            )
            return

        profit = selling - cost
        loss = spoiled_amount * 100

        data = [
            record_id_var.get(),
            crop_var.get(),
            planted_var.get(),
            harvested_var.get(),
            harvested_amount,
            spoiled_amount,
            unit_var.get(),
            cost,
            selling,
            profit,
            loss
        ]

        records.append(data)

        tree.insert(
            "",
            "end",
            values=(
                record_id_var.get(),
                crop_var.get(),
                harvested_var.get(),
                harvested_amount,
                profit,
                loss
            )
        )

        clear_fields()

    def delete_record():

        selected = tree.selection()

        if not selected:

            messagebox.showerror(
                "Error",
                "Select a record"
            )
            return

        answer = messagebox.askyesno(
            "Delete",
            "Delete selected record?"
        )

        if answer:

            item_index = tree.index(selected[0])

            tree.delete(selected[0])

            if item_index < len(records):
                records.pop(item_index)

    def update_record():

        selected = tree.selection()

        if not selected:

            messagebox.showerror(
                "Error",
                "Select a record"
            )
            return

        answer = messagebox.askyesno(
            "Update",
            "Update selected record?"
        )

        if answer:

            cost = float(cost_var.get())
            selling = float(selling_var.get())

            profit = selling - cost
            loss = float(spoiled_var.get()) * 100

            tree.item(
                selected[0],
                values=(
                    record_id_var.get(),
                    crop_var.get(),
                    harvested_var.get(),
                    amount_var.get(),
                    profit,
                    loss
                )
            )

    def show_selected(_event):

        selected = tree.selection()

        if not selected:
            return

        values = tree.item(
            selected[0],
            "values"
        )

        record_id_var.set(values[0])
        crop_var.set(values[1])
        harvested_var.set(values[2])
        amount_var.set(values[3])

    tree.bind(
        "<<TreeviewSelect>>",
        show_selected
    )

    # ================= BUTTONS =================

    button_frame = tk.Frame(
        content_frame,
        bg="white"
    )

    button_frame.pack(pady=10)

    tk.Button(
        button_frame,
        text="Add Record",
        bg="green",
        fg="white",
        command=add_record
    ).grid(row=0, column=0, padx=5)

    tk.Button(
        button_frame,
        text="Update",
        bg="orange",
        fg="white",
        command=update_record
    ).grid(row=0, column=1, padx=5)

    tk.Button(
        button_frame,
        text="Delete",
        bg="red",
        fg="white",
        command=delete_record
    ).grid(row=0, column=2, padx=5)

    tk.Button(
        button_frame,
        text="Clear",
        command=clear_fields
    ).grid(row=0, column=3, padx=5)