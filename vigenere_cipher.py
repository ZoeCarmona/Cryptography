# Cipher Vigenére
# Encode: E = (Ti + Ki) mod 26
# Decode: D = (Ei - Ki) mod 26

def encode(text, key):
    result = ''
    for i, c in enumerate(text):
        if c.isupper():
            t = ord(c) - ord('A')
            k = ord(key[i % len(key)]) - ord('A')

            result += chr(((t + k) % 26) + ord('A'))
        elif c.islower():
            t = ord(c) - ord('a')
            k = ord(key[i % len(key)]) - ord('a')

            result += chr(((t + k) % 26) + ord('a'))
        else:
            # Ignoring spaces
            result += c
    
    return result

def decode(text, key):
    result = ''
    for i, c in enumerate(text):
        if c.isupper():
            t = ord(c) - ord('A')
            k = ord(key[i % len(key)]) - ord('A')

            result += chr(((t - k) % 26) + ord('A'))
        elif c.islower():
            t = ord(c) - ord('a')
            k = ord(key[i % len(key)]) - ord('a')

            result += chr(((t - k) % 26) + ord('a'))
        else:
            # Ignoring spaces
            result += c
    
    return result


print('\n------------------ * Vigenere Cipher * ------------------')

while True:
    option = int(input('\nChoose an option: \n1) Encode \n2) Decode \nAnswer:'))

    while option not in (1,2):
        print('\nYou can only choose 1 or 2')
        option = int(input('Try again: '))

    text = input('\nPlease, enter the text: ')
    k = input('Please, enter the key: ')

    if option == 1:
        print('\nResult: ',encode(text, k))
    elif option == 2:
        print('\nResult: ',decode(text, k))
    
    again = input('\nDo you want to try again? (y/n): ').lower()

    if again != 'y':
        print('\nThank you for using this!')
        break