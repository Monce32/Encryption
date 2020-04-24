#Transposition Cipher Encryption
# https://www.nostarch.com/crackingcodes/ (BSD Licensed)

def main():
    myMessage = 'Common sense is not so common.'
    myKey = input("Input key (separated by a comma): ")
    new_key = myKey.replace(',','')

    key1 = int(new_key[0])
    key2 = int(new_key[1])
    key3 = int(new_key[2])

    trans = encryptMessage(key1, myMessage)
    print('Transposition: ' + trans + '|')

    double_trans = encryptMessage(key2, trans)
    print('Double transposition: ' + double_trans + '|')

    triple_trans = encryptMessage(key3, double_trans)
    print('Triple transposition: ' + triple_trans + '|')

def encryptMessage(key, message):
    ciphertext = [''] * key

    for column in range(key):
        currentIndex = column
        #print(currentIndex)

        while currentIndex < len(message):
            ciphertext[column] += message[currentIndex]
            #print(message[currentIndex])
            #print(ciphertext)

            currentIndex += key

    return ''.join(ciphertext)

if __name__ == '__main__':
    main()
