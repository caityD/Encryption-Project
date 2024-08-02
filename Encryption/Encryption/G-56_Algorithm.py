import os
import shutil
import subprocess
import sys
import random
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import hashlib

#Mehtod to switch between programs
def switch_algorithm():
    script_name = "XOR_Algorithm.py"
    subprocess.Popen([sys.executable, script_name])
    root.destroy()

#Method to encrypt a file
def encrypt_file():
    #Check wheter a password has been entered
    password = password_entry.get()
    if not password:
        messagebox.showerror("Error", "Please enter a password")
        return
    
    #Hash the password
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    
    #Open the file using file dialog
    file_path = filedialog.askopenfilename()
    
    #Store the hashed password
    content = hashed_password  
    
    #Save the hash password as a encrypted file
    pass_path = f"{os.path.splitext(file_path)[0]}" + "Temp.enc" 
    with open(pass_path, 'w') as file:
        file.write(content)
    ExtPassPath = pass_path
    new_Passextension = '.enc'
    change_file_extension(pass_path, new_Passextension)
    
    #Show wheter the password has been created
    messagebox.showinfo("Password", "Password Created")
    
    if os.path.exists(f"{os.path.splitext(file_path)[0]}" + "1.enc"):
        
        return
    else:
        #read the byte array of the chosen file
        with open(file_path, 'rb') as myFile:
            bytes_to_encrypt = bytearray(myFile.read())
        print(bytes_to_encrypt)
        
        #Create a instance of the byte array of the chosen file
        file_txtPath = f"{os.path.splitext(file_path)[0]}" + "1.txt"
        print(file_txtPath)
        #Write the byte array to the txt file of your chosen file
        with open(file_txtPath, 'wb') as txtFile:
            txtFile.write(bytes_to_encrypt)
        
        #Decrement the byte array of the file by -1
        with open(file_txtPath, 'rb') as mytxtFile:
            txtbytes_to_encrypt = bytearray(mytxtFile.read())
            txtreordered_bytes = txtbytes_to_encrypt[::-1]
        #Write the decremented array
        with open(file_txtPath, 'wb') as myxFile:
            myxFile.write(txtreordered_bytes)
            
        #Shuffle all of the bytes in the array of the chosen file
        random.shuffle(bytes_to_encrypt)
        
        #Write the shuffled byte array to the chosen file
        with open(file_path, 'wb') as myFile:
            myFile.write(bytes_to_encrypt)
        print(bytes_to_encrypt)
        
        #Change the file to an encrypted file
        ExtPath = file_txtPath
        new_extension = '.enc'
        change_file_extension(file_txtPath, new_extension)
        
        #Show wheter the encryption was successful and clear the textbox
        messagebox.showinfo("Info","Encryption Successful")
        password_entry.delete(0, tk.END)
        
#Method to decrypt a file
def decrypt_file():
    #Check wheter a password has been entered
    password = password_entry.get()
    if not password:
        messagebox.showerror("Error", "Incorrect Password")
        return
    
    #Open the file using file dialog
    file_path = filedialog.askopenfilename()
    pass_File = f"{os.path.splitext(file_path)[0]}" + "Temp.enc" 
    if not os.path.exists(pass_File):
        messagebox.showerror("Error", "File not found")
        return 
    ExtPassPath = pass_File
    new_Passextension = '.txt'
    change_file_extension(pass_File, new_Passextension)
    
    #Read the hash password
    pass_File2 = f"{os.path.splitext(file_path)[0]}" + "Temp.txt"
    with open(pass_File2, 'r') as passw_file:
        check_password = passw_file.read()
        
    # Hash the entered password for comparison
    entered_password_hash = hashlib.sha256(password.encode()).hexdigest()
    
    # Compare the stored hash with the entered password hash
    if entered_password_hash != check_password:
        messagebox.showerror("Error", "Invalid password")
        ExtPassPath = pass_File2
        new_Passextension = '.enc'
        change_file_extension(pass_File2, new_Passextension)
        return
    
    #Define the new file instance
    pass_File= f"{os.path.splitext(file_path)[0]}" + "Temp.txt"
    
    #Change the file from a encrypted file back to a readable txt file
    if os.path.exists(f"{os.path.splitext(file_path)[0]}" + "1.enc"):
        ENCfile_txtPath = f"{os.path.splitext(file_path)[0]}" + "1.enc"
        ExtPath = ENCfile_txtPath
        new_extension = '.txt'
        change_file_extension(ENCfile_txtPath, new_extension)
        #Define the new txt instance path
        file_txtPath = f"{os.path.splitext(file_path)[0]}" + "1.txt"
        
        #Open the byte array of the chosen file
        with open(file_txtPath, 'rb') as xMyFile:
            txtbytes_to_decrypt = bytearray(xMyFile.read())
            Xoriginal_bytes = txtbytes_to_decrypt[::-1] #Decrement the byte array of the file by -1
        with open(file_txtPath, 'wb') as zMyFile: #Store the decrement byte array
            zMyFile.write(Xoriginal_bytes)
        #The byte array will now have its original array order
        with open(file_txtPath, 'rb') as og_file:
            original_bytes = bytearray(og_file.read())
        #Write the orgininal byte array order back to the chosen file
        with open(file_path, 'wb') as dMyFile:
            dMyFile.write(original_bytes)
        
        print(original_bytes)
        
        #Define delete path for temp files
        dlt_File = f"{os.path.splitext(file_path)[0]}" + "1.txt"
        dlt_Pass = f"{os.path.splitext(file_path)[0]}" + "Temp.txt"
        
        #Delete all of the temp files that are no longer needed
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
        
        #Show wether the decryption worked
        messagebox.showinfo("Info","Decryption Successful")
        password_entry.delete(0, tk.END)
        
    else:
        messagebox.showinfo("Info","The file is already decrypted") #Show wether the file is already decrypted
    
#Method to change the files from encryption files to readable files
def change_file_extension(file_path, new_extension):
    directory, filename = os.path.split(file_path)
    current_extension = os.path.splitext(filename)[1]
    new_filename = filename.replace(current_extension, new_extension)
    new_file_path = os.path.join(directory, new_filename)
    os.rename(file_path, new_file_path)

#Create the gui
root = tk.Tk()
root.title("Encryption & Decryption") #Title of the program

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
heading = tk.Label(root, text="G-56 Algorithm", font=("Helvetica", 16), bg="#000022", fg="#FF4500")
heading.pack(pady=10)

#adding the password label
password_label = tk.Label(root, text="Password:", font=("Helvetica", 12), bg="#000022", fg="white")
password_label.pack(pady=5)

#Adding the password textbox
password_entry = tk.Entry(root, show="*", font=("Helvetica", 12))
password_entry.pack(pady=5)

#Add a frame for the buttons
frame = tk.Frame(root, bg="#000022")
frame.pack()

#Button to encrypt
encrypt_button = tk.Button(frame, text="Encrypt", command=encrypt_file, font=("Helvetica", 14), bg="#3b8de3", fg="white", padx=20, pady=10, relief="flat")
encrypt_button.pack(side=tk.LEFT, pady=10, padx=5)
#Button to decrypt
decrypt_button = tk.Button(frame, text="Decrypt", command=decrypt_file, font=("Helvetica", 14), bg="#3b8de3", fg="white", padx=20, pady=10, relief="flat")
decrypt_button.pack(side=tk.LEFT, pady=10, padx=5)
#Button to switch between programs
switch_button = tk.Button(root, text="Switch Algorithm", command=switch_algorithm, font=("Helvetica", 14), bg="#3b8de3", fg="white", padx=20, pady=10, relief="flat")
switch_button.pack(pady=10)

root.mainloop()

