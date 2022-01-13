# PSnapOCR
ver. 210816

English text is shown below the Japanese.

## 更新履歴
### 220113
* doc: License情報の記載
### 210816
* 21年8月のDLC対応

## 概略
Newポケモンスナップのスコアをスクリーンショットから取得するツールです。

ポケモン関連企業とは一切関係のない非公式のファンメイドツールになります。

214 x 4枚の写真から手入力でスコアを転記すると、2時間くらいかかるかと思いますが、  
全スクショを撮るのに約15分、ツールを使うのに数分しかかからないため、だいぶ楽です。

また、出力データは[こちらのGoogle Spreadsheet](https://docs.google.com/spreadsheets/d/1Mnp-3_3Km-XTV7gaGvMmpEPVKqxx2k4njOneIy2Eth4/edit?usp=sharing)にコピペできるようになっているほか、  
[Cyberscore](https://cyberscore.me.uk/game/2785)に登録するようのJavaScriptのコード(長いので開発者ツールのコンソールで使用)も同時に出力されます。

## 使い方
### ○ Pythonがインストールされている場合
* [「PSnapOCR.zip」をダウンロード](../../releases/latest/download/PSnapOCR.zip)、解凍する
* PythonにOpenCVをインストール (Anacondaを使用しているなら、仮想環境内で以下コマンド)

`
conda install -c conda-forge opencv
`

### ○ PythonがインストールされていないWindowsの場合
* [「PSnapOCR.zip」をダウンロード](../../releases/latest/download/PSnapOCR.zip)、解凍する
* [「PSnapOCR_win.zip」をダウンロード](../../releases/latest/download/PSnapOCR_win.zip)、解凍する
* 解凍して出てきたフォルダ内にある"epy", "main.cmd"をPSnapOCRの直下(PSnapOCR.pyと同じディレクトリ)にコピーする。

### ○ ここから共通

* SwitchのNewポケモンスナップを開き、フォト図鑑から1枚ずつスクショを撮る
* SwitchからSD経由で画像を取り出し、PSnapOCR内の「images」に*.jpgファイルを全て入れる
* PSnapOCR.pyをPythonで実行 (PSnapOCR_winの場合は、「main.cmd」をクリックで実行される)
* *.csvファイルが2つ(Spreadsheet貼り付け用と、詳細なテーブル)生成されるはず

## 出力されるファイルについて
* 日付_detail.csv: 写真のポケモンの図鑑番号、星の数、合計スコア、スコアの詳細を全てまとめたファイル
* 日付_sum.csv: 入力した写真の中でスコアが最高のものに関して、各ポケモンの各☆ごとにまとめたファイル
* 日付_cs-script.txt: Cyberscoreにスコアを簡単に登録することができるJavaScriptが記載されたファイル
### cs-scriptの使い方
#### スコア登録
* FirefoxもしくはChromeで[Cyberscore](https://cyberscore.me.uk/game/2785)を開く
* 「+ Submit records」を開く
* 「1★ Photos」にチェック
* 「Edit selected records」をクリック
* 「set ALL to:」にある「Plat form:」を「Switch」に設定
* 開発者ツールを開く(有効になっているならF12で開く)
* Firefoxなら「コンソール」、Chromeなら「Console」タブを開く
* cs-scriptに出力されたコード("a=[[..."の方)を、コンソールに入力(Firefoxの場合はセキュリティエラーが出るので従ってください)。
* よく確認してから「Save changes」をクリック。
* 「2★ Photos」「3★ Photos」「4★ Photos」についても同じ作業を行う。
#### Proof画像の登録方法
* FirefoxもしくはChromeで[Cyberscore](https://cyberscore.me.uk/game/2785)を開く
* 「Submit proofs」を開く
* 「Upload proofs from your device」を選択
* 開発者ツールを開く(有効になっているならF12で開く)
* Firefoxなら「コンソール」、Chromeなら「Console」タブを開く
* cs-scriptに出力されたコード(let arr =..."の方)を、コンソールに入力(Firefoxの場合はセキュリティエラーが出るので従ってください)。
* ページ上部のナビゲーションバー(Home, Games, Scoreboards,...って書いてあるやつ)の下にファイルをアップロードするボタンが現れる
* そのボタンから、PSnapOCR内の「images」ディレクトリの画像ファイルを全て選択する
* 元の画面に戻ると、自動的に画像ファイルが選択されている
* 各ポケモンごとに手動で「Upload proof」をクリックする(セキュリティとサーバー負担の問題で手動)

※どうしても手動が面倒な場合は、ブラウザのポップアップブロックを無効にした後、  
　下記コードをコンソールに入れれば自動でクリックが行われますが、  
　PCのスペックやサーバーからの応答、ブラウザの挙動で不具合が出まくります。  
　そのため、このコードの使い方に関する質問は一切受け付けません。  
　コードを使う場合は、1行目の「1」を「アップロードにかかる秒数+3」  
　に変更してください(サーバーの同時接続数の関係で公式から指示されてる)。  
　また、大量のタブが開き、開きすぎるとブラウザがそれ以上のタブを抑制するので、  
　「このタブより右のタブを閉じる」などを定期的に押す必要があります。

```
let interval = 1;    // ここにアップロードにかかる秒数+3秒を設定してください。
for(let i = 0; i < document.forms.length; i++){
    let tempForm = document.forms[i];
    if(!tempForm.chart_id){
        continue;
    }
    setTimeout(
        function(f){
            f.click();
        }
    , interval * 1000 * i, tempForm[tempForm.length - 1]);
}
```

## PSnapOCRの内容物
* PSnapOCR.py: 本体
* Descriptors: OCRに必要な画像のデータ
* images: ここにスクリーンショットを保存する
* LICENSE: MIT License
* README.md: このファイル

## PSnapOCR_winの内容物
* main.cmd: Pythonを動かすためのバッチファイル
* epy: スタンドアローンで動くPython (embeddable python)


## 注意事項
* 旧型Switch初期ロットのみで動作確認　
* Switch Liteなどだと動かないかも
* 読み取り結果の正確性は保証しないので登録時は各自確認
* このソフトに関連する一切の責任を負いません
* ポケモン関連企業とは一切関係のない非公式のファンメイドツールになります

## What's This?
This tool recognizes screenshots of New Pokémon Snap Photodex and exports the score data to a csv file.

The exported data can be easily registered with [Cyberscore](https://cyberscore.me.uk/game/2785) by using [this Google Spreadsheet](https://docs.google.com/spreadsheets/d/1iP0DA5Ce3V9_AqayWOorvx85n3LNy5c2PkOq_CHcb2A/edit?usp=sharing).

This tool is an unofficial fan-made application and is not affiliated with any Pokémon related company.


## How to Use
### For Phython Users
* Download and unzip the "[PSnapOCR.zip](../../releases/latest/download/PSnapOCR.zip)".
* Install OpenCV to your Python (Anaconda user can install it by the following command)

`
conda install -c conda-forge opencv
`

### For Windows Users WITHOUT Python
* Download and unzip the "[PSnapOCR.zip](../../releases/latest/download/PSnapOCR.zip)".
* Download and unzip the "[PSnapOCR_win.zip](../../releases/latest/download/PSnapOCR_win.zip)
* Copy the contained files, "epy" and "main.cmd", to the root directory of PSnapOCR.


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
* epy: embeddable python


## Attention
* This application was tested only with the initial lot of the old Switch.
* This application may not work with screenshots from Switch lite.
* Accuracy of results is not guaranteed, and use at your own risk.
* I assume no responsibility for anything related to this software.
* This tool is an unofficial fan-made application and is not affiliated with any Pokémon related company.

## Credit
This application uses the below open source software.
* OpenCV © Copyright 2022, OpenCV team ([Apache 2.0](https://github.com/opencv/opencv/blob/master/LICENSE))

