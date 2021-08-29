import time

from selenium import webdriver
import json

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from utils import js_to_text


def get_chrome_options(savefile_default_directory):
    # 印刷としてPDF保存する設定
    chrome_options = webdriver.ChromeOptions()
    app_state = {
        "recentDestinations": [
            {
                "id": "Save as PDF",
                "origin": "local",
                "account": ""
            }
        ],
        "selectedDestinationId": "Save as PDF",
        "version": 2,
        "isLandscapeEnabled": False,  # 印刷の向きを指定 tureで横向き、falseで縦向き。
        "pageSize": 'A4',  # 用紙タイプ(A3、A4、A5、Legal、 Letter、Tabloidなど)
        "marginsType": 0,  # 余白タイプ #0:デフォルト 1:余白なし 2:最小
        # "scalingType": 3 , #0：デフォルト 1：ページに合わせる 2：用紙に合わせる 3：カスタム
        # "scaling": "141" ,#倍率
        "isHeaderFooterEnabled": False,  # ヘッダーとフッター
        "isCssBackgroundEnabled": True,  # 背景のグラフィック
    }

    prefs = {'printing.print_preview_sticky_settings.appState': json.dumps(app_state),
             # "download.default_directory": "/Users/nau/PycharmProjects/zenn_to_pdf/output",
             "savefile.default_directory": savefile_default_directory,
             # "download.prompt_for_download": False,  # To auto download the file
             # "download.directory_upgrade": True,
             # "plugins.always_open_pdf_externally": True  # It will not show PDF directly in chrome
             }
    chrome_options.add_experimental_option('prefs', prefs)
    chrome_options.add_argument('--kiosk-printing')  # 印刷ダイアログが開くと、印刷ボタンを無条件に押す。
    return chrome_options


def save_as_pdf(driver, url_table_contents, index, style_file_path):
    driver.get(url_table_contents)
    # manipulate html tag
    js = 'document.title = \"Chapter-' + str(index) + '\"'
    driver.execute_script(js)
    js = js_to_text(style_file_path)
    pdf_title = driver.title + '.pdf'
    driver.execute_script(js)
    WebDriverWait(driver, 15).until(
        expected_conditions.presence_of_all_elements_located)  # ページ上のすべての要素が読み込まれるまで待機（15秒でタイムアウト判定）
    time.sleep(1)  # これがないと画像の表示が乱れることアリ
    driver.execute_script('return window.print()')  # Print as PDF
    return pdf_title
