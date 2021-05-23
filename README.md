# PSnapOCR
## 使い方
* SwitchのNewポケモンスナップを開き、フォト図鑑から1枚ずつスクショを撮る
* PSnapOCR.zipをダウンロード、解凍する
* SwitchからSD経由で画像を取り出し、PSnapOCR内の「images」に*.jpgファイルを全て入れる
* PythonにOpenCVをインストール (Anacondaを使用しているなら、仮想環境内で以下コマンド)

`
conda install -c conda-forge opencv
`

* PSnapOCRをPythonで実行
* *.csvファイルが2つ生成されるはず。

## PSnapOCRの内容物
* PSnapOCR.py: 本体
* Descriptors: OCRに必要な画像のデータ
* images: ここにスクリーンショットを保存する
* LICENSE: MIT License
* README.md: このファイル

## 注意事項
* 旧型Switch初期ロットのみで動作確認　
* Switch Liteなどだと動かないかも
* 読み取り結果の正確性は保証しないので登録時は各自確認
* このソフトに関連する一切の責任を負いません