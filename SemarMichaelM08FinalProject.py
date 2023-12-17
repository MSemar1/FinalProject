"""
Author: Michael Semar
Date: 12/5/2023
Description: PC Playground - This application checks for compatibility while the user builds their computer.
"""

import tkinter as tk
from tkinter import ttk
from components_database import components_database, component_specs

class PCPlayground:
    def __init__(self, root):
        """
        Initializes the PCPlayground class.

        Parameters:
        - root (tk.Tk): The root Tkinter window.
        """
        self.root = root
        self.root.title("PC Playground")

        # Variables to store selected components
        self.selected_cpu = tk.StringVar()
        self.selected_cpucooler = tk.StringVar()
        self.selected_case = tk.StringVar()
        self.selected_powersupply = tk.StringVar()
        self.selected_gpu = tk.StringVar()
        self.selected_ram = tk.StringVar()
        self.selected_storage = tk.StringVar()
        self.selected_motherboard = tk.StringVar()

        # Populate dropdowns using components_database
        self.create_dropdown("CPU", components_database["CPU"], self.selected_cpu)
        self.create_dropdown("GPU", components_database["GPU"], self.selected_gpu)
        self.create_dropdown("RAM", components_database["RAM"], self.selected_ram)
        self.create_dropdown("Storage", components_database["Storage"], self.selected_storage)
        self.create_dropdown("cpucooler", components_database["cpucooler"], self.selected_cpucooler)
        self.create_dropdown("case", components_database["case"], self.selected_case)
        self.create_dropdown("powersupply", components_database["powersupply"], self.selected_powersupply)
        self.create_dropdown("motherboard", components_database["motherboard"], self.selected_motherboard)

        # Button to check compatibility
        check_button = ttk.Button(root, text="Check Compatibility", command=self.check_compatibility)
        check_button.pack(pady=10)

        # Exit button
        exit_button = ttk.Button(root, text="Exit", command=self.exit_application)
        exit_button.pack(pady=10)

    def create_dropdown(self, label, options, variable):
        """
        Creates a dropdown menu with a label and specified options.

        Parameters:
        - label (str): The label for the dropdown.
        - options (list): The options for the dropdown menu.
        - variable (tk.StringVar): The variable to store the selected option.
        """
        frame = ttk.Frame(self.root)
        frame.pack(pady=10)
        ttk.Label(frame, text=label).pack(side="left")
        dropdown = ttk.Combobox(frame, values=options, textvariable=variable)
        dropdown.pack(side="left")

    def check_compatibility(self):
        """
        Checks compatibility based on the selected components and their specifications.
        Displays the compatibility result in a label.
        """
        # Get selected components
        cpu = self.selected_cpu.get()
        gpu = self.selected_gpu.get()
        ram = self.selected_ram.get()
        storage = self.selected_storage.get()
        cpucooler = self.selected_cpucooler.get()
        case = self.selected_case.get()
        powersupply = self.selected_powersupply.get()
        motherboard = self.selected_motherboard.get()

        # Check input validation
        if not all((cpu, gpu, ram, storage, cpucooler, case, powersupply, motherboard)):
            self.display_error("Please select all components.")
            return

        # Check compatibility based on component specifications
        cpu_specs = component_specs.get(cpu, {})
        gpu_specs = component_specs.get(gpu, {})
        motherboard_specs = component_specs.get(motherboard, {})
        powersupply_specs = component_specs.get(powersupply, {})

        # Check CPU and motherboard socket compatibility
        cpu_socket = cpu_specs.get("socket")
        motherboard_socket = motherboard_specs.get("socket")
        if cpu_socket and motherboard_socket and cpu_socket != motherboard_socket:
            compatibility_result = "Compatibility Check: Not Compatible - Motherboard and CPU socket mismatch"
        else:
            # Check power supply wattage
            total_wattage = cpu_specs.get("wattage", 0) + gpu_specs.get("wattage", 0)
            if total_wattage > powersupply_specs.get("wattage", 0):
                compatibility_result = "Compatibility Check: Not Compatible - Insufficient Power Supply"
            else:
                compatibility_result = "Compatibility Check: Compatible"

        result_label = ttk.Label(self.root, text=compatibility_result)
        result_label.pack(pady=10)

    def exit_application(self):
        """Callback function to exit the application."""
        self.root.destroy()

    def display_error(self, message):
        """
        Displays an error message in a pop-up window.

        Parameters:
        - message (str): The error message to be displayed.
        """
        error_popup = tk.Toplevel(self.root)
        error_popup.title("Error")
        ttk.Label(error_popup, text=message).pack(padx=10, pady=10)
        ok_button = ttk.Button(error_popup, text="OK", command=error_popup.destroy)
        ok_button.pack(pady=10)

if __name__ == "__main__":
    root = tk.Tk()
    app = PCPlayground(root)
    root.mainloop()
