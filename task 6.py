import tkinter as tk
from tkinter import PhotoImage, Label, Button
from PIL import Image, ImageTk
from pathlib import Path

if __name__ == "__main__":
    root = tk.Tk()

    file = Path(__file__).resolve().parent.joinpath("test_axe.ico")
    root.iconbitmap(file)

    app = PhotoViewerApp(root)
    root.mainloop()
