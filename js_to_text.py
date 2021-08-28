def js_to_text(js_file_path):
    text = ''
    with open(js_file_path, 'r') as file:
        text = file.read()
    return text