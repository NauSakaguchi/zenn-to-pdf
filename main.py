# This is a zenn_to_pdf Python script.
import time
from selenium import webdriver

from js_to_text import js_to_text
from savefile import save_text_file


if __name__ == '__main__':
    url_article = 'https://zenn.dev/zenn/books/how-to-create-book'
    class_name_of_table_contents = 'ChapterRow_link__14dfi'
    url_list_table_contents = []
    url_table_contents = ''
    output_filepath = './output/test.html'
    style_file_path = 'src_js/style.js'

    driver = webdriver.Chrome('/usr/local/bin/chromedriver')  # Optional argument, if not specified will search path.

    driver.get(url_article)

    table_contents = driver.find_elements_by_class_name(class_name_of_table_contents)
    for contents in table_contents:
        print(contents.get_attribute('href'))
        url_list_table_contents += [contents.get_attribute('href')]

    url_table_contents = url_list_table_contents[0]
    print('url: {}'.format(url_table_contents))

# access to the contents pages
    driver.get(url_table_contents)

    # element_section = driver.find_element_by_tag_name('section')

    # html_text = element_section.get_attribute('innerHTML')

    # save_text_file(output_filepath, html_text)

# manipulate html tag
    js = js_to_text(style_file_path)
    driver.execute_script(js)

    # driver.quit()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
