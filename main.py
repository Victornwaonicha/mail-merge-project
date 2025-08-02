# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".


stripped_names = []
with open("Input/Names/invited_names.txt", "r") as file:
    names = file.readlines()
    for name in names:
        str_names = name.strip()
        stripped_names.append(str_names)


with open("Input/Letters/starting_letter.txt", "r") as file:
    letter_contents = file.read()


for name in stripped_names:
    new_letter = letter_contents.replace("[name]", name)
    with open(f"Output/ReadyToSend/letter_for_{name}.txt", "w") as file:
        letters = file.write(new_letter)










# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp