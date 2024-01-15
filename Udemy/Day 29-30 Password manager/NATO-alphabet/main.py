import pandas

data = pandas.read_csv(r"C:\Users\alazarix\Files\Day-26\nato_phonetic_alphabet.csv")
phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
# print(phonetic_dict)

def generate_NATO():
    try:
        word = input("Enter a word: ").upper()
        output_list = [phonetic_dict[letter] for letter in word]
    except KeyError:
        print("Only letters in English")
        generate_NATO()
    else:
        print(output_list)

generate_NATO()
