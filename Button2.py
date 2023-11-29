import tkinter as tk
from tkinter import PhotoImage

# List of image paths
image_paths = image_paths = [
    r"C:\Users\indom\Downloads\pixil-frame-0 (1).png",
    r"C:\Users\indom\Downloads\pixil-frame-0 (2).png",
    r"C:\Users\indom\Downloads\pixil-frame-0 (3).png",
    r"C:\Users\indom\Downloads\pixil-frame-0 (4).png",
    r"C:\Users\indom\Downloads\pixil-frame-0 (5).png",
    r"C:\Users\indom\Downloads\pixil-frame-0 (6).png",
    r"C:\Users\indom\Downloads\pixil-frame-0 (3).png",
    r"C:\Users\indom\Downloads\pixil-frame-0 (1).png",
    r"C:\Users\indom\Downloads\pixil-frame-0 (7).png",]
    # ... Your image paths ...


# List of messages to display
messages = [
    "Hi! My name is Larry welcome to this code. There is only one rule. DONT push the button.",
    "Agh! I'm yellow dont push it again!",
    "What did you do! Now im Yellow with poka-dots!",
    "Woah hey there! Wait a minute ... thats me !",
    "I said DONT push the button NOT PUSH IT MORE !",
    "Whew most are gone just one more and they will be gone!",
    "okay just one more press and I will be normal again.",
    "Okay all better now ... Maybe just one more press!",
    # ... Add more messages as needed ...
]

current_image_index = -1  # Start before the first image
current_message_index = -1  # Start before the first message

def update_content():
    global current_image_index, current_message_index, sprite_label, image_paths, sprite_image, message_label, messages

    # Load the next image
    current_image_index = (current_image_index + 1) % len(image_paths)
    new_image = PhotoImage(file=image_paths[current_image_index])
    sprite_label.configure(image=new_image)
    sprite_label.image = new_image  # Keep a reference to the new image

    # Update the message
    current_message_index = (current_message_index + 1) % len(messages)
    message_label.config(text=messages[current_message_index])

def on_button_click():
    # Update the displayed image and message
    update_content()

    # Remove the current button
    canvas.delete("button")

    # Create a new button with the same functionality
    create_round_button()

def create_round_button():
    # Draw a red circle that will act as a button
    canvas.create_oval(100, 100, 200, 200, fill='red', tags="button")
    # Put a text label in the middle of the circle
    canvas.create_text(150, 150, text="Don't Click Me", tags="button")
    # Bind the click event to the circle and text
    canvas.tag_bind("button", '<Button-1>', lambda event: on_button_click())

# Initialize the main application window
root = tk.Tk()
root.title("Image on Button Click")

# Initialize the canvas
canvas = tk.Canvas(root, width=300, height=300)
canvas.pack()

# Create a sprite label for displaying images
sprite_label = tk.Label(root)
sprite_label.pack()

# Create a label for displaying messages
message_label = tk.Label(root, text="", font=("Helvetica", 14))
message_label.pack()

# Create the initial round "button"
create_round_button()

# Start the GUI event loop
root.mainloop()
