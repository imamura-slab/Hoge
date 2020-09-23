# pdfkeyword_to_excel

未完成だよ

文字識別精度の問題

キーワード切り出し位置・方法の問題


## タスク
- [この感想シート](./temp/template.pdf)の今日のキーワード欄に書かれたキーワードを読み取り, エクセルに出力する. その際, キーワード数TOP3の人の行は黄色で塗りつぶし, 未提出の人の行は赤文字にする. 
- エクセルシートにはあらかじめ受講者の名前や学生番号などが書かれている. 
- キーワードと一緒に学生番号も読み込み, エクセルに書かれている学生番号と照合してキーワードの書き込み位置を決める. 


## プログラム概要

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
  - 





***
This software includes the work that is  distributed in the [Apache License 2.0](http://www.apache.org/licenses/LICENSE-2.0)



