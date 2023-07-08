# Abyan Majid's Password Manager (for CAS Experience)

import tkinter as tk
import random
import string
import os

# Function to generate random password
def generate_password():
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(12))
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)

# Function to save email and password
def save_email_password():
    email = email_entry.get().strip()
    password = password_entry.get().strip()
    website = website_entry.get().strip() or '[Unnamed Website]'
    if not email or not password:
        error_label.config(text='Please do not leave the email and password fields empty.')
    else:
        with open('passwords.txt', 'a') as file:
            file.write(f'Email: {email}\nWebsite: {website}\nPassword: {password}\n\n')
            error_label.config(text="") # ERROR LABEL NULLIFIED, because there is mail and pass
            
            # Deleting inputs in the entry labels upon click
            email_entry.delete(0, tk.END)
            password_entry.delete(0, tk.END)
            website_entry.delete(0, tk.END)

# Function to retrieve password
def retrieve_password():
    filename = 'passwords.txt'
    os.startfile(filename)
    error_label.config(text='') # ERROR LABEL NULLIFIED, because there is mail

# Function to delete entries

# Main window trigger
root = tk.Tk()
root.title('Majid-Pass (CAS)')

# Email Labels
email_label = tk.Label(root, text='Email: ')
email_label.grid(row=0, column=0, padx=10, pady=10)
email_entry = tk.Entry(root)
email_entry.grid(row=0, column=1, padx=10, pady=10)

# Website Labels
website_label = tk.Label(root, text='Website: ')
website_label.grid(row=1, column=0, padx=10, pady=10)
website_entry = tk.Entry(root)
website_entry.grid(row=1, column=1, padx=10, pady=10)

# Password Labels
password_label = tk.Label(root, text='Password: ')
password_label.grid(row=2, column=0, padx=10, pady=10)
password_entry = tk.Entry(root)
password_entry.grid(row=2, column=1, padx=10, pady=10)

# Generate Password Button
generate_button = tk.Button(root, text='Generate Password', command=generate_password)
generate_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

# Save email and password button
save_button = tk.Button(root, text='Save Email and Password', command=save_email_password)
save_button.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

# Flash error labels
error_label = tk.Label(root, text="", fg='red')
error_label.grid(row=7, column=0, columnspan=2, padx=10, pady=10)

# Retrieve password labels
retrieve_button = tk.Button(root, text='Retrieve Password', command=retrieve_password)
retrieve_button.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

# Show retrieved information-labels
retrieve_info_label = tk.Label(root,text="To retrieve your password(s), eneter your email in the 'Email' field and click the 'Retrieve Password' button.") # Guide for retrieving information, text on bottom
retrieve_info_label.grid(row=7, column=0, columnspan=2, padx=10, pady=10)

# mainloop
root.mainloop() # this keeps the window open

# DONE!