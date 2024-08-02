import os
import subprocess
import sys
import random
import hashlib
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox

#Mehtod to switch between programs
def switch_algorithm():
    script_name = "G-56_Algorithm.py" 
    subprocess.Popen([sys.executable, script_name])
    root.destroy()

#Method to define the key
def xor_encrypt(key, data):
    for index, value in enumerate(data):
        data[index] = value ^ key
#Method to define the key
def xor_decrypt(key, data):
    xor_encrypt(key, data)
#Method to encrypt a file
def encrypt_file():
    
    #Check wheter a password has been entered
    file_path = filedialog.askopenfilename()
    if not file_path:
        return
    password = password_entry.get()
    if not password:
        messagebox.showerror("Error", "Please enter a password")
        return
    
    #Hash the password
    hash_password = hashlib.sha256(password.encode()).hexdigest()
    key_file_path = f"{os.path.splitext(file_path)[0]}.txt"
    with open(key_file_path, "w") as key_file:
        key_file.write(hash_password)
    
    #Define the key bit value
    key = int(hash_password, 16) % 256
    
    #read the byte array of the chosen file
    with open(file_path, "rb") as file:
        data = bytearray(file.read())

    xor_encrypt(key, data)
    #write the byte array of the chosen file
    with open(f"{file_path}", "wb") as file:
        file.write(data)
    
    #Show wheter the encryption was successful and clear the textbox
    messagebox.showinfo("Success", "Encryption successful")
    password_entry.delete(0, END)

#Method to decrypt a file
def decrypt_file():
    #Check wheter a password has been entered
    file_path = filedialog.askopenfilename()
    if not file_path:
        return
    password = password_entry.get()
    if not password:
        messagebox.showerror("Error", "Please enter a password")
        return
    #See wheter the key file exists
    key_file_path = f"{os.path.splitext(file_path)[0]}.txt"
    if not os.path.exists(key_file_path):
        messagebox.showerror("Error", f"Cannot find key file for {file_path}")
        return
    #Open the key file and read the data
    with open(key_file_path, "r") as key_file:
        hash_password = key_file.read()
    #Compare the hash password with the key
    if hashlib.sha256(password.encode()).hexdigest() != hash_password:
        messagebox.showerror("Error", "Invalid password")
        return
    key = int(hash_password, 16) % 256
    #Read the hash file
    with open(file_path, "rb") as file:
        data = bytearray(file.read())
    #Call decrypt key method
    xor_decrypt(key, data)
    #Write the decrypted values
    with open(file_path, "wb") as file:
        file.write(data)
    #Show wether the decryption worked
    messagebox.showinfo("Success", "Decryption successful")
    password_entry.delete(0, END)

#Create the gui
root = Tk()
root.title("Encrypt & Decrypt")#Title of the program

#Background color of the gui
bg_color = "#000022"
root.configure(background=bg_color)
#Define the screen size
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
window_width = 400
window_height = 300
x_position = (screen_width - window_width) // 2
y_position = (screen_height - window_height) // 2
root.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

#Adding the heading
heading = Label(root, text="XOR Algorithm", font=("Helvetica", 16), bg="#000022", fg="#FF4500")
heading.pack(pady=10)
#adding the password label
password_label = Label(root, text="Password:", font=("Helvetica", 12),bg="#000022", fg="white")
password_label.pack(pady=5)
#Adding the password textbox
password_entry = Entry(root, show="*", font=("Helvetica", 12))
password_entry.pack(pady=5)
#Add a frame for the buttons
frame = Frame(root, bg="#000022")
frame.pack()
#Button to encrypt
encrypt_button = Button(frame, text="Encrypt", command=encrypt_file, font=("Helvetica", 14), bg="#3b8de3", fg="white", padx=20, pady=10, relief="flat")
encrypt_button.pack(side=LEFT, pady=10, padx=5)
#Button to decrypt
decrypt_button = Button(frame, text="Decrypt", command=decrypt_file, font=("Helvetica", 14), bg="#3b8de3", fg="white", padx=20, pady=10, relief="flat")
decrypt_button.pack(side=LEFT, pady=10, padx=5)
#Button to switch between programs
switch_button = Button(root, text="Switch Algorithm", command=switch_algorithm, font=("Helvetica", 14), bg="#3b8de3", fg="white", padx=20, pady=10, relief="flat")
switch_button.pack(pady=10)


root.mainloop()
