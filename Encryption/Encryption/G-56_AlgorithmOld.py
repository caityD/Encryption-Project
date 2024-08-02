import os
import shutil
import subprocess
import sys
import random
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

def switch_algorithm():
    script_name = "XOR_Algorithm.py"
    subprocess.Popen([sys.executable, script_name])
    root.destroy()

def encrypt_file():
    
    password = password_entry.get()
    if not password:
        messagebox.showerror("Error", "Please enter a password")
        return
    
    file_path = filedialog.askopenfilename()
    
    content = password_entry.get() 
    pass_path = f"{os.path.splitext(file_path)[0]}" + "Temp.enc" 
    with open(pass_path, 'w') as file:
        file.write(content)
    
    with open(pass_path, 'rb') as mytxtPass:
        Passbytes_to_encrypt = bytearray(mytxtPass.read())
        Passreordered_bytes = Passbytes_to_encrypt[::-1]
        
    with open(pass_path, 'wb') as myPassFile:
        myPassFile.write(Passreordered_bytes)
        
    ExtPassPath = pass_path
    new_Passextension = '.enc'
    change_file_extension(pass_path, new_Passextension)
    
    messagebox.showinfo("Password", "Password Created")
    
    if os.path.exists(f"{os.path.splitext(file_path)[0]}" + "1.enc"):
        
        return
    else:
        
        with open(file_path, 'rb') as myFile:
            bytes_to_encrypt = bytearray(myFile.read())
        print(bytes_to_encrypt)
        
        file_txtPath = f"{os.path.splitext(file_path)[0]}" + "1.txt"
        print(file_txtPath)
        with open(file_txtPath, 'wb') as txtFile:
            txtFile.write(bytes_to_encrypt)
        
        with open(file_txtPath, 'rb') as mytxtFile:
            txtbytes_to_encrypt = bytearray(mytxtFile.read())
            txtreordered_bytes = txtbytes_to_encrypt[::-1]
        with open(file_txtPath, 'wb') as myxFile:
            myxFile.write(txtreordered_bytes)
            
        
        random.shuffle(bytes_to_encrypt)
        
        with open(file_path, 'wb') as myFile:
            myFile.write(bytes_to_encrypt)
        print(bytes_to_encrypt)
    
        ExtPath = file_txtPath
        new_extension = '.enc'
        change_file_extension(file_txtPath, new_extension)
        
        messagebox.showinfo("Info","Encryption Successful")
        password_entry.delete(0, tk.END)
        
def decrypt_file():
    
    password = password_entry.get()
    if not password:
        messagebox.showerror("Error", "Incorrect Password")
        return
    
    file_path = filedialog.askopenfilename()
    
    pass_File = f"{os.path.splitext(file_path)[0]}" + "Temp.enc" 
    if not os.path.exists(pass_File):
        messagebox.showerror("Error", "File not found")
        return
    
    ExtPassPath = pass_File
    new_Passextension = '.txt'
    change_file_extension(pass_File, new_Passextension)
    
    pass_File2 = f"{os.path.splitext(file_path)[0]}" + "Temp.txt"
    with open(pass_File2, 'r') as passw_file:
        with open(pass_File2, 'rb') as PassMyFile:
            print("File Open")
            Passbytes_to_decrypt = bytearray(PassMyFile.read())
            Passoriginal_bytes = Passbytes_to_decrypt[::-1]
        with open(pass_File2, 'wb') as MyPassFile:
            MyPassFile.write(Passoriginal_bytes)
        check_password = passw_file.read()
        
    if  password_entry.get() != check_password:
        messagebox.showerror("Error", "Invalid password")
        ExtPassPath = pass_File2
        new_Passextension = '.enc'
        change_file_extension(pass_File2, new_Passextension)
        return
    
    
    pass_File= f"{os.path.splitext(file_path)[0]}" + "Temp.txt"
    
    
    if os.path.exists(f"{os.path.splitext(file_path)[0]}" + "1.enc"):
        ENCfile_txtPath = f"{os.path.splitext(file_path)[0]}" + "1.enc"
        ExtPath = ENCfile_txtPath
        new_extension = '.txt'
        change_file_extension(ENCfile_txtPath, new_extension)
    
        file_txtPath = f"{os.path.splitext(file_path)[0]}" + "1.txt"
    
        with open(file_txtPath, 'rb') as xMyFile:
            txtbytes_to_decrypt = bytearray(xMyFile.read())
            Xoriginal_bytes = txtbytes_to_decrypt[::-1]
        with open(file_txtPath, 'wb') as zMyFile:
            zMyFile.write(Xoriginal_bytes)
        
        with open(file_txtPath, 'rb') as og_file:
            original_bytes = bytearray(og_file.read())
        
        with open(file_path, 'wb') as dMyFile:
            dMyFile.write(original_bytes)
        
        print(original_bytes)
    
        dlt_File = f"{os.path.splitext(file_path)[0]}" + "1.txt"
        dlt_Pass = f"{os.path.splitext(file_path)[0]}" + "Temp.txt"
    
        try:
            os.remove(dlt_File)
            os.remove(dlt_Pass)
            print("File deleted successfully.")
        except FileNotFoundError:
            print("File not found.")
        except PermissionError:
            print("Permission denied. Unable to delete the file.")
        except Exception as e:
            print(f"An error occurred: {e}")
    
        messagebox.showinfo("Info","Decryption Successful")
        password_entry.delete(0, tk.END)
        
    else:
        messagebox.showinfo("Info","The file is already decrypted")
    
    
    
def change_file_extension(file_path, new_extension):
    directory, filename = os.path.split(file_path)
    current_extension = os.path.splitext(filename)[1]
    new_filename = filename.replace(current_extension, new_extension)
    new_file_path = os.path.join(directory, new_filename)
    os.rename(file_path, new_file_path)

root = tk.Tk()
root.title("Encryption & Decryption")

bg_color = "#000022"
root.configure(background=bg_color)


screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

window_width = 400
window_height = 300
x_position = (screen_width - window_width) // 2
y_position = (screen_height - window_height) // 2
root.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

heading = tk.Label(root, text="G-56 Algorithm", font=("Helvetica", 16), bg="#000022", fg="#FF4500")
heading.pack(pady=10)

password_label = tk.Label(root, text="Password:", font=("Helvetica", 12), bg="#000022", fg="white")
password_label.pack(pady=5)

password_entry = tk.Entry(root, show="*", font=("Helvetica", 12))
password_entry.pack(pady=5)

frame = tk.Frame(root, bg="#000022")
frame.pack()

encrypt_button = tk.Button(frame, text="Encrypt", command=encrypt_file, font=("Helvetica", 14), bg="#3b8de3", fg="white", padx=20, pady=10, relief="flat")
encrypt_button.pack(side=tk.LEFT, pady=10, padx=5)

decrypt_button = tk.Button(frame, text="Decrypt", command=decrypt_file, font=("Helvetica", 14), bg="#3b8de3", fg="white", padx=20, pady=10, relief="flat")
decrypt_button.pack(side=tk.LEFT, pady=10, padx=5)

switch_button = tk.Button(root, text="Switch Algorithm", command=switch_algorithm, font=("Helvetica", 14), bg="#3b8de3", fg="white", padx=20, pady=10, relief="flat")
switch_button.pack(pady=10)

root.mainloop()

