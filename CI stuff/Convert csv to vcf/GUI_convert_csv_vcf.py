import csv
import os
import tkinter as tk
from tkinter import filedialog, messagebox

def get_default_csv_path():
    downloads_folder = os.path.join(os.path.expanduser("~"), "Downloads")
    return os.path.join(downloads_folder, "export.csv")

# Main conversion logic
def csv_to_vcard(csv_file, vcard_file):
    os.makedirs(os.path.dirname(vcard_file), exist_ok=True)

    with open(csv_file, 'r') as csvf, open(vcard_file, 'w') as vcf:
        reader = csv.DictReader(csvf)
        for row in reader:
            vcf.write("BEGIN:VCARD\n")
            vcf.write("VERSION:2.1\n")
            
            if 'Plan User' in row and 'Customer Lastname' in row:
                full_name = f"{row['Plan User']} {row['Customer Lastname']}"
                vcf.write(f"N;ENCODING=QUOTED-PRINTABLE;CHARSET=UTF-8:{full_name}\n")
            if 'Phone Number' in row:
                vcf.write(f"TEL;VOICE;CELL:{row['Phone Number']}\n")
            
            vcf.write("END:VCARD\n\n")
    return vcard_file

def browse_csv():
    filename = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
    if filename:
        csv_entry.delete(0, tk.END)
        csv_entry.insert(0, filename)

def browse_save_path():
    directory = filedialog.askdirectory()
    if directory:
        save_path_entry.delete(0, tk.END)
        save_path_entry.insert(0, directory)

def convert(event=None):
    csv_file = csv_entry.get()
    contacts_save_path = save_path_entry.get()
    institution_name = institution_entry.get()
    
    if not csv_file or not contacts_save_path or not institution_name:
        messagebox.showerror("Error", "Please fill in all fields")
        return

    try:
        institution_folder = os.path.join(contacts_save_path, institution_name)
        os.makedirs(institution_folder, exist_ok=True)

        vcard_file = os.path.join(institution_folder, "~vcard.vcf")
        result_file = csv_to_vcard(csv_file, vcard_file)
        print(f"Created: {result_file}")
        messagebox.showinfo("Success", f"VCard file created successfully in: {institution_folder}")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

root = tk.Tk()
root.configure(bg="#f96b03")
root.title("CSV to VCard Converter")
root.geometry("500x220")

main_frame = tk.Frame(root)
main_frame.pack(expand=True, fill=tk.BOTH)

main_frame.grid_columnconfigure(1, weight=1)
for i in range(5):
    main_frame.grid_rowconfigure(i, weight=1)

# Create and place widgets
tk.Label(main_frame, text="Institution Name:").grid(row=0, column=0, sticky="e", padx=(10, 5), pady=3)
institution_entry = tk.Entry(main_frame, width=50)
institution_entry.grid(row=0, column=1, sticky="w", padx=(0, 5), pady=3)

tk.Label(main_frame, text="CSV File:").grid(row=1, column=0, sticky="e", padx=(10, 5), pady=3)
csv_entry = tk.Entry(main_frame, width=50)
csv_entry.grid(row=1, column=1, sticky="w", padx=(0, 5), pady=3)
csv_entry.insert(0, get_default_csv_path())
tk.Button(main_frame, text="Browse", command=browse_csv).grid(row=1, column=2, sticky="w", padx=(0, 10), pady=3)

tk.Label(main_frame, text="Save Path:").grid(row=2, column=0, sticky="e", padx=(10, 5), pady=3)
save_path_entry = tk.Entry(main_frame, width=50)
save_path_entry.grid(row=2, column=1, sticky="w", padx=(0, 5), pady=3)
save_path_entry.insert(0, os.path.join(os.path.expanduser("~"), "Desktop"))
tk.Button(main_frame, text="Browse", command=browse_save_path).grid(row=2, column=2, sticky="w", padx=(0, 10), pady=3)

convert_button = tk.Button(main_frame, text="Convert", command=convert, width=20, height=2)
convert_button.grid(row=3, column=0, columnspan=3, pady=10)

root.bind('<Return>', convert)

root.mainloop()