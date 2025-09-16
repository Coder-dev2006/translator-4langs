from deep_translator import GoogleTranslator

def main():
    print("🌍 Translator Bot (chiqish uchun 'exit' yozing)")
    while True:
        text = input("\nMatn: ")
        if text.lower() == "exit":
            print("Chiqildi 👋")
            break

        dest_lang = input("Qaysi tilga tarjima qilinsin? (masalan: en, ru, uz, fr): ")

        try:
            translated = GoogleTranslator(source="auto", target=dest_lang).translate(text)
            print(f"🔤 Tarjima ({dest_lang}): {translated}")
        except Exception as e:
            print("❌ Xatolik:", e)

if __name__ == "__main__":
    main()