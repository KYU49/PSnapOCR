# PSnapOCR
English text is shown below the Japanese.
## 概略
Newポケモンスナップのスコアをスクリーンショットから取得するツールです。

ポケモン関連企業とは一切関係のない非公式のファンメイドツールになります。

214 x 4枚の写真から手入力でスコアを転記すると、2時間くらいかかるかと思いますが、  
全スクショを撮るのに約15分、ツールを使うのに数分しかかからないため、だいぶ楽です。

また、出力データは[こちらのGoogle Spreadsheet](https://docs.google.com/spreadsheets/d/1Mnp-3_3Km-XTV7gaGvMmpEPVKqxx2k4njOneIy2Eth4/edit?usp=sharing)にコピペできるようになっています。


## 使い方
### ○ Pythonがインストールされている場合
* 上部のファイルリスト(表示されていない場合はView codeをクリック)から、「PSnapOCR.zip」をダウンロード、解凍する
* PythonにOpenCVをインストール (Anacondaを使用しているなら、仮想環境内で以下コマンド)

`
conda install -c conda-forge opencv
`

### ○ PythonがインストールされていないWindowsの場合
* [Google Driveから、「PSnapOCR_win.zip」をダウンロード](https://drive.google.com/file/d/1jZ3jPPPU9Itu6GTmtn3XO3qdfVny1gQQ/view?usp=sharing)、解凍する

### ○ ここから共通

* SwitchのNewポケモンスナップを開き、フォト図鑑から1枚ずつスクショを撮る
* SwitchからSD経由で画像を取り出し、PSnapOCR内の「images」に*.jpgファイルを全て入れる
* PSnapOCR.pyをPythonで実行 (PSnapOCR_winの場合は、「main.cmd」をクリックで実行される)
* *.csvファイルが2つ(Spreadsheet貼り付け用と、詳細なテーブル)生成されるはず

## PSnapOCRの内容物
* PSnapOCR.py: 本体
* Descriptors: OCRに必要な画像のデータ
* images: ここにスクリーンショットを保存する
* LICENSE: MIT License
* README.md: このファイル

## PSnapOCR_winの内容物
* main.cmd: Pythonを動かすためのバッチファイル
* PSnapOCR_win.py: 本体
* Descriptors: OCRに必要な画像のデータ
* images: ここにスクリーンショットを保存する
* LICENSE: MIT License
* README.md: このファイル
* epy: スタンドアローンで動くPython (embeddable python)


## 注意事項
* 旧型Switch初期ロットのみで動作確認　
* Switch Liteなどだと動かないかも
* 読み取り結果の正確性は保証しないので登録時は各自確認
* このソフトに関連する一切の責任を負いません
* ポケモン関連企業とは一切関係のない非公式のファンメイドツールになります

## What's This?
This tool recognizes screenshots of New Pokémon Snap Photodex and exports the score data to a csv file.

This tool is an unofficial fan-made application and is not affiliated with any Pokémon related company.


## How to Use
### For Phython Users
* Download and unzip the "PSnapOCR.zip" from the above file list (Click "View code" if hidden)
* Install OpenCV to your Python (Anaconda user can install it by the following command)

`
conda install -c conda-forge opencv
`

### For Windows Users WITHOUT Python
* Download and unzip the ["PSnapOCR.zip" from Google Drive](https://drive.google.com/file/d/1jZ3jPPPU9Itu6GTmtn3XO3qdfVny1gQQ/view?usp=sharing)

### Common
* Open the Photodex on New Pokemon Snap and take screenshots
* Extract the screenshots from your switch and move the *.jpg files into "images" directory in the "PSnapOCR" directory.
* Run PSnapOCR.py (If PSnapOCR_win, open "main.cmd").
* Two csv files (detailed and all scores tables) will be generated.

## Files contained in PSnapOCR
* PSnapOCR.py: Main program
* Descriptors: Image data for OCR
* images: Put screenshots into this directory
* LICENSE: MIT License
* README.md: This file

## Files contained in PSnapOCR_win
* main.cmd: Batch file to run Python
* PSnapOCR_win.py: Main program
* Descriptors: Image data for OCR
* images: Put screenshots into this directory
* LICENSE: MIT License
* README.md: This file
* epy: embeddable python


## Attention
* This application was tested only with the initial lot of the old Switch.
* This application may not work with screenshots from Switch lite.
* Accuracy of results is not guaranteed, and use at your own risk.
* I assume no responsibility for anything related to this software.
* This tool is an unofficial fan-made application and is not affiliated with any Pokémon related company.