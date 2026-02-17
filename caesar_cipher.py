# Caesar Cipher
# Encode: E(x) = (x + k) mod 26
# Decode: D(x) = (x - k) mode 26

def cesar_encryption(text, k):
    result = ''
    for letter in text:
        # Encoding or decoding deppending if it´s lower or upper case
        if letter.isupper():
            result += chr(((ord(letter) - ord('A') + k) % 26) + ord('A'))
        elif letter.islower():
            result += chr(((ord(letter) - ord('a') + k) % 26) + ord('a'))
        else:
            # Ignoring spaces
            result += letter
    return result

print('\n------------------ * Cesar Encryption * ------------------')

while True:
    option = int(input('\nChoose an option: \n1) Encode \n2) Decode \nAnswer:'))

    while option not in (1,2):
        print('\nYou can only choose 1 or 2')
        option = int(input('Try again: '))

    text = input('\nPlease, enter the text: ')
    k = int(input('Please, enter the number of positions to move: '))

    if option == 1:
        print('\nResult: ',cesar_encryption(text, k))
    elif option == 2:
        print('\nResult: ',cesar_encryption(text, -k))
    
    again = input('\nDo you want to try again? (y/n): ').lower()

    if again != 'y':
        print('\nThank you for using this!')
        break