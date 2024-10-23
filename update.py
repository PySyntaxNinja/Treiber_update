import customtkinter as ctk
from tkinter import filedialog

# Initialize the application
app = ctk.CTk()
app.geometry("900x700")  # Increased size of the window
app.title("Update or Delete Files and Folders")

# Functions for button actions
def add_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        entry_update_file.delete(0, ctk.END)
        entry_update_file.insert(0, file_path)

def set_address():
    address = filedialog.askdirectory()
    if address:
        entry_update_address.delete(0, ctk.END)
        entry_update_address.insert(0, address)

def delete_folders():
    folder_path = filedialog.askdirectory()
    if folder_path:
        entry_delete_folder.delete(0, ctk.END)
        entry_delete_folder.insert(0, folder_path)

def start_update_or_delete():
    selected_radio = radio_var.get()
    if selected_radio == 1:
        log_textbox.insert(ctk.END, "Updating LSBSetup...\n")
    elif selected_radio == 2:
        log_textbox.insert(ctk.END, "Updating System_Update...\n")
    elif selected_radio == 3:
        log_textbox.insert(ctk.END, "Deleting Ethernet Folder...\n")
    else:
        log_textbox.insert(ctk.END, "No option selected.\n")

def search_apps_or_folders():
    log_textbox.insert(ctk.END, "Searching for Apps or Folders...\n")

# Frame 1 - Radio buttons for selecting update or delete option
frame1 = ctk.CTkFrame(app)
frame1.grid(row=0, column=0, columnspan=2, pady=10, sticky='ew')

radio_var = ctk.IntVar()

radio1 = ctk.CTkRadioButton(frame1, text="Update LSBSetup", variable=radio_var, value=1)
radio2 = ctk.CTkRadioButton(frame1, text="Update System_Update", variable=radio_var, value=2)
radio3 = ctk.CTkRadioButton(frame1, text="Delete Ethernet Folder", variable=radio_var, value=3)

radio1.grid(row=0, column=0, padx=20)
radio2.grid(row=0, column=1, padx=20)
radio3.grid(row=0, column=2, padx=20)

# Frame 2 - Entry and buttons for selecting a file and setting an update address
frame2 = ctk.CTkFrame(app)
frame2.grid(row=1, column=0, columnspan=2, pady=10, sticky='ew')

# File entry and button
entry_update_file = ctk.CTkEntry(frame2, width=300)
entry_update_file.grid(row=0, column=0, padx=10)

btn_add_file = ctk.CTkButton(frame2, text="Add File for Update", command=add_file)
btn_add_file.grid(row=0, column=1, padx=10)

# Address entry and button
entry_update_address = ctk.CTkEntry(frame2, width=300)
entry_update_address.grid(row=1, column=0, padx=10, pady=5)

btn_set_address = ctk.CTkButton(frame2, text="Set Adresse", command=set_address)
btn_set_address.grid(row=1, column=1, padx=10, pady=5)

# Frame 3 - Entry and button for selecting a folder to delete
frame3 = ctk.CTkFrame(app)
frame3.grid(row=2, column=0, columnspan=2, pady=10, sticky='ew')

entry_delete_folder = ctk.CTkEntry(frame3, width=300)
entry_delete_folder.grid(row=0, column=0, padx=10)

btn_delete_folder = ctk.CTkButton(frame3, text="Delete Folders", command=delete_folders)
btn_delete_folder.grid(row=0, column=1, padx=10)

# Frame 4 - Buttons for starting the update or delete process, and searching apps or folders
frame4 = ctk.CTkFrame(app)
frame4.grid(row=3, column=0, columnspan=2, pady=10, sticky='ew')

btn_start = ctk.CTkButton(frame4, text="Start Update or Delete", command=start_update_or_delete)
btn_start.grid(row=0, column=0, padx=10)

btn_search = ctk.CTkButton(frame4, text="Search Apps or Folders", command=search_apps_or_folders)
btn_search.grid(row=0, column=1, padx=10)

# Frame 5 - Textbox for logging with a scrollbar
frame5 = ctk.CTkFrame(app)
frame5.grid(row=4, column=0, columnspan=2, pady=10, sticky='nsew')

log_textbox = ctk.CTkTextbox(frame5, width=800, height=250)  # Increased the size of the textbox
log_textbox.grid(row=0, column=0, padx=10, pady=10, sticky='nsew')

scrollbar = ctk.CTkScrollbar(frame5, command=log_textbox.yview)
scrollbar.grid(row=0, column=1, sticky='ns')

log_textbox.configure(yscrollcommand=scrollbar.set)

# Configure the grid to expand the log textbox when resizing the window
app.grid_rowconfigure(4, weight=1)
app.grid_columnconfigure(0, weight=1)

# Start the application loop
app.mainloop()
