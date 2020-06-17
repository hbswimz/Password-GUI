import tkinter as tk
from hacker import main_hacker

# Makes GUI and Sets Background
root = tk.Tk()
root.geometry("580x580")
root.configure(bg='Lime')
root.title("Has Your Password Been Hacked?")

# Global Vars
my_string = tk.StringVar(root)

# GUI (need to do: show image)
general = tk.Label(root, text="""
Welcome to the password checker like no other. This password checker checks
if your password has ever been hacked! If you are interested to know this
information, please continue. (By Henry Boisdequin)
""", bg='Lime')
general.grid(column=0, row=0)
# Asks for password
p_label = tk.Label(root, text="Please Enter Your Password", bg='Lime')
p_label.grid(column=0, row=1)


# Gets password from user
en = tk.Entry(root, width=35, borderwidth=5, show='*', textvariable=my_string)
en.grid(column=0, row=2)


# If button is clicked than show is password has been hacked
def if_clicked():
    password = en.get()
    main_hacker(password)


# Button which user clicks to check if password has been hacked
my_button = tk.Button(root, padx=10, pady=10, text="Done", bg='Lime', command=if_clicked)
my_button.grid(column=0, row=3)


if __name__ == '__main__':
    root.mainloop()
