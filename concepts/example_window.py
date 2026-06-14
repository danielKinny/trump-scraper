from tkinter import *
from tkinter import ttk

root = Tk()
root.withdraw()

popup = Toplevel(root)
popup.title("Notification")
popup.geometry("400x200")
popup.resizable(False, False)

popup.update_idletasks()
x = (popup.winfo_screenwidth() // 2) - (popup.winfo_width() // 2)
y = (popup.winfo_screenheight() // 2) - (popup.winfo_height() // 2)
popup.geometry(f"+{x}+{y}")

frm = ttk.Frame(popup, padding=20)
frm.pack(fill=BOTH, expand=True)

ttk.Label(frm, text="TRUMP HAS TWEETED!", font=("Arial", 14, "bold")).pack(pady=10)
ttk.Label(frm, text="EXAMPLE TEXT", wraplength=350).pack(pady=5)

# Add buttons
button_frame = ttk.Frame(frm)
button_frame.pack(pady=15)
ttk.Button(button_frame, text="GOT IT!", command=popup.destroy).pack(side=LEFT, padx=5)
popup.protocol("WM_DELETE_WINDOW", root.destroy)

root.bell()

root.mainloop()