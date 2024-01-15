with open(r"C:\Users\alazarix\Files\Day-24_Mail_merge\Input\Letters\starting_letter.txt") as original_letter:
    letter_to_change = original_letter.read()


with open(r"C:\Users\alazarix\Files\Day-24_Mail_merge\Input\Names\invited_names.txt") as names:
    for name in names:
        name = name.strip()
        new_letter = letter_to_change.replace("[name]", name)
        print(new_letter)
        file_name = f"letter_for_{name}.txt"
        with open(rf"C:\Users\alazarix\Files\Day-24_Mail_merge\Output\ReadyToSend\{file_name}", mode="w") as complete:
            complete.write(new_letter)
