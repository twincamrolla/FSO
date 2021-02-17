from tkinter import *
from PIL import ImageTk, Image
import pyttsx3

root = Tk()
root.title("FSOperations")
root.iconbitmap('c:/gui/exes/1.ico')
root.geometry("400x400")
#e.insert(0, "Enter Your Name: ")

engine = pyttsx3.init()
engine.say("Welcome to Flight Sim Operations!")

engine.runAndWait()

my_menu = Menu(root)

root.config(menu=my_menu)

def button_add():
	return

# click command

def our_command():
    my_label = Label(root, text="You Clicked a Dropdown Menu!").pack()

def file_Login():
    hide_all_frames()
    top = Toplevel()
    top.title('FSOperations')
    top.iconbitmap('c:/gui/1.ico')
    top.geometry("400x400")

    # Create Text Boxes
    Username_top = Entry(top, width=30)
    Username_top.grid(row=0, column=1, padx=20, pady=(10, 0))
    Password_top = Entry(top, width=30)
    Password_top.grid(row=1, column=1)
    
    # create text box labels
    Username_label = Label(top, text="Username")
    Username_label.grid(row=0, column=0, pady=(10, 0))
    Password_label = Label(top, text="Password")
    Password_label.grid(row=1, column=0)

    btn = Button(top, text="Login", padx=15, pady=5)
    btn.grid(row=2, column=0)
    
    

# edit cut
def edit_cut():
    hide_all_frames()
    edit_cut_frame.pack(fill="both", expand=1)
    my_label = Label(root, text="You Clicked the Edit >> Edit cut Menu!").pack()


# hide all frames 
def hide_all_frames():
    file_new_frame.pack_forget()
    edit_cut_frame.pack_forget()

# create a menu item

file_menu = Menu(my_menu)
my_menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Login", command=file_Login)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

# create a edit menu item
edit_menu = Menu(my_menu)
my_menu.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Cut", command=edit_cut)
edit_menu.add_command(label="Copy", command=our_command)

# create an options menu
option_menu = Menu(my_menu)
my_menu.add_cascade(label="Options", menu=option_menu)
option_menu.add_command(label="Find", command=our_command)
option_menu.add_command(label="Find Next", command=our_command)

# create some frames
file_new_frame = Frame(root, width=400, height=400, bg="red")
edit_cut_frame = Frame(root, width=400, height=400, bg="blue")

# define buttons

button_2 = Button(root, text="start flight", padx=20, pady=5, command=button_add)
button_3= Button(root, text="finish flight", padx=20, pady=5, command=button_add)
button_4 = Button(root, text="cancel flight", padx=20, pady=5, command=button_add)



#put the buttons on the screen 
button_2.pack()
button_3.pack()
button_4.pack()

button_quit = Button(root, text="exit", command=root.quit)
button_quit.pack()




root.mainloop()

