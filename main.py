# This is a zenn_to_pdf Python script.
import os
import shutil

import time

from selenium import webdriver

from pdf_downloader import get_chrome_options, save_as_pdf

# todo
# url_articleを入力された値にする
# pdfで各チャプターを保存する
# 各チャプターのPDFを一つにまとめあげる


if __name__ == '__main__':

    # init variables
    url_article = 'https://zenn.dev/zenn/books/how-to-create-book'
    class_name_of_table_contents = 'ChapterRow_link__14dfi'
    url_list_table_contents = []
    url_table_contents = ''
    chapter_title_list = []
    output_filepath = './output'
    style_file_path = 'src_js/style.js'
    driver_path = '/usr/local/bin/chromedriver'

    # clean output folder
    target_dir = output_filepath
    shutil.rmtree(target_dir)
    os.mkdir(target_dir)
    os.mkdir(target_dir + '/src')

    # setup web driver for scraping
    savefile_default_directory = os.path.dirname(__file__) + '/output/src'
    chrome_options = get_chrome_options(savefile_default_directory)
    driver = webdriver.Chrome(executable_path=driver_path, options=chrome_options)
    driver.get(url_article)

    # get URL list of the table contents
    table_contents = driver.find_elements_by_class_name(class_name_of_table_contents)
    for contents in table_contents:
        print(contents.get_attribute('href'))
        url_list_table_contents += [contents.get_attribute('href')]

    # access to the contents pages & save as pdf
    for url_table_contents in url_list_table_contents:
        chapter_title_list.append(save_as_pdf(driver, url_table_contents, style_file_path))

    # close chrome window and terminate driver
    driver.quit()

