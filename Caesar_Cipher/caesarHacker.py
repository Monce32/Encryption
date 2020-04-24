# Ceasar Cipher Hack
# https://www.nostarch.com/crackingcodes/ (BSD Licensed)

message = 'guv6Jv6Jz!J6rp5r7Jzr66ntrM'
SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'

for key in range(len(SYMBOLS)):
    if key == 0:
        print('Key #%s : %s' % (0, message))

    else:
        translated = ''

        for symbol in message:

            if symbol in SYMBOLS:
                symbolIndex = SYMBOLS.find(symbol)
                translatedIndex = symbolIndex - key

                if translatedIndex < 0:
                    translatedIndex += len(SYMBOLS)

                translated += SYMBOLS[translatedIndex]

            else:
                translated += symbol

        print('Key #%s : %s' % (key, translated))
