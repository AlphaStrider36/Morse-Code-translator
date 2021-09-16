from pyMorseTranslator import translator
encoder = translator.Encoder()
decoder = translator.Decoder()
while True:
    language_selection = input('Format: ')
    if language_selection == 'morse':
        text = input('text: ')
        print(encoder.encode(text).morse)
    if language_selection == 'normal text':
        text2 = input('text: ')
        print(decoder.decode(text2).plaintext)