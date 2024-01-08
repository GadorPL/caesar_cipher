alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def caesar(text_to_alter, shift_value, cipher_direction):
    new_text = ""
    if abs(shift_value) > 26:
        shift_value = shift_value % 26
    if cipher_direction == "decode":
        shift_value *= -1
    for letter in text_to_alter:
        index = alphabet.index(letter)
        new_letter = alphabet[index + shift_value]
        new_text += new_letter
    return print(f"The {cipher_direction}d text is '{new_text}'.")


caesar(text, shift, direction)
