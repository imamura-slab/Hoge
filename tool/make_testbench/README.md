# 連続画像からテストベンチ作成, さらに出力画像生成

***
## 概要
- 連続画像からSystemVerilog用画像入力テストベンチを生成する. (参考 : [Python3でVerilog用画像入力テストベンチ自動生成](http://kirin.hatenadiary.jp/entry/2014/11/25/020004) )
  - 入力
    - 連続画像 (RGB)
  - 出力
    - テストベンチ(testbench.sv)
      - 1clkに1画素ずつ流れてくる設計だが, 今は有効画素のみ (同期領域は完全に無視)
    - 処理後の画像 (output_img/*.png)
    - 処理後の画像のgif画像 (anime.gif)


***
## 処理の流れ
  1. [img2hex.py](img2hex.py)
     - 連続画像のRGB画素データを16進数でそれぞれ別のファイルに書き込む (./hex_file/img_*.hex, *はr/g/b)
  1. [testbench.sv](testbench.sv)
     - 16進データを読み込み, 何らかの処理を行い, その結果を16進でファイルに書き込む (./output_data/data_*.hex)
     - サンプルとして, 画素のビット反転を行っている (reverseq.sv)
  1. [hex2img.py](hex2img.py)
     - 処理後の16進データを読み込み, 画像を生成する
  1. (gif画像生成)



***
## 使用方法
### 準備
- pythonの`PIL`, `cv2`が使えるマシンを用意する
- 連続画像を`imgディレクトリ`に入れる (000.png, 001.png,... のように命名しておく)
- パラメータ設定
  - [img2hex.py](img2hex.py)
    - 以下, ImageRom のインスタンス化時に指定
    - 輝度値のbit幅 (0～255で表現されるなら8)
    - クロック周期[ns]
    - 自分のトップモジュールのインスタンス名(使ってないのでテキトーで良い)
    - frame数
  - [hex2img.py](hex2img.py)
    - 画像サイズを指定. 上部の HEIGHT・WIDTH


### SystemVerilogでやりたい処理を追加
1. やりたい処理を書いた.svファイルを用意する
1. [testbench.sv](testbench.sv)でそのモジュールをインスタンス化する
   - 適宜wireとか用意していい感じにつなぐ
1. レイテンシに応じて, #(CLOCK_PERIOD) とか入れながら $fdisplay を開始するタイミングを調整する
   - output_data/data_*.hex は 1行目に1frame目の左上の画素データが入ることを想定している


### 実行
- 以下のコマンドで全ての処理が実行される

```
make all
```	


***
## TODO
- [ ] 有効画素領域だけでなく, 同期領域を含めたシミュレーションができるようにする.
- [ ] 今はr,g,bそれぞれのファイルを用意しているが, それを一つにまとめる.
- [ ] img2hex.py の処理の中で画像サイズは分かるので, ファイルに書き込むなどして hex2img.py で指定しなくて良いようにする.


