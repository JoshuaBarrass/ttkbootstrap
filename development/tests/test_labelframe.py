import tkinter as tk
from tkinter import ttk
from ttkbootstrap import Style

DARK = 'superhero'
LIGHT = 'flatly'


def create_labelframe_style(bootstyle, style):
    frame = ttk.Frame(root, padding=5)

    # title
    title = ttk.Label(frame, text='Labelframe', anchor=tk.CENTER)
    title.pack(padx=5, pady=2, fill=tk.BOTH)
    ttk.Separator(frame).pack(padx=5, pady=5, fill=tk.X)

    # default
    lbl = ttk.Labelframe(
        master=frame,
        text='default',
        bootstyle=bootstyle,
        width=150,
        height=75
    )
    lbl.pack(padx=5, pady=5, fill=tk.BOTH)

    # colored
    for color in style.colors:
        lbl = ttk.Labelframe(
            master=frame,
            text=color,
            bootstyle=color,
            width=150,
            height=75
        )
        lbl.pack(padx=5, pady=5, fill=tk.BOTH)

    return frame


if __name__ == '__main__':
    # create visual widget style tests
    root = tk.Tk()
    style = Style(theme=LIGHT)

    create_labelframe_style('', style).pack(side=tk.LEFT)

    root.mainloop()