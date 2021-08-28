def save_text_file(filepath, text):
    with open(filepath, 'w') as file:
        print(text, file=file)
