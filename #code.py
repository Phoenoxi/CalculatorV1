import customtkinter

# Initialize the customtkinter application
app = customtkinter.CTk()
app.title("CalculatorV1")
app.geometry("700x500")

equation = ""

#text box
textbox = customtkinter.CTkTextbox(app, width = 700, height = 100)
textbox.grid(row = 0, column = 0, columnspan = 4)



#Buttons
def fclear():
    global equation
    equation = ""

    textbox.delete("1.0", "end")

def fequal():
    global equation

    equation_list = equation.split(",")

    if equation_list[1] == "+":
        total = str(float(equation_list[0]) + float(equation_list[2]))
        textbox.delete("1.0", "end")
        textbox.insert("end", str(total))
        equation = total
        print(equation)
    elif equation_list[1] == "-":
        total = str(float(equation_list[0]) - float(equation_list[2]))
        textbox.delete("1.0", "end")
        textbox.insert("end", str(total))
        equation = total
    elif equation_list[1] == "*":
        total = str(float(equation_list[0]) * float(equation_list[2]))
        textbox.delete("1.0", "end")
        textbox.insert("end",str(total))
        equation = total
    elif equation_list[1] == "/":
        if equation_list[2] == "0":
            textbox.delete("1.0", "end")
            textbox.insert("end", "Error/Zero Division")

        else:
            total = str(float(equation_list[0]) / float(equation_list[2]))
            textbox.delete("1.0", "end")
            textbox.insert("end",str(total))
            equation = total




def fbutton_0():
    global equation

    equation += "0"
    textbox.insert("end", "0")


def fbutton_1():
    global equation

    equation += "1"
    textbox.insert("end", "1")

def fbutton_2():
    global equation

    equation += "2"
    textbox.insert("end", "2")

def fbutton_3():
    global equation

    equation += "3"
    textbox.insert("end", "3")

def fbutton_4():
    global equation

    equation += "4"
    textbox.insert("end", "4")

def fbutton_5():
    global equation
    equation += "5"
    textbox.insert("end", "5")
    print(equation)

def fbutton_6():
    global equation
    equation += "6"
    textbox.insert("end", "6")
def fbutton_7():
    global equation
    equation += "7"
    textbox.insert("end", "7")
def fbutton_8():
    global equation
    equation += "8"
    textbox.insert("end", "8")
def fbutton_9():
    global equation
    equation += "9"
    textbox.insert("end", "9")

def button_additon():
    global equation
    equation += ",+,"
    textbox.insert("end", "+")

def button_subtraction():
    global equation
    equation += ",-,"
    textbox.insert("end", "-")

def button_multiplication():
    global equation
    equation += ",*,"
    textbox.insert("end", "*")

def button_division():
    global equation
    equation += ",/,"
    textbox.insert("end", "/")








button_0 = customtkinter.CTkButton(app, text="0", command=fbutton_0)
button_0.grid(row = 5, column= 0, pady=(0, 20))

button_1 = customtkinter.CTkButton(app, text="1", command=fbutton_1)
button_1.grid(row = 4, column= 0, pady=(0, 20))

button_2 = customtkinter.CTkButton(app, text="2", command=fbutton_2)
button_2.grid(row = 4, column= 1, pady=(0, 20))

button_3 = customtkinter.CTkButton(app, text="3", command=fbutton_3)
button_3.grid(row = 4, column= 2, pady=(0, 20))

button_4 = customtkinter.CTkButton(app, text="4", command=fbutton_4)
button_4.grid(row = 3, column= 0, pady=(0, 20))

button_5 = customtkinter.CTkButton(app, text="5", command=fbutton_5)
button_5.grid(row = 3, column= 1, pady=(0, 20))

button_6 = customtkinter.CTkButton(app, text="6", command=fbutton_6)
button_6.grid(row = 3, column= 2, pady=(0, 20))

button_7 = customtkinter.CTkButton(app, text="7", command=fbutton_7)
button_7.grid(row = 2, column= 0, pady=(0, 20))

button_8 = customtkinter.CTkButton(app, text="8", command=fbutton_8)
button_8.grid(row = 2, column= 1, pady=(0, 20))

button_9 = customtkinter.CTkButton(app, text="9", command=fbutton_9)
button_9.grid(row = 2, column= 2, pady=(0, 20))

button_additon = customtkinter.CTkButton(app, text="+", command=button_additon)
button_additon.grid(row=3, column=3,pady=(0, 20))

button_equal = customtkinter.CTkButton(app, text="=", command=fequal)
button_equal.grid(row=2, column=3, pady=(0, 20))

button_clear = customtkinter.CTkButton(app, text="clear", command=fclear)
button_clear.grid(row=1, column=3, pady=(0, 20))

button_subtraction = customtkinter.CTkButton(app, text="-", command=button_subtraction)
button_subtraction.grid(row=4, column=3, pady=(0, 20))

button_multiplication = customtkinter.CTkButton(app, text="*", command=button_multiplication)
button_multiplication.grid(row=5, column=3, pady=(0, 20))

button_division = customtkinter.CTkButton(app, text="/", command=button_division)
button_division.grid(row=6, column=3, pady=(0, 20))




# Run the application
app.mainloop()