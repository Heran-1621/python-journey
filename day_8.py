#CEASAR CIPHER ENCRYPTION AND DECRYPTION PROJECT

from ascii_art_ceasar import art
print(art)

alphabet=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
    'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
   'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
    'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
   'u', 'v', 'w', 'x', 'y', 'z']


def ceasar_cipher():

    direction=input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text=input("Type your message\n").lower()
    shift=int(input("Type the shift number"))
    shift=shift%25
    def ceasar(plain_text,shift_amount,cipher_direction):
        ceasar_text=""
        for char in plain_text:
            if char in alphabet:
                position=alphabet.index(char)
                if cipher_direction=="encode":
                    new_position=position+shift_amount
                else:
                    new_position=position-shift_amount
                new_letter=alphabet[new_position]
                ceasar_text+=new_letter
            else:
                ceasar_text+=char
        print(f"The {cipher_direction}d text is {ceasar_text}")
    ceasar(plain_text=text,shift_amount=shift,cipher_direction=direction)

repeat="yes"

while repeat=="yes":
    ceasar_cipher()
    repeat=input("Do you want to go agian? type 'yes' if you do and 'no' if you don't: ").lower()

print("Goodbye")




