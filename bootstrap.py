import importlib.util
import subprocess
import sys
from pathlib import Path
from tkinter import messagebox, Tk

RAW_DATA_FILE = Path("raw_data_map.py")
GENERATOR_FILE = Path("generator.py")

def ensure_raw_data_map():
    """
    Ensures raw_data_map.py exists.
    If not, runs generator.py to create it.
    Returns the imported raw_data_map dict.
    """
    if not RAW_DATA_FILE.exists():
        root = Tk()
        root.withdraw()

        if not messagebox.askyesno(
            "Data Missing",
            "raw_data_map.py was not found.\n\n"
            "Do you want to generate it now?"
        ):
            sys.exit(0)

        if not GENERATOR_FILE.exists():
            messagebox.showerror(
                "Error",
                "generator.py not found.\nCannot generate data."
            )
            sys.exit(1)

        # Run generator.py
        subprocess.run(
            [sys.executable, str(GENERATOR_FILE)],
            check=True
        )

        if not RAW_DATA_FILE.exists():
            messagebox.showerror(
                "Error",
                "raw_data_map.py was not created."
            )
            sys.exit(1)

    return import_raw_data_map()

def import_raw_data_map():
    """Dynamically imports raw_data_map.py"""
    spec = importlib.util.spec_from_file_location(
        "raw_data_map",
        RAW_DATA_FILE
    )
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module.raw_data_map
