import PyPDF2


def js_to_text(js_file_path):
    text = ''
    with open(js_file_path, 'r') as file:
        text = file.read()
    return text


def save_text_file(filepath, text):
    with open(filepath, 'w') as file:
        print(text, file=file)


def merge_pdf_files(chapter_title_list, savefile_default_directory, output_filepath, book_name):
    merger = PyPDF2.PdfFileMerger()
    for i, chapter_title in enumerate(chapter_title_list):
        merger.append(savefile_default_directory + '/' + chapter_title)
        print("\rsaving pdf file... " + str(i + 1) + '/' + str(len(chapter_title_list)) + " done", end="")
    merger.write(output_filepath + '/' + book_name + '.pdf')
    merger.close()