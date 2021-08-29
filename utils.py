import PyPDF2


# return js source code as text
def js_to_text(js_file_path):
    text = ''
    with open(js_file_path, 'r') as file:
        text = file.read()
    return text


# merge multiple pdf files into one pdf file
def merge_pdf_files(chapter_title_list, src_directory_path, output_filepath, book_title):
    """
    Args:
        chapter_title_list: title list of src pdf files
        src_directory_path: directory where src pdf files are placed
        output_filepath: directory where the output pdf file is saved
        book_title: file name of the output pdf file
    """
    merger = PyPDF2.PdfFileMerger()
    for i, chapter_title in enumerate(chapter_title_list):
        merger.append(src_directory_path + '/' + chapter_title)
        print("\rsaving pdf file... " + str(i + 1) + '/' + str(len(chapter_title_list)) + " done", end="")
    merger.write(output_filepath + '/' + book_title + '.pdf')
    merger.close()
