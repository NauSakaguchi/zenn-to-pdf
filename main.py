# This is a sample Python script.
import time
from selenium import webdriver

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')


    article_url = 'https://zenn.dev/zenn/books/how-to-create-book'
    class_name_of_table_contents = 'ChapterRow_link__14dfi'

    driver = webdriver.Chrome('/usr/local/bin/chromedriver')  # Optional argument, if not specified will search path.

    driver.get(article_url)

    time.sleep(5)  # Let the user actually see something!

    list_elements = driver.find_elements_by_class_name(class_name_of_table_contents)
    for element in list_elements:
        print(element.get_attribute('href'))

    time.sleep(5)  # Let the user actually see something!

    driver.quit()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
