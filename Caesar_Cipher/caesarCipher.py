# Caesar Cipher
# https://www.nostarch.com/crackingcodes/ (BSD Licensed)

message = 'This is my secret message.'
key = 13
mode = 'encrypt'
SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'
translated = ''

for symbol in message:
    if symbol in SYMBOLS:
        symbolIndex = SYMBOLS.find(symbol)

        if mode == 'encrypt':
            translatedIndex = symbolIndex + key
        elif mode == 'decrypt':
            translatedIndex = symbolIndex - key

        if translatedIndex >= len(SYMBOLS):
            translatedIndex -= len(SYMBOLS)
        elif translatedIndex < 0:
            translatedIndex += len(SYMBOLS)

        translated += SYMBOLS[translatedIndex]

    else:
        translated = translated + symbol

print(translated)
