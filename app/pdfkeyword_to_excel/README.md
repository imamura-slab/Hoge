# pdfkeyword_to_excel

未完成だよ

文字識別精度に問題あり(より良い日本語手書き文字識別方法募集)

キーワード切り出し位置・方法の問題


## タスク概要
- [この感想シート](./temp/template.pdf)の今日のキーワード欄に書かれたキーワードを読み取り, エクセルに出力する. その際, キーワード数TOP3の人の行は黄色で塗りつぶし, 未提出の人の行は赤文字にする. 
- エクセルシートにはあらかじめ名前や学生番号などが書かれている. 
- キーワードと一緒に学生番号も読み込み, エクセルに書かれている学生番号と照合してキーワードの書き込み位置を決める. 


## 使用法
### 概要
- extract_id.py : 学生番号を切り出して出力
- id.csv : 学生番号とキーワードか書かれたcsvファイル
- crop.py : 画像からキーワードの部分を切り出して保存
- make_excel.py : id.csvから学生番号とキーワードを読み出して, excelファイルにキーワードを書き込む. さらに未提出者を赤文字にし, キーワード数TOP3の人を黄色でハイライトする. 



### 手順(文字認識を使わないVer)
excelに直接入力するのとあまり変わらないかも... ターミナルでの作業に慣れているならこっちの方が良い...?  

1. 準備
   - `python3系の環境構築`
   - 名前や学生番号などが書かれたエクセルファイル`template.xlsx` (ファイル名は何でも良いが, これ以外の名前だと, プログラムの読み込むファイル名の部分を変更する必要あり)
1. csvファイルの用意
   - `python3 extract_id.py > id.csv`
   - 該当する学生番号が書かれた行に, キーワードをコンマで区切りながら入力していく
     - 例) 1111111, キーワード1, キーワード2, キーワード3  
       　　2222222, キーワードa, キーワードb
   - 未提出者の行は学生番号ごと削除する
1. excel書き込み
   - `python3 make_excel.py`
   - output.xslxが生成される
   


### 手順(文字認識を使うVer)
文字認識精度の問題でほぼ使えない. 半分くらい正しく認識してくれない. 

1. 準備(文字認識を使わないVerに加えて必要なこと)
   - `OpenVINOの環境構築`
1. ...の実行



***
***
### 文字認識(OCR : Optical character recognition)
- Intelの`OpenVINO`(その中のhandwritten_japanese_recognition_demo)を使用

#### OpenVINO
> OpenVINOツールキットは、フレームワークからのディープラーニングモデルの最適化と、推論エンジンを使用したIntelハードウェアへの展開を容易にする無料のツールキットです。([Wikipedia](https://en.wikipedia.org/wiki/OpenVINO)の日本語訳)
- Apache License Version 2.0 
- 参考サイト
  - [環境構築（MacOS編）](https://openvino.jp/configuration-macos/)
  - [AIコラムー第6回 (OpenVINO第1回) OpenVINOの環境構築とサンプルアプリケーションの実行](https://www.nskint.co.jp/2020/07/10/ai_column_6/)
  - [日本語手書き文字の認識](https://openvino.jp/handwritten-japanese/)
- pythonのバージョンに制限があるので注意



### Excel書き出し
- PythonでExcelの操作ができるモジュール`openpyxl`を使用

#### openpyxl
- 参考サイト
  - [] 



### テキストマイニング
- id.csv を [https://textmining1.userlocal.jp/old/file](https://textmining1.userlocal.jp/old/file) に投げると, キーワードを分析し, ワードクラウドの作成などをしてくれる



***
This software includes the work that is  distributed in the [Apache License 2.0](http://www.apache.org/licenses/LICENSE-2.0)



