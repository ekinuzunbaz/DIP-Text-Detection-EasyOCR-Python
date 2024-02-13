import cv2
import numpy as np
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from tkinter import ttk
from boxes import textDetection
# ----- GUI Functions -----
def load_image_command():
    global input_image
    global file_path

    # Selected file's path is stored in the file_path variable (full path to the selected file)
    file_path = filedialog.askopenfilename()

    if file_path:
        input_image = cv2.imread(file_path)

        # Inform the user about the operation
        messagebox.showinfo("Info", "Image loaded successfully!")
    else:
        messagebox.showinfo("Info", "You closed the file dialog without choosing an image!\n\nDon't forget to choose an image before trying extraction.")

def extract_title_command():
    global input_image
    global language_code
    
    if input_image is not None:
        # Extract the title
        print("EXTRACTION")
        print("language code: ", language_code)
        extracted_text = textDetection(input_image,language_code)
        
        # Create a new window to display the extracted text
        window_width = 400
        window_height = 300

        text_window = tk.Toplevel(root)
        text_window.title("Extracted Text")
        text_window.geometry(f"{window_width}x{window_height}")

        # Frame to contain information message
        info_frame = tk.Frame(text_window)
        info_frame.pack(padx=20, pady=20)

        # Display the info  label
        info_label = tk.Label(info_frame, text="📖 Possible Cover Text of Book 📖", font=('Arial', 16, 'bold'))
        info_label.pack()

        # Frame to contain information message
        subinfo_frame = tk.Frame(text_window)
        subinfo_frame.pack(padx=20, pady=20)

        # Display the info  label
        subinfo_label = tk.Label(subinfo_frame, text="You can copy it by using button below", font=('Arial', 10, 'bold'))
        subinfo_label.pack()

        # Frame to contain the extracted text and button
        frame = tk.Frame(text_window)
        frame.pack(padx=20, pady=20)

        # Display the extracted text in a label inside the new window
        # Create a Text widget
        text_widget = tk.Text(frame, wrap='word', width=25, height=5)

        # Insert the text
        text_widget.insert('1.0', extracted_text)

        # Disable editing
        text_widget.config(state='disabled')

        # Create a scrollbar
        scrollbar = tk.Scrollbar(frame)

        # Configure the scrollbar to scroll the text widget
        scrollbar.config(command=text_widget.yview)
        
        # Pack the text widget and the scrollbar
        text_widget.pack(side='left', fill='both', expand=True)
        
        # Function to copy the text to clipboard
        def copy_to_clipboard():
            text_window.clipboard_clear()
            text_window.clipboard_append(extracted_text)
            text_window.update()

        # Button to copy text to clipboard
        copy_button = tk.Button(frame, text="Copy to Clipboard", command=copy_to_clipboard)
        copy_button.pack(side='left', padx=10)
        input_image = None

    else:
        messagebox.showerror("Error", "No image is selected!\nFirstly, choose an image!")

def about_us_command():
        messagebox.showinfo("Info", "Developed by\n\n2018510115_Yusuf-Orhan-Okkabas\n\n2018510127_Ekin-Uzunbaz\n\n2019510019_Yüksel-Baltacıoğlu\n\n\tAralık 2023")

# Create the GUI
root = tk.Tk()
root.title("Book Title Extraction")

# Set the window size (width x height)
window_width = 500
window_height = 500
root.geometry(f"{window_width}x{window_height}")

# *** PLACE THE ROOT WINDOW ON THE CENTER OF SCREEN ***
# # Calculate screen dimensions
# screen_width = root.winfo_screenwidth()
# screen_height = root.winfo_screenheight()

# # Calculate window position to center it
# x_coordinate = int((screen_width - window_width) / 2)
# y_coordinate = int((screen_height - window_height) / 2)

# # Set the window position to center
# root.geometry(f"{window_width}x{window_height}+{x_coordinate}+{y_coordinate}")

# Variable to hold the input image and language code through the application
input_image = None
language_code = 'en'

# Frame to contain information message
welcome_frame = tk.Frame(root)
welcome_frame.pack(padx=20, pady=20)

# Display the info  label
welcome_label = tk.Label(welcome_frame, text="WELCOME", font=('Arial', 16, 'bold'))
welcome_label.pack()

# Create a frame for buttons
button_frame = tk.Frame(root)
button_frame.pack(pady=15)

# Create a dictionary to map display values to language codes
language_codes = {"English": "en", "Turkish": "tr"}

# Define buttons and assign functions to these buttons
load_button = tk.Button(button_frame, text="Load Image of Book Cover", command=load_image_command)
extract_button = tk.Button(button_frame, text="Extract Title", command=extract_title_command)
language_label = tk.Label(button_frame, text="Select Language:")
language_combobox = ttk.Combobox(button_frame, values=list(language_codes.keys()), state="readonly")
about_us_button = tk.Button(button_frame, text="About Us", command=about_us_command)

# Define a function to be called when a selection is made
def combobox_selected(event):
    global language_code
    
    # Get the selected display value
    display_value = language_combobox.get()
    
    # Look up the corresponding language code
    language_code = language_codes[display_value]
    
    print(language_code)

# Set the function to be called when a selection is made
language_combobox.bind("<<ComboboxSelected>>", combobox_selected)

# Place buttons below each other
load_button.pack(pady=25)
extract_button.pack(pady=25)
about_us_button.pack(pady=25)
language_label.pack(pady=25)
language_combobox.pack(pady=25)

root.mainloop()