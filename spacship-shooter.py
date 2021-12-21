import tkinter as tk
root = tk.Tk()
root.geometry("1100x1000")
frame = tk.Frame()
canvas = tk.Canvas(frame)
frame.pack(expan=True,fill="both")
frame.master.title("The spacship Allien shooter!")
canvas.pack(expan=True,fill="both")
root.mainloop()