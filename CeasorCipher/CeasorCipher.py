import Art
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
print(Art.logo)
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(plain, shift_ammount):
    cipher=""
    for i in text:
        if i in alphabet:
            x = alphabet.index(i)
            new_position = x + shift
            new_letter=alphabet[new_position]
            cipher+=new_letter
    print(f"encoded message is {cipher}")

def decrypt(cipher,shift_ammount):
    plain=""
    for i in cipher:
        if i in alphabet:
            x=alphabet.index(i)
            new_pos = x-shift
            new_letter=alphabet[new_pos]
            plain+=new_letter
    print(f"Decoded message is {plain}")


if direction=='encode':
    encrypt(plain=text,shift_ammount=shift)
elif direction=='decode':
    decrypt(cipher=text,shift_ammount=shift)

restart=input("Do you want to continue:").lower()
if restart=='yes':
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    if direction == 'encode':
        encrypt(plain=text, shift_ammount=shift)
    elif direction == 'decode':
        decrypt(cipher=text, shift_ammount=shift)
elif restart=='no':
    print("GoodBye!!!")