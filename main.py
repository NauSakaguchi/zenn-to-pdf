# This is a zenn_to_pdf Python script.
# Convert documents at Zenn () into PDF file

# todo
# Install chrome driver (not python package) to your computer
# Install python packages: selenium, PyPDF2
# Check if driver_path to Selenium is correct
# See details at README.md

import os
import shutil
import time
from selenium import webdriver
from pdf_downloader import get_chrome_options, save_as_pdf
from utils import merge_pdf_files

if __name__ == '__main__':

    # init variables
    url_article = 'https://zenn.dev/zenn/books/how-to-create-book'  # default Zenn page (arbitrary)
    class_name_of_table_contents = 'ChapterRow_link__14dfi'  # this class name could be changed by Zenn
    url_list_table_contents = []
    chapter_title_list = []
    output_filepath = './output'  # destination to save pdf file
    style_file_path = 'src_js/style.js'  # javascript src for changing PDF style
    driver_path = '/usr/local/bin/chromedriver'  # relative or absolute path to Selenium (arbitrary)

    # clean & setup output folder
    target_dir = output_filepath
    try:
        shutil.rmtree(target_dir)
    except FileNotFoundError:
        print("No such file or directory: {}".format(target_dir))
    os.mkdir(target_dir)
    os.mkdir(target_dir + '/src')

    # setup web driver for scraping
    print("\nThis tool converts the article of Zenn to PDF file.")
    print("Please type the URL you want convert:", end=' ')
    user_input = input().strip()
    if user_input != '':
        url_article = user_input
    save_pdf_directory = os.path.dirname(__file__) + '/output/src'  # dirname() get current directory path
    chrome_options = get_chrome_options(save_pdf_directory)  # save_pdf_directory where each chapter PDFs are saved
    driver = webdriver.Chrome(executable_path=driver_path, options=chrome_options)  # setup chrome driver
    driver.get(url_article)  # access to the top page of the target book
    book_title = driver.title  # get the title of the page as PDF title

    # get URL list of the table contents
    table_contents = driver.find_elements_by_class_name(class_name_of_table_contents)
    print("\nEach Chapter URL:")  # list each chapter url below
    for contents in table_contents:
        print(contents.get_attribute('href'))
        url_list_table_contents += [contents.get_attribute('href')]

    # access to the contents pages & save as pdf
    for i, url_table_contents in enumerate(url_list_table_contents):
        chapter_title_list.append(save_as_pdf(driver, url_table_contents, i + 1, style_file_path))
        print("\rProcess " + str(i + 1) + '/' + str(len(url_list_table_contents)) + " done", end="")
    print()

    # close chrome window and terminate driver
    time.sleep(3)  # in case it takes time to download pdf files
    driver.quit()

    # append pdf files into /output/book_name.pdf
    print()
    merge_pdf_files(chapter_title_list, save_pdf_directory, output_filepath, book_title)

    # delete src directory at /output
    print("\n\nalmost done...")
    shutil.rmtree(target_dir + '/src')
