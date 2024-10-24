import customtkinter as ctk
from tkinter import filedialog, messagebox
import os
import shutil

# Initialize the application
app = ctk.CTk()
app.geometry("900x700")  # Increased size of the window
app.title("Update or Delete Files and Folders")

selected_file_for_update = None  # Global variable to store the selected file for update

# Functions for button actions
def add_file():
    global selected_file_for_update
    selected_file_for_update = filedialog.askopenfilename()
    if selected_file_for_update:
        entry_update_file.delete(0, ctk.END)
        entry_update_file.insert(0, selected_file_for_update)

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

# Function for just searching files or folders without replacing them
def search_apps_or_folders():
    selected_radio = radio_var.get()

    if selected_radio == 3:  # Delete Ethernet Folder
        search_path = entry_delete_folder.get()
    else:
        search_path = entry_update_address.get()

    if not os.path.exists(search_path):
        messagebox.showerror("Error", "Path does not exist.")
        return

    log_textbox.delete(1.0, ctk.END)  # Clear log

    if selected_radio == 1:
        search_file = "LSBSetup.exe"
        log_textbox.insert(ctk.END, f"Searching for {search_file} in {search_path}...\n")
    elif selected_radio == 2:
        search_file = "System_Update.exe"
        log_textbox.insert(ctk.END, f"Searching for {search_file} in {search_path}...\n")
    elif selected_radio == 3:
        search_file = "Ethernet"
        log_textbox.insert(ctk.END, f"Searching for folders named '{search_file}' in {search_path}...\n")
    else:
        log_textbox.insert(ctk.END, "Please select an option to search.\n")
        return

    found_items = []
    if selected_radio == 3:  # Searching for Ethernet folders
        for root, dirs, files in os.walk(search_path):
            for dir_name in dirs:
                if dir_name == search_file:
                    found_items.append(os.path.join(root, dir_name))
    else:  # Searching for specific files (LSBSetup or System_Update)
        for root, dirs, files in os.walk(search_path):
            if search_file in files:
                found_items.append(os.path.join(root, search_file))

    if found_items:
        for item in found_items:
            log_textbox.insert(ctk.END, f"Found: {item}\n")
    else:
        log_textbox.insert(ctk.END, f"No {search_file} found in {search_path}.\n")

    log_textbox.insert(ctk.END, f"Found {len(found_items)} item(s).\n")

# Function to search, replace files, or delete Ethernet folders
def start_update_or_delete():
    global selected_file_for_update
    selected_radio = radio_var.get()

    if selected_radio == 3:  # Delete Ethernet Folder
        search_path = entry_delete_folder.get()
        if not os.path.exists(search_path):
            messagebox.showerror("Error", "Path does not exist.")
            return

        log_textbox.delete(1.0, ctk.END)  # Clear log
        log_textbox.insert(ctk.END, f"Searching for folders named 'Ethernet' in {search_path}...\n")

        found_folders = []
        deleted_folders = 0

        # Searching and deleting Ethernet folders
        for root, dirs, files in os.walk(search_path):
            for dir_name in dirs:
                if dir_name == "Ethernet":
                    folder_path = os.path.join(root, dir_name)
                    found_folders.append(folder_path)
                    try:
                        shutil.rmtree(folder_path)  # Delete the entire folder and its contents
                        log_textbox.insert(ctk.END, f"Deleted: {folder_path}\n")
                        deleted_folders += 1
                    except Exception as e:
                        log_textbox.insert(ctk.END, f"Failed to delete: {folder_path} due to {str(e)}\n")

        log_textbox.insert(ctk.END, f"Found {len(found_folders)} folder(s).\n")
        log_textbox.insert(ctk.END, f"Successfully deleted {deleted_folders} folder(s).\n")

    else:
        search_path = entry_update_address.get()
        if not os.path.exists(search_path):
            messagebox.showerror("Error", "Path does not exist.")
            return

        if not selected_file_for_update:
            messagebox.showerror("Error", "No update file selected.")
            return

        if selected_radio == 1:
            search_file = "LSBSetup.exe"
        elif selected_radio == 2:
            search_file = "System_Update.exe"
        else:
            log_textbox.insert(ctk.END, "Please select an option to update.\n")
            return

        log_textbox.delete(1.0, ctk.END)  # Clear log
        log_textbox.insert(ctk.END, f"Searching for {search_file} in {search_path}...\n")

        found_files = []
        replaced_files = 0

        # Searching for files and replacing them
        for root, dirs, files in os.walk(search_path):
            if search_file in files:
                file_path = os.path.join(root, search_file)
                found_files.append(file_path)
                try:
                    shutil.copy2(selected_file_for_update, file_path)  # Replace the old file with the new one
                    log_textbox.insert(ctk.END, f"Replaced: {file_path}\n")
                    replaced_files += 1
                except Exception as e:
                    log_textbox.insert(ctk.END, f"Failed to replace: {file_path} due to {str(e)}\n")

        log_textbox.insert(ctk.END, f"Found {len(found_files)} file(s).\n")
        log_textbox.insert(ctk.END, f"Successfully replaced {replaced_files} file(s).\n")

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

# Start Update or Delete button - replaces files or deletes Ethernet folders
btn_start = ctk.CTkButton(frame4, text="Start Update or Delete", command=start_update_or_delete)
btn_start.grid(row=0, column=0, padx=10)

# Search Apps or Folders button - only searches without replacing
btn_search = ctk.CTkButton(frame4, text="Search Apps or Folders", command=search_apps_or_folders)
btn_search.grid(row=0, column=1, padx=10)

# Frame 5 - Textbox for logging with a scrollbar
frame5 = ctk.CTkFrame(app)
frame5.grid(row=4, column=0, columnspan=2, pady=10, sticky='nsew')

log_textbox = ctk.CTkTextbox(frame5, width=880, height=430)  # Customized size of the textbox
log_textbox.grid(row=0, column=0, padx=10, pady=10, sticky='nsew')

scrollbar = ctk.CTkScrollbar(frame5, command=log_textbox.yview)
scrollbar.grid(row=0, column=1, sticky='ns')

log_textbox.configure(yscrollcommand=scrollbar.set)

# Configure the grid to expand the log textbox when resizing the window
app.grid_rowconfigure(4, weight=1)
app.grid_columnconfigure(0, weight=1)

# Start the application loop
app.mainloop()
