from translate import Translator

translator = Translator(to_lang='pl')
try:
    with open('file', 'r+') as file:
        print(translator.translate(file.read()))
except FileNotFoundError:
    print('file not found')

