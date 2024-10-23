from tkinter import *
from PIL import ImageTk, Image
import os

def on_enter(event, widget, default_text):
    if widget.get() == default_text:
        widget.delete(0, END)
        widget.config(fg='black')

def hide():
    passwordEntry.config(show='*')
    eyeButton.config(image=openeye)  # Set the button image to "openeye"
    eyeButton.config(command=show)

def show():
    passwordEntry.config(show='')  # Show the password
    eyeButton.config(image=closeeye)  # Set the button image to "closeeye"
    eyeButton.config(command=hide)

root = Tk()
root.geometry('1000x800+50+50')
root.resizable(0, 0)
root.title('Login Page')

# Ensure the image files are found
image_path = 'login page/1.new.JPG'
eye_image_path = 'login page/openeye.png'
close_eye_image_path = 'login page/close image.png'

if not os.path.exists(image_path) or not os.path.exists(eye_image_path) or not os.path.exists(close_eye_image_path):
    print(f"Error: One or more image files do not exist. Make sure {image_path}, {eye_image_path}, and {close_eye_image_path} are in the correct directory.")
    root.destroy()
    exit(1)

bgImage = ImageTk.PhotoImage(file=image_path)
bgLabel = Label(root, image=bgImage)
bgLabel.pack()

heading = Label(root, text='USER LOGIN', font=('Microsoft YaHei UI Light', 16, 'bold'), fg='firebrick1', bg='white')
heading.place(x=525, y=50)

usernameEntry = Entry(root, width=25, font=('Microsoft YaHei UI Light', 11, 'bold'), bd=0, fg='firebrick1')
usernameEntry.place(x=480, y=100)
usernameEntry.insert(0, 'Username')
usernameEntry.bind('<FocusIn>', lambda event: on_enter(event, usernameEntry, 'Username'))

frame1 = Frame(root, width=250, height=2, bg='firebrick1')
frame1.place(x=480, y=120)

passwordEntry = Entry(root, width=25, font=('Microsoft YaHei UI Light', 11, 'bold'), bd=0, fg='firebrick1', show='*')
passwordEntry.place(x=480, y=140)
passwordEntry.insert(0, 'Password')
passwordEntry.bind('<FocusIn>', lambda event: on_enter(event, passwordEntry, 'Password'))

frame2 = Frame(root, width=250, height=2, bg='firebrick1')
frame2.place(x=480, y=160)

# Load both eye icons once at the start
openeye = Image.open(eye_image_path)
openeye = openeye.resize((20, 20), Image.LANCZOS)
openeye = ImageTk.PhotoImage(openeye)

closeeye = Image.open(close_eye_image_path)
closeeye = closeeye.resize((20, 20), Image.LANCZOS)
closeeye = ImageTk.PhotoImage(closeeye)

# Set the initial button with the "openeye" image
eyeButton = Button(root, image=openeye, bd=0, bg='white', activebackground='white', cursor='hand2', command=show)
eyeButton.place(x=735, y=135)  # Adjust x to align better with the password entry

forgetButton = Button(root, text='Forgot Password?', bd=0, bg='white', activebackground='white', cursor='hand2',
                      font=('Microsoft YaHei UI Light', 11, 'bold'), fg='firebrick1', activeforeground='firebrick1')
forgetButton.place(x=610, y=165)

loginButton = Button(root, text='Login', font=('Open Sans', 14, 'bold'), fg='white', bg='firebrick1', activeforeground='white',
                     activebackground='firebrick1', cursor='hand2', bd=0, width=22)
loginButton.place(x=480, y=205)

signupLabel = Label(root, text='Don\'t have an account?', font=('Open Sans', 10, 'bold'), fg='firebrick1', bg='white')
signupLabel.place(x=460, y=265)

newaccountButton = Button(root, text='Create new one!', font=('Open Sans', 10, 'bold underline'), fg='white', bg='firebrick1',
                          activeforeground='white', activebackground='firebrick1', cursor='hand2', bd=0)
newaccountButton.place(x=630, y=260)

root.mainloop()
