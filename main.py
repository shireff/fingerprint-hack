
from tkinter import *

root = Tk()
root.title('ZkTeco Password Reset')
root.config(bg='orange')


def zkteco():
    try:
        time = int(a.get())
        result = 9999 - time
        x = result * result
        label.config(text=(f"Username: 8888\nPassword: {x}"))
    except ValueError:
        print("Enter a valid number")


Label(root, text="Enter the time on the machine screen!",
      font=('calibri', 30, 'bold'),
      background='orange',
      foreground='white').pack()

a = Entry(root, width=36)
a.pack()

label = Label(root, text="",
              font=('Arial', 15, 'bold'),
              background="black",
              width=18,
              foreground="white")
label.pack(pady=20)

Button(root, text="Calculate",
       background="green",
       width=20,
       foreground="black",
       command=zkteco).pack()
Button(root,
       text='Exit',
       width=20,
       background="green",
       foreground="black",
       command=root.quit).pack()

root.mainloop()
