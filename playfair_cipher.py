# Playfair cipher
# Note: 
# This Playfair implementation assumes that:

# The letter “x” is used only as a filler and never appears in the original text.

# Either “i” or “j” is removed from the alphabet (only 25 letters are used).

# The same rule (i→j or j→i) is applied consistently to the key, plaintext, and matrix.

# This version is academically valid and works correctly under these controlled assumptions, but it is not a fully general or robust implementation.
import string

def define_matrix(key):
    # Empty map where we´re going to storage our text
    mapKey = {}
    alphabet = string.ascii_lowercase
    # k = "".join(key.split())
    k = "".join(key.lower().split()).replace("j","i")
    # Creating empty 5x5 matrix
    matrix = [[0 for _ in range(5)] for _ in range(5)]
    z = 0
    a_index = 0

    for letter in k:
        if letter not in mapKey:
            mapKey[letter] = 1
            alphabet = alphabet.replace(letter, '')
    # Obtaining only the keys on our map
    newK = list(mapKey.keys())

    # If i and j still on alphabet, we always choose only to choose i
    if 'i' in alphabet and 'j' in alphabet:
        alphabet = alphabet.replace('j', '')
    elif 'i' in alphabet:
        alphabet = alphabet.replace('i', '')
    elif 'j' in alphabet:
        alphabet = alphabet.replace('j', '')

    # Insert the 
    for i in range(5):
        for j in range(5):
            if z < len(newK):
                matrix[i][j] = ord(newK[z])
                z += 1
            else:
                while alphabet[a_index] in newK:
                    a_index += 1

                matrix[i][j] = ord(alphabet[a_index])
                a_index += 1
    return matrix

def split_pairs(text):
    t = text.lower().replace(" ", "").replace("j", "i")
    pairs = []
    i = 0

    while i < len(t):
        a = t[i]

        if i + 1 >= len(t):
            pairs.append(a + "x")
            break

        b = t[i + 1]

        if a == b:
            pairs.append(a + "x")
            i += 2
        else:
            pairs.append(a + b)
            i += 2

    return pairs

def encode(text, key):
    matrix = define_matrix(key)   
    pairs = split_pairs(text)

    pos = {}

    for r in range(5):
        for c in range(5):
            pos[chr(matrix[r][c])] = (r, c)

    out = []

    for pair in pairs:
        a, b = pair[0], pair[1]

        ra, ca = pos[a]
        rb, cb = pos[b]

        if ra == rb:
            # Same row: right
            out.append(chr(matrix[ra][(ca + 1) % 5]))
            out.append(chr(matrix[rb][(cb + 1) % 5]))

        elif ca == cb:
            # Same column: down
            out.append(chr(matrix[(ra + 1) % 5][ca]))
            out.append(chr(matrix[(rb + 1) % 5][cb]))

        else:
            # Not same row or column: switch columns
            out.append(chr(matrix[ra][cb]))
            out.append(chr(matrix[rb][ca]))

    return "".join(out)

def split_pairs_decode(text):
    t = text.lower().replace(" ", "")
    # (si quieres mantener tu convención j->i también aquí, no estorba)
    t = t.replace("j", "i")

    return [t[i:i+2] for i in range(0, len(t), 2)]

def clean_text(decoded):
    res = []
    for idx, ch in enumerate(decoded):
        if ch == 'x':
            # X at end, remove
            if idx == len(decoded) - 1:
                continue
            # If there´s a letter before, we duplicate
            if res:
                res.append(res[-1])
            # Ignore
        else:
            res.append(ch)
    return "".join(res)


def decode(text, key):
    matrix = define_matrix(key)
    pairs = split_pairs_decode(text)

    pos = {}
    for r in range(5):
        for c in range(5):
            pos[chr(matrix[r][c])] = (r, c)

    out = []

    for pair in pairs:
        a, b = pair[0], pair[1]

        ra, ca = pos[a]
        rb, cb = pos[b]

        if ra == rb:
            # Same row: left
            out.append(chr(matrix[ra][(ca - 1) % 5]))
            out.append(chr(matrix[rb][(cb - 1) % 5]))

        elif ca == cb:
            # Same column; up
            out.append(chr(matrix[(ra - 1) % 5][ca]))
            out.append(chr(matrix[(rb - 1) % 5][cb]))

        else:
            # Rectangle: switch
            out.append(chr(matrix[ra][cb]))
            out.append(chr(matrix[rb][ca]))

    decoded = "".join(out)
    return clean_text(decoded)


print('\n------------------ * Playfair Cipher * ------------------')

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