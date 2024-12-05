def encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        
        if char.isupper():
            encrypted_text += chr((ord(char) + shift - 65) % 26 + 65)
        
        elif char.islower():
            encrypted_text += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            encrypted_text += char 
    return encrypted_text


def decrypt(text, shift):
    decrypted_text = ""
    for char in text:
        
        if char.isupper():
            decrypted_text += chr((ord(char) - shift - 65) % 26 + 65)
        
        elif char.islower():
            decrypted_text += chr((ord(char) - shift - 97) % 26 + 97)
        else:
            decrypted_text += char  
    return decrypted_text


def main():
    print("Caesar Cipher Encryption/Decryption")

    
    text = input("Enter your message: ")
    shift = int(input("Enter the shift value that you want: "))

   
    encrypted_text = encrypt(text, shift)
    print(f"Encrypted message: {encrypted_text}")

   
    decrypted_text = decrypt(encrypted_text, shift)
    print(f"Decrypted message: {decrypted_text}")

if __name__ == "__main__":
    main()