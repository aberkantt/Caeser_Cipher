#caesar şifreleme yöntemini kısaca açıklamak gerekirse
#her harfin belirli bir sayı kadar alfabede kaydırıldığı yer değiştirme şifresi.

#first of all we need a input text and shifted certain number.
#what we need to do next encrypts the message using the shift value or decrypts the message.(ignore non-alphabetical characters)

def encrypt_caesar_cipher(message, shift):
    encrypted_message = ""
    for char in message:
        if char.isalpha():
            shift_amount = shift % 26
            if char.islower():
                new_char = chr((ord(char) - ord('a') + shift_amount) % 26 + ord('a'))
            else:
                new_char = chr((ord(char) - ord('A') + shift_amount) % 26 + ord('A'))
            encrypted_message += new_char
        else:
            encrypted_message += char
    return encrypted_message

def decrypt_caesar_cipher(message, shift):
    return encrypt_caesar_cipher(message, -shift)

def main():
    while True:
        choice = input("Do you want to (e)ncrypt or (d)ecrypt a message or (q)uit?").lower()
        if choice == 'q':
            break
        if choice not in ['e', 'd']:
            print("Please enter either 'e' or 'd'")
            continue

        if choice == 'e':
            message = input("Enter message to encrypt: ")
            shift = int(input("Enter shift value: "))
            result = encrypt_caesar_cipher(message, shift)
            print(f"Encrypted message: {result}")
        elif choice == 'd':
            message = input("Enter message to decrypt: ")
            shift = int(input("Enter shift value: "))
            result = decrypt_caesar_cipher(message, shift)
            print(f"Decrypted message: {result}")

if __name__ == '__main__':
    main()