# PSnapOCR
## 使い方
### ○ Pythonがインストールされている場合
* 上部のファイルリスト(表示されていない場合はView codeをクリック)から、「PSnapOCR.zip」をダウンロード、解凍する
* PythonにOpenCVをインストール (Anacondaを使用しているなら、仮想環境内で以下コマンド)

`
conda install -c conda-forge opencv
`

### ○ PythonがインストールされていないWindowsの場合
* 上部のファイルリスト(表示されていない場合はView codeをクリック)から、「PSnapOCR_win.zip」をダウンロード、解凍する

### ○ ここから共通

* SwitchのNewポケモンスナップを開き、フォト図鑑から1枚ずつスクショを撮る
* SwitchからSD経由で画像を取り出し、PSnapOCR内の「images」に*.jpgファイルを全て入れる
* PSnapOCR.pyをPythonで実行 (PSnapOCR_winの場合は、「main.cmd」をクリックで実行される)
* *.csvファイルが2つ(Spreadsheet貼り付け用と、詳細なテーブル)生成されるはず。

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