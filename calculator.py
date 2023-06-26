import tkinter as tk

win = tk.Tk()
win.geometry("312x335")
win.resizable(0, 0) # type: ignore
win.title("Calculator")

input_value = ""
display_text = tk.StringVar()


def click_button_action(item):
    global input_value
    input_value = input_value + str(item)
    display_text.set(input_value)
    global input_value
    calculate = str(eval(input_value))
    display_text.set(calculate)


def clear_button_action():
    global input_value
    input_value = ""
    display_text.set("")

def equal_button_action():
    global input_value
    calculate = str(eval(input_value))
    display_text.set(calculate)    


def keyboard_input(event):
    key = event.char
    if key.isdigit():
        click_button_action(int(key))
    elif key == "+":
        click_button_action("+")
    elif key == "-":
        click_button_action("-")
    elif key == "*":
        click_button_action("*")
    elif key == "/":
        click_button_action("/")
    elif key == "=" or key == "\r":
        equal_button_action()
    elif key == "\x08":  # Backspace key
        clear_button_action()


input_frame = tk.Frame(win, width=312, height=50, background="lightgrey", highlightbackground="Black", highlightthickness=2)
input_frame.pack(side=tk.TOP)

input_field = tk.Entry(input_frame, width=312, textvariable=display_text, font=("Arial", 18, "bold"), bd=0, background="lightgrey", justify=tk.RIGHT)
input_field.pack(ipady=10)

buttons_frame = tk.Frame(win, width=312, height=274)
buttons_frame.pack()

clear_btn = tk.Button(buttons_frame, width=33, height=3, text="C", background="#eee", bd=1, fg="Black",
cursor="hand2", command=lambda: clear_button_action()).grid(row=0, column=0, columnspan=3, padx=1, pady=1)
divide_btn = tk.Button(buttons_frame, width=10, height=3, text="/", background="#eee", bd=1, fg="Black",
                       cursor="hand2", command=lambda: click_button_action("/")).grid(row=0, column=3, padx=1, pady=1)

btn_7 = tk.Button(buttons_frame, width=10, height=3, text="7", background="#fff", bd=1, fg="Black", cursor="hand2",
                  command=lambda: click_button_action(7)).grid(row=1, column=0, padx=1, pady=1)
btn_8 = tk.Button(buttons_frame, width=10, height=3, text="8", background="#fff", bd=1, fg="Black", cursor="hand2",
                  command=lambda: click_button_action(8)).grid(row=1, column=1, padx=1, pady=1)
btn_9 = tk.Button(buttons_frame, width=10, height=3, text="9", background="#fff", bd=1, fg="Black", cursor="hand2",
                  command=lambda: click_button_action(9)).grid(row=1, column=2, padx=1, pady=1)
mul_btn = tk.Button(buttons_frame, width=10, height=3, text="x", background="#eee", bd=1, fg="Black", cursor="hand2",
                    command=lambda: click_button_action("*")).grid(row=1, column=3, padx=1, pady=1)

btn_4 = tk.Button(buttons_frame, width=10, height=3, text="4", background="#fff", bd=1, fg="Black", cursor="hand2",
                  command=lambda: click_button_action(4)).grid(row=2, column=0, padx=1, pady=1)
btn_5 = tk.Button(buttons_frame, width=10, height=3, text="5", background="#fff", bd=1, fg="Black", cursor="hand2",
                  command=lambda: click_button_action(5)).grid(row=2, column=1, padx=1, pady=1)
btn_6 = tk.Button(buttons_frame, width=10, height=3, text="6", background="#fff", bd=1, fg="Black", cursor="hand2",
                  command=lambda: click_button_action(6)).grid(row=2, column=2, padx=1, pady=1)
sub_btn = tk.Button(buttons_frame, width=10, height=3, text="-", background="#eee", bd=1, fg="Black", cursor="hand2",
                    command=lambda: click_button_action("-")).grid(row=2, column=3, padx=1, pady=1)

btn_3 = tk.Button(buttons_frame, width=10, height=3, text="3", background="#fff", bd=1, fg="Black", cursor="hand2",
                  command=lambda: click_button_action(3)).grid(row=3, column=0, padx=1, pady=1)
btn_2 = tk.Button(buttons_frame, width=10, height=3, text="2", background="#fff", bd=1, fg="Black", cursor="hand2",
                  command=lambda: click_button_action(2)).grid(row=3, column=1, padx=1, pady=1)
btn_1 = tk.Button(buttons_frame, width=10, height=3, text="1", background="#fff", bd=1, fg="Black", cursor="hand2",
                  command=lambda: click_button_action(1)).grid(row=3, column=2, padx=1, pady=1)
add_btn = tk.Button(buttons_frame, width=10, height=3, text="+", background="#eee", bd=1, fg="Black", cursor="hand2",
                    command=lambda: click_button_action("+")).grid(row=3, column=3, padx=1, pady=1)

btn_0 = tk.Button(buttons_frame, width=10, height=3, text="0", background="#fff", bd=1, fg="Black", cursor="hand2",
                  command=lambda: click_button_action(0)).grid(row=4, column=0, padx=1, pady=1)
btn_dot = tk.Button(buttons_frame, width=10, height=3, text=".", background="#fff", bd=1, fg="Black", cursor="hand2",
                    command=lambda: click_button_action(".")).grid(row=4, column=1, padx=1, pady=1)
equal_button = tk.Button(buttons_frame, width=20, height=3, text="=", background="#eee", bd=1, fg="Black",
                         cursor="hand2", command=lambda: equal_button_action()).grid(row=4, column=2, columnspan=2,
                                                                                     padx=1, pady=1)

# Bind keyboard events
win.bind('<Key>', keyboard_input)

win.mainloop()
