import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import cv2
from PIL import Image, ImageTk
import numpy as np

# create a GUI window
root = tk.Tk()
root.title("Image Resize Tool")
root.geometry("600x600")

# Global variable to save the image
original_image = None
resized_image = None

# Load image function
def load_image():
    global original_image
    # pop up the option
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.png;*.jpeg;*.bmp")])
    
    if not file_path:
        return
    
    # read image
    original_image = cv2.imread(file_path)
    if original_image is None:
        messagebox.showerror("Error", "Can not read image")
        return
    
    # change to RBG to display
    image_rgb = cv2.cvtColor(original_image, cv2.COLOR_BGR2RGB)
    img = Image.fromarray(image_rgb)
    img.thumbnail((400, 400))  # adjust the window to show the image
    img = ImageTk.PhotoImage(img)
    
    # show the image
    panel.config(image=img)
    panel.image = img

# reize image
def resize_image():
    global original_image, resized_image
    
    if original_image is None:
        messagebox.showerror("Error", "Upload an image please")
        return
    
    try:
        # input the sieze
        target_width = int(width_entry.get())
        target_height = int(height_entry.get())
    except ValueError:
        messagebox.showerror("Error", "Input is invalid")
        return
    
    # resize image
    resized_image = cv2.resize(original_image, (target_width, target_height))
    
    # change to RGB
    image_rgb = cv2.cvtColor(resized_image, cv2.COLOR_BGR2RGB)
    img = Image.fromarray(image_rgb)
    img.thumbnail((400, 400))  #
    img = ImageTk.PhotoImage(img)
    
    # show new image
    panel.config(image=img)
    panel.image = img

# save image
def save_image():
    global resized_image
    
    if resized_image is None:
        messagebox.showerror("Error", "Resize your image first")
        return
    

    save_path = filedialog.asksaveasfilename(defaultextension=".jpg", filetypes=[("JPEG", "*.jpg"), ("PNG", "*.png")])
    if save_path:
        cv2.imwrite(save_path, resized_image)
        messagebox.showinfo("Saved", f"Save to: {save_path}")


load_button = tk.Button(root, text="Open", command=load_image)
load_button.pack(pady=20)


width_label = tk.Label(root, text="Width:")
width_label.pack()
width_entry = tk.Entry(root)
width_entry.pack()

height_label = tk.Label(root, text="Height:")
height_label.pack()
height_entry = tk.Entry(root)
height_entry.pack()

# button 1
resize_button = tk.Button(root, text="Resize", command=resize_image)
resize_button.pack(pady=20)

# save button
save_button = tk.Button(root, text="Save", command=save_image)
save_button.pack(pady=20)


panel = tk.Label(root)
panel.pack(padx=10, pady=10)

# launch GUI
root.mainloop()
