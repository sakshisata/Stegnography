from tkinter import *
from tkinter import filedialog
import os
from PIL import Image, ImageTk
from stegano import lsb

root = Tk()
root.title("Steganography - SECRET code app")
root.geometry("700x500+150+180")
root.resizable(False, False)
root.configure(bg="#2f4155")

def showimage():
    global filename
    filename = filedialog.askopenfilename(initialdir=os.getcwd(),
                                          title='Select Image File',
                                          filetypes=(("PNG files", "*.png"),
                                                     ("JPG files", "*.jpg"),
                                                     ("All files", "*.*")))

    if filename:
        try:
            img = Image.open(filename)
            img = img.resize((250, 250), Image.Resampling.LANCZOS)
            img = ImageTk.PhotoImage(img)
            lb1.configure(image=img)
            lb1.image = img
        except Exception as e:
            print(f"Error opening or processing image: {e}")

def Hide():
    global filename
    message = text1.get(1.0, END).strip()
    if filename and message:
        try:
            secret = lsb.hide(filename, message)
            secret.save("hidden_image.png")
        except Exception as e:
            print(f"Error hiding message: {e}")

def Show():
    global filename
    if filename:
        try:
            clear_message = lsb.reveal(filename)
            text1.delete(1.0, END)
            text1.insert(END, clear_message)
        except Exception as e:
            print(f"Error revealing message: {e}")

def save():
    global filename
    if filename:
        try:
            img = Image.open(filename)
            img.save("")
        except Exception as e:
            print(f"Error saving image: {e}")

# Load the image for icon and logo
try:
    test_image_path = ""  # Replace with a valid test image
    icon_image = Image.open(test_image_path)
    image_icon = ImageTk.PhotoImage(icon_image)
    root.iconphoto(False, image_icon)
except Exception as e:
    print(f"Error loading image for icon: {e}")

try:
    logo_image = Image.open(test_image_path)
    logo = ImageTk.PhotoImage(logo_image)
    Label(root, image=logo, bg="#2f4155").place(x=10, y=0)
except Exception as e:
    print(f"Error loading image for logo: {e}")

# Create and place widgets
Label(root, text="CYBER SCIENCE", bg="#2d4155", fg="white", font="arial 25 bold").place(x=100, y=20)

f = Frame(root, bd=3, bg="black", width=340, height=280, relief=GROOVE)
f.place(x=10, y=80)

lb1 = Label(f, bg="black")
lb1.place(x=40, y=10)

frame2 = Frame(root, bd=3, width=340, height=280, bg="white", relief=GROOVE)
frame2.place(x=340, y=50)

text1 = Text(frame2, font="Roboto 20", bg="white", fg="black", relief=GROOVE)
text1.place(x=0, y=0, width=320, height=295)

scrollbar1 = Scrollbar(frame2)
scrollbar1.place(x=320, y=0, height=300)

scrollbar1.configure(command=text1.yview)
text1.configure(yscrollcommand=scrollbar1.set)

frame3 = Frame(root, bd=3, bg="#2f4155", width=330, height=100, relief=GROOVE)
frame3.place(x=10, y=370)

Button(frame3, text="Open Image", width=10, height=2, font="arial 14 bold", command=showimage).place(x=20, y=30)
Button(frame3, text="Save Image", width=10, height=2, font="arial 14 bold", command=save).place(x=180, y=30)
Label(frame3, text="Picture, Image, Photo File", bg="#2f4155", fg="yellow").place(x=20, y=5)

frame4 = Frame(root, bd=3, bg="#2f4155", width=330, height=100, relief=GROOVE)
frame4.place(x=360, y=370)

Button(frame4, text="Hide data", width=10, height=2, font="arial 14 bold", command=Hide).place(x=20, y=30)
Button(frame4, text="Show data", width=10, height=2, font="arial 14 bold", command=Show).place(x=180, y=30)
Label(frame4, text="Picture, Image, Photo File", bg="#2f4155", fg="yellow").place(x=20, y=5)

# Start the Tkinter event loop
root.mainloop()




