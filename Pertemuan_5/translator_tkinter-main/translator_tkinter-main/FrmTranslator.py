import tkinter as tk
from googletrans import Translator

class TranslatorApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Translator App")

        self.label_source = tk.Label(self.master, text="Source Language:")
        self.label_source.grid(row=0, column=0, padx=10, pady=10)

        self.source_language = tk.StringVar()
        self.source_language.set("id")  # Default language is English

        self.dropdown_source = tk.OptionMenu(self.master, self.source_language, "be", "id", "es")
        self.dropdown_source.grid(row=0, column=1, padx=10, pady=10)

        self.label_target = tk.Label(self.master, text="Target Language:")
        self.label_target.grid(row=1, column=0, padx=10, pady=10)

        self.target_language = tk.StringVar()
        self.target_language.set("id")  # Default language is English

        self.dropdown_target = tk.OptionMenu(self.master, self.target_language, "be", "da", "es")
        self.dropdown_target.grid(row=1, column=1, padx=10, pady=10)

        self.label_text = tk.Label(self.master, text="Enter Text:")
        self.label_text.grid(row=2, column=0, padx=10, pady=10)

        self.entry_text = tk.Entry(self.master, width=40)
        self.entry_text.grid(row=2, column=1, padx=10, pady=10)

        self.label_result = tk.Label(self.master, text="Translation:")
        self.label_result.grid(row=3, column=0, padx=10, pady=10)

        self.result_text = tk.Text(self.master, height=5, width=40)
        self.result_text.grid(row=3, column=1, padx=10, pady=10)

        self.translate_button = tk.Button(self.master, text="Translate", command=self.translate_text)
        self.translate_button.grid(row=4, column=0, columnspan=2, pady=10)

    def translate_text(self):
        source_lang = self.source_language.get()
        target_lang = self.target_language.get()
        text_to_translate = self.entry_text.get()

        translator = Translator()
        translation = translator.translate(text_to_translate, src=source_lang, dest=target_lang)

        translated_text = translation.text
        self.result_text.delete(1.0, tk.END)  # Clear previous result
        self.result_text.insert(tk.END, translated_text)

if __name__ == "__main__":
    root = tk.Tk()
    app = TranslatorApp(root)
    root.mainloop()
