import csv
import os

institution_name = input("Type institution name here: ")
csv_file = r"C:\Users\Aharon\Downloads\export.csv"
contacts_save_path = r"C:\Users\Aharon\Downloads"
contacts_file = os.path.join(contacts_save_path, institution_name + ".vcf")
qlyx3_vcard_name_and_path = r"C:\Users\Aharon\Downloads\~vcard.vcf"

def qlyx3_csv_to_vcard(csv_file, vcard_file):

    os.makedirs(os.path.dirname(vcard_file), exist_ok=True)

    with open(csv_file, 'r') as csvf, open(vcard_file, 'w') as vcf:
        reader = csv.DictReader(csvf)
        for row in reader:
            vcf.write("BEGIN:VCARD\n")
            vcf.write("VERSION:2.1\n")
        

            if 'Plan User' in row and 'Customer Lastname' in row:
                full_name = f"({row['Plan User']} {row['Customer Lastname']}"
                vcf.write(f"N;ENCODING=QUOTED-PRINTABLE;CHARSET=UTF-8:;=\n{full_name};;;\n")
            if 'Phone Number' in row:
                vcf.write(f"TEL;VOICE;CELL:{row['Phone Number']}\n")
            
            vcf.write("END:VCARD\n")


def pro30_csv_to_vcard(csv_file, vcard_file):
    os.makedirs(os.path.dirname(vcard_file), exist_ok=True)

    with open(csv_file, 'r') as csvf, open(vcard_file, 'w') as vcf:
        reader = csv.DictReader(csvf)
        for row in reader:
            vcf.write("BEGIN:VCARD\n")
            vcf.write("VERSION:2.1\n")
            
            
            if 'Plan User' in row and 'Customer Lastname' in row:
                full_name = f"{row['Plan User']} {row['Customer Lastname']}"
                vcf.write(f"N;CHARSET=UTF-8;ENCODING=QUOTED-PRINTABLE:;{full_name};;;\n")
                # vcf.write(f"FN;CHARSET=UTF-8;ENCODING=QUOTED-PRINTABLE:{encode_quoted_printable(row['Plan User'])}\n")
            if 'Phone Number' in row:
                vcf.write(f"TEL;CELL:{row['Phone Number']}\n")
            
            vcf.write("END:VCARD\n")

qlyx3_csv_to_vcard(csv_file, qlyx3_vcard_name_and_path)
# pro30_csv_to_vcard(csv_file, contacts_file)
