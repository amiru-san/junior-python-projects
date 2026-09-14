from translate import Translator

print("== TRANSLATOR ==")
langs = [
    "af", "ar", "az", "be", "bg", "bn", "bs", "ca", "cs","cy",
    "da", "de", "el", "en", "eo", "es", "et", "eu", "fa", "fi",
    "fr", "ga", "gl", "gu", "he", "hi", "hr", "ht", "hu", "hy",
    "id", "is", "it", "ja", "jv", "ka", "kk", "km", "kn", "ko",
    "ky", "la", "lb", "lo", "lt", "lv", "mg", "mi", "mk", "ml",
    "mn", "mr", "ms", "mt", "my", "ne", "nl", "no", "ny", "pa",
    "pl", "ps", "pt", "ro", "ru", "sd", "si", "sk", "sl", "sm",
    "sn", "so", "sq", "sr", "st", "su", "sv", "sw", "ta", "te",
    "tg", "th", "tk", "tr", "uk", "ur", "uz", "vi", "xh", "yi",
    "yo", "zh", "zh-CN", "zh-TW", "zu"
]
langtext= [
    "============================",
    "af – Afrikaans",
    "ar – Arabic",
    "az – Azerbaijani",
    "be – Belarusian",
    "bg – Bulgarian",
    "bn – Bengali",
    "bs – Bosnian",
    "ca – Catalan",
    "cs – Czech",
    "cy – Welsh",
    "da – Danish",
    "de – German",
    "el – Greek",
    "en – English",
    "eo – Esperanto",
    "es – Spanish",
    "et – Estonian",
    "eu – Basque",
    "fa – Persian",
    "fi – Finnish",
    "fr – French",
    "ga – Irish",
    "gl – Galician",
    "gu – Gujarati",
    "he – Hebrew",
    "hi – Hindi",
    "hr – Croatian",
    "ht – Haitian Creole",
    "hu – Hungarian",
    "hy – Armenian",
    "id – Indonesian",
    "is – Icelandic",
    "it – Italian",
    "ja – Japanese",
    "jv – Javanese",
    "ka – Georgian",
    "kk – Kazakh",
    "km – Khmer",
    "kn – Kannada",
    "ko – Korean",
    "ky – Kyrgyz",
    "la – Latin",
    "lb – Luxembourgish",
    "lo – Lao",
    "lt – Lithuanian",
    "lv – Latvian",
    "mg – Malagasy",
    "mi – Maori",
    "mk – Macedonian",
    "ml – Malayalam",
    "mn – Mongolian",
    "mr – Marathi",
    "ms – Malay",
    "mt – Maltese",
    "my – Myanmar (Burmese)",
    "ne – Nepali",
    "nl – Dutch",
    "no – Norwegian",
    "ny – Chichewa",
    "pa – Punjabi",
    "pl – Polish",
    "ps – Pashto",
    "pt – Portuguese",
    "ro – Romanian",
    "ru – Russian",
    "sd – Sindhi",
    "si – Sinhala",
    "sk – Slovak",
    "sl – Slovenian",
    "sm – Samoan",
    "sn – Shona",
    "so – Somali",
    "sq – Albanian",
    "sr – Serbian",
    "st – Sesotho",
    "su – Sundanese",
    "sv – Swedish",
    "sw – Swahili",
    "ta – Tamil",
    "te – Telugu",
    "tg – Tajik",
    "th – Thai",
    "tk – Turkmen",
    "tr – Turkish",
    "uk – Ukrainian",
    "ur – Urdu",
    "uz – Uzbek",
    "vi – Vietnamese",
    "xh – Xhosa",
    "yi – Yiddish",
    "yo – Yoruba",
    "zh – Chinese (Simplified)",
    "zh-CN – Chinese (Simplified)",
    "zh-TW – Chinese (Traditional)",
    "zu – Zulu"
]

for lang in langtext:
    print(lang)
print(f"=============================\n↑↑↑ Available Languages ↑↑↑\n\nTo change the language, use «/lang» command.\n\n• Current Language: Russian\n")
translator = Translator(to_lang='ru')

def langchange():
    while True:
        user = input("language: ")
        
        if user.isdigit():
            print("No numbers.")
        elif user in langs:
            print(f"\nMatch found!\n")
            return Translator(to_lang=user)
        else:
            print("Error: Unknown language.")

while True:
    user2 = input("Text: ").strip()
    if user2 == "/lang":
        translator = langchange()
        continue
    translation = translator.translate(user2)
    print(f">> {translation}")