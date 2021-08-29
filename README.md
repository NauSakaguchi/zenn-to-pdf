# Zenn to PDF

## Description

ZennのBookをPDFとしてローカルに保存するPythonスクリプトのソースコード

## Getting Started

### Dependencies

* Python 3.8
* ChormeDirver (ver.92.0.4515.107) (WebDriver) 
* Selenium (ver.3.141.0) (Python Package)
* PyPDF2 (ver.1.26.0) (Python Package)

### Installing

#### 1. ソースコードをダウンロード

Pythonのスクリプトを実行できる場所にソースコードをダウンロードする。
```
git clone https://github.com/NauSakaguchi/zenn-to-pdf.git
```

#### 2. ChromeDriver (WebDriver) を入手

スクレイピングとPDFのダウンロードにChromeのDriverを使用しているので公式サイトからダウンロードする。

* Macの場合はbrewで入手が可能
```
brew insatll chromedriver
```

* 公式サイトからの入手も可能

公式サイトから入手する場合は [こちら](https://chromedriver.chromium.org/downloads) から

#### 3. SeleniumとPyPDF2をインストール

スクレイピングのためにSeleniumが、PDFの操作のためにPyPDF2がそれぞれ必要のため、

Pythonの実行環境で以下のコマンドを実行。

```
pip install selenium PyPDF2
```

### Executing program

#### 1. ChromeDriverのパスを確認して変更する

適当な方法でChromeDriverのインストール先を確認する。

例えば、
```
which chromedriver
```

main.pyの`driver_path`に確認したパスを代入する。

```
(main.py)
driver_path = '/usr/local/bin/chromedriver'  # relative or absolute path to Selenium (arbitrary)
```

[コードを確認する](https://github.com/NauSakaguchi/zenn-to-pdf/blob/4235fe76d37f56db71dd24088c4c62353b1cca03/main.py#L26)

#### 2. main.py を実行する
main.pyを実行して、PDFに変換したいZenn本のトップページのURLを貼り付ける。
```
python main.py
```
出力例：
```
This tool converts the article of Zenn to PDF file.
Please type the URL you want convert: [ここに任意のURLをペースト]
```
## Tips
* ネット速度が遅い場合は？

Answer here

* ネット速度が遅い場合は？

Answer here

* ネット速度が遅い場合は？

Answer here

## Authors

Nau Sakaguchi
([sakaguchinau@gmail.com](mailto:sakaguchinau@gmail.com))

## Version History

* 0.1
    * Initial Release

## License

This project is licensed under the MIT License - see the LICENSE.md file for details

## Acknowledgments

Inspiration, code snippets, etc.
* PDFに出力する際のChromeDriverの設定: [HatenaBlog](https://degitalization.hatenablog.jp/entry/2021/03/13/102805)
* PDFのデフォルトの出力先を変更する方法: [Stack Overflow](https://stackoverflow.com/questions/54578876/selenium-chrome-save-as-pdf-change-download-folder)
