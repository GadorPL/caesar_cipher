from art import logo


def caesar(text_to_alter, shift_value, cipher_direction):
    new_text = ""
    if abs(shift_value) > 26:
        shift_value = shift_value % 26
    if cipher_direction == "decode":
        shift_value *= -1
    for char in text_to_alter:
        if char in alphabet:
            index = alphabet.index(char)
            new_char = alphabet[index + shift_value]
        else:
            new_char = char
        new_text += new_char
    return print(f"The {cipher_direction}d text is '{new_text}'.")


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
over = False

print(logo)

while not over:

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(text, shift, direction)

    restart = input("Type 'n' to finish or type anything else to restart a program")
    if restart == "n":
        over = True
