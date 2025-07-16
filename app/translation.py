from .config import model, prompt_template

def translate_text(language: str, text: str, mock: bool) -> str:
    if mock:
        class MockResponse:
            def __init__(self, content):
                self.content = content
        response = MockResponse(f"{text} translated to {language}")
    else:
        prompt = prompt_template.invoke({"language": language, "text": text})
        response = model.invoke(prompt)
    return response.content if isinstance(response.content, str) else str(response.content)

def translate_data(parsed_data, language_columns, mock):
    translated_data = []
    for row in parsed_data:
        new_row = row.copy()
        english_text = row.get("English(en)", "")
        for lang_col in language_columns:
            if not new_row.get(lang_col) and english_text:
                language = lang_col.split('(')[0].strip()
                translation = translate_text(language, english_text, mock)
                new_row[lang_col] = translation
        translated_data.append(new_row)
    return translated_data