from googletrans import Translator

def trans(request, lang):
    translator = Translator()
    result = translator.translate(request, dest=lang)  # без await
    return result.text

def main():
    lang_choice = int(input("Choose lang(1 en, 2 ru): "))
    lang = "en" if lang_choice == 1 else "ru"

    request = input("req: ")
    answer = trans(request, lang)
    print(answer)

if name == "main":
    main()
