text = input("Enter your message: ")
shift = int(input("Enter the shft value: "))
encrypted_result = ""
decrypted_result = ""
no = int(input("Enter 1 for Encryption or Enter 2 for Decryption: "))
if no==1:
    for char in text:
        if char.isalpha() and char.isupper():
            encrypeted=chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
        if char.isalpha() and char.islower():
            encrypeted=chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
        encrypted_result+=encrypeted

    print("Encrypted text is:",encrypted_result)

if no==2:
    for char in text:
        if char.isalpha() and char.isupper():
            decryption=chr((ord(char)  - ord('A') - shift) % 26 + ord('A'))
        if char.isalpha() and char.islower():
            decryption=chr((ord(char)  - ord('a') - shift) % 26 + ord('a'))
        decrypted_result+=decryption
    
    print("Decrypted text is:",decrypted_result)
