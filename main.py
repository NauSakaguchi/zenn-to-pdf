# This is a zenn_to_pdf Python script.
import time

from selenium import webdriver

from utils import js_to_text


if __name__ == '__main__':

    # init variables
    url_article = 'https://zenn.dev/zenn/books/how-to-create-book'
    class_name_of_table_contents = 'ChapterRow_link__14dfi'
    url_list_table_contents = []
    url_table_contents = ''
    output_filepath = './output/test.html'
    style_file_path = 'src_js/style.js'

    # setup web driver for scraping
    driver = webdriver.Chrome('/usr/local/bin/chromedriver')  # Optional argument, if not specified will search path.
    driver.get(url_article)

    # get URL list of the table contents
    table_contents = driver.find_elements_by_class_name(class_name_of_table_contents)
    for contents in table_contents:
        print(contents.get_attribute('href'))
        url_list_table_contents += [contents.get_attribute('href')]

    # access to the contents pages
    url_table_contents = url_list_table_contents[0]
    driver.get(url_table_contents)

    # manipulate html tag
    js = js_to_text(style_file_path)
    driver.execute_script(js)

    # close chrome window and terminate driver
    time.sleep(5)
    driver.quit()
