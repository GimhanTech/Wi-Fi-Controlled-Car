import tkinter as tk # Python default GUI module
import urllib.request  # Module for handling URLs
from tkinter import messagebox
import keyboard  # Import the keyboard library


# Global variable for storing the root URL
root_url = ""


def ip_address(event=None):
    global root_url
    root_url = user_input.get()  # Update the global root_url with user input
    messagebox.showinfo("IP Address", f"IP Address set to: {root_url}")  # Show a message confirming the IP address


def send_request(url):
    """Send a request to the ESP8266."""
    try:
        urllib.request.urlopen(url)  # Send request to ESP
    except Exception as e:
        print(f"Error: {e}")


def move_forward():
    send_request(root_url + "/Forward")


def stop():
    send_request(root_url + "/Stop")


def move_backward():
    send_request(root_url + "/Backward")


def turn_left():
    send_request(root_url + "/Left")


def turn_right():
    send_request(root_url + "/Right")


def show_keys():
    messagebox.showinfo("Keyboard Keys", "Keys     Car Motion\n"
                                         "\n"
                                         "UP    -->  Forward\n"
                                         "DOWN  -->  Backward\n"
                                         "LEFT  -->  Turn Left\n"
                                         "RIGHT -->  Turn Right\n"
                                         "SPACE -->  Stop")


def show_signals():
    messagebox.showinfo("Send Signals", "Button       Signal\n"
                                        "\n"
                                        "Forward    --> Forward\n"
                                        "Backward   -->  Backward\n"
                                        "Turn Left  -->  Left\n"
                                        "Turn Right -->  Right\n"
                                        "Stop       -->  Stop")


def on_key_event(event):
    if event.name == 'up':
        move_forward()
    elif event.name == 'down':
        move_backward()
    elif event.name == 'left':
        turn_left()
    elif event.name == 'right':
        turn_right()
    elif event.name == 'space':
        stop()


def start_keyboard_control():
    """Start listening to keyboard events."""
    keyboard.on_press(on_key_event)


def stop_keyboard_control():
    """Stop listening to keyboard events."""
    keyboard.unhook_all()





def control_start():
    """Function to open the second window."""
    swindow = tk.Toplevel(window)
    swindow.title("Controlling Window")


    
    button_left = tk.Button(swindow, text="Left", command=turn_left, fg="yellow", bg="green", font=("Lobster 1.4", 25))
    button_left.grid(column=1, row=2)

    button_right = tk.Button(swindow, text="Right", command=turn_right, fg="yellow", bg="green", font=("Lobster 1.4", 25))
    button_right.grid(column=3, row=2)

    button_forward = tk.Button(swindow, text="Forward", command=move_forward, fg="yellow", bg="green", font=("Lobster 1.4", 25))
    button_forward.grid(column=2, row=1)

    button_backward = tk.Button(swindow, text="Backward", command=move_backward, fg="yellow", bg="green", font=("Lobster 1.4", 25))
    button_backward.grid(column=2, row=3)

    button_stop = tk.Button(swindow, text="Stop", command=stop, fg="yellow", bg="red", font=("Lobster 1.4", 25))
    button_stop.grid(column=2, row=2)




# Create the main window
window = tk.Tk()
window.title("Wi-fi Car Window")


# Add widgets to the window
headline1 = tk.Label(window, text="Keyboard and Button Control Wi-Fi Car", fg="red", font=("ANUDAW", 25))
headline1.grid(column=1, row=0)




# Entry widget for IP address input with increased font size
user_input = tk.Entry(window, font=("Helvetica", 20))
user_input.grid(column=1, row=1)
user_input.bind("<Return>", ip_address)

# Button to set IP address
button_set_ip = tk.Button(window, text="Set IP Address", command=ip_address, fg="white", bg="blue", font=("Lobster 1.4", 20))
button_set_ip.grid(column=2, row=1)


# Buttons for displaying information and controlling keyboard input
button_show_keys = tk.Button(window, text="Show Keyboard Keys", command=show_keys, fg="black", bg="orange", font=("Lobster 1.4", 25))
button_show_keys.grid(column=1, row=2)

button_show = tk.Button(window, text="Show Send Signals", command=show_signals, fg="black", bg="orange", font=("Lobster 1.4", 25))
button_show.grid(column=1, row=3)

headline1 = tk.Label(window, text="//////////////////////////", fg="white", font=("ANUDAW", 25))
headline1.grid(column=1, row=4)

button_start_keyboard = tk.Button(window, text="Start Keyboard Control", command=start_keyboard_control, fg="white", bg="green", font=("Lobster 1.4", 25))
button_start_keyboard.grid(column=1, row=5)

button_stop_keyboard = tk.Button(window, text="Stop Keyboard Control", command=stop_keyboard_control, fg="white", bg="red", font=("Lobster 1.4", 25))
button_stop_keyboard.grid(column=1, row=6)

headline1 = tk.Label(window, text="//////////////////////////", fg="white", font=("ANUDAW", 25))
headline1.grid(column=1, row=7)

control_start = tk.Button(window, text="Button Control Window", command=control_start, fg="yellow", bg="green", font=("Lobster 1.4", 25))
control_start.grid(column=1, row=8)


# Start the Tkinter main loop
window.mainloop()
