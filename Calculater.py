from tkinter import *

root = Tk()
root.title("CALCULATOR BY Raghav")
root.geometry("360x470")

#---------------------------TEXTBOX--------------------------#
textbox = Entry(root, relief="sunken", borderwidth=5, font=("Consolas", 15))
textbox.grid(row=0, column=0,columnspan=2, pady=10, padx=10)
textbox.config(width=30)


#---------------------------FUNCTIONS-----------------------#
def button_click(number):
	current = textbox.get()
	textbox.delete(0, END)
	textbox.insert(0, str(current) + str(number))

def button_clear():
	textbox.delete(0, END)

def button_add():
	first_number = textbox.get()
	global f_num
	global math
	math = "addition"
	f_num = int(first_number)
	textbox.delete(0, END)

def button_equal():
	second_number = textbox.get()
	textbox.delete(0, END)

	if math == "addition":
		textbox.insert(0, f_num + int(second_number))

	if math == "subtraction":
		textbox.insert(0, f_num - int(second_number))

	if math == "multiplication":
		textbox.insert(0, f_num * int(second_number))

	if math == "division":
		textbox.insert(0, f_num / int(second_number))

def button_subtract():
	first_number = textbox.get()
	global f_num
	global math
	math = "subtraction"
	f_num = int(first_number)
	textbox.delete(0, END)

def button_multiply():
    first_number = textbox.get()
    global f_num
    global math
    math = "multiplication"
    f_num = int(first_number)
    textbox.delete(0, END)

def button_divide():
	first_number = textbox.get()
	global f_num
	global math
	math = "division"
	f_num = int(first_number)
	textbox.delete(0, END)


#---------------------------BUTTONS--------------------------#
button1 = Button(root, text="1", width=15, font=("Consolas", 12), fg="black", bg="cyan",
	command = lambda: button_click(1))
button1.grid(row=1, column=0, pady=4)


button2 = Button(root, text="2", width=15, font=("Consolas", 12), fg="black", bg="cyan",
	command = lambda: button_click(2))
button2.grid(row=2, column=0, pady=4)

button3 = Button(root, text="3", width=15, font=("Consolas", 12), fg="black", bg="cyan",
	command = lambda: button_click(3))
button3.grid(row=3, column=0, pady=4)

button4 = Button(root, text="4", width=15, font=("Consolas", 12), fg="black", bg="cyan",
	command = lambda: button_click(4))
button4.grid(row=4, column=0, pady=4)

button5 = Button(root, text="5", width=15, font=("Consolas", 12), fg="black", bg="cyan",
	command = lambda: button_click(5))
button5.grid(row=5, column=0, pady=4)

button6 = Button(root, text="6", width=15, font=("Consolas", 12), fg="black", bg="cyan",
	command = lambda: button_click(6))
button6.grid(row=6, column=0, pady=4)

button7 = Button(root, text="7", width=15, font=("Consolas", 12), fg="black", bg="cyan",
	command = lambda: button_click(7))
button7.grid(row=7, column=0, pady=4)

button8 = Button(root, text="8", width=15, font=("Consolas", 12), fg="black", bg="cyan",
	command = lambda: button_click(8))
button8.grid(row=8, column=0, pady=4)

button9 = Button(root, text="9", width=15, font=("Consolas", 12), fg="black", bg="cyan",
	command = lambda: button_click(9))
button9.grid(row=9, column=0, pady=4)

button10 = Button(root, text="0", width=15, font=("Consolas", 12), fg="black", bg="cyan",
	command = lambda: button_click(0))
button10.grid(row=10, column=0, pady=4)

button11 = Button(root, text="+", width=15, font=("Consolas", 12), fg="black", bg="cyan",
	command = button_add)
button11.grid(row=1, column=1, pady=4)

button12 = Button(root, text="-", width=15, font=("Consolas", 12), fg="black", bg="cyan",
	command = button_subtract)
button12.grid(row=2, column=1, pady=4)

button13 = Button(root, text="*", width=15, font=("Consolas", 12), fg="black", bg="cyan",
	command = button_multiply)
button13.grid(row=3, column=1, pady=4)

button14 = Button(root, text="/", width=15, font=("Consolas", 12), fg="black", bg="cyan",
	command = button_divide)
button14.grid(row=4, column=1, pady=4)

button15 = Button(root, text="=", width=15, font=("Consolas", 12), fg="black", bg="cyan",
	command = button_equal)
button15.grid(row=5, column=1, pady=4)

button16 = Button(root, text=".", width=15, font=("Consolas", 12), fg="black", bg="cyan",
	command = lambda: button_click())
button16.grid(row=6, column=1, pady=4)

button17 = Button(root, text="CLEAR", font=("Consolas", 12), fg="black", bg="cyan",
	command = button_clear)
button17.grid(row=7, column=1, pady=4)
button17.config(width=15)



#-----MAINLOOP-----#
root.mainloop()