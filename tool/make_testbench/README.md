# 連続画像からテストベンチ作成, さらに出力画像生成

***
## 概要
- 連続画像からSystemVerilog用画像入力テストベンチを生成する. (参考 : [Python3でVerilog用画像入力テストベンチ自動生成](http://kirin.hatenadiary.jp/entry/2014/11/25/020004) )
  - 入力
    - (RGB)連続画像 (input_img/*.png)
  - 出力
    - テストベンチ(testbench.sv)
      - 1clkに1画素ずつ流れてくる設計 (同期領域も)
    - 何かしら処理した後の画像 (output_img/*.png)
    - 何かしら処理した後の画像のgif画像 (anime.gif)


***
## 処理の流れ
  1. [img2hex.py](img2hex.py)
     - 連続画像のRGB画素データ(有効画素領域だけ)を16進数でそれぞれ別のファイルに書き込む (./hex_file/img_*.hex, *はr/g/b)
  1. [testbench.sv](testbench.sv)
     - 16進データを読み込み, [selfmade_wrapper.sv](selfmade_wrapper.sv)に書かれた何らかの処理を行い, その結果を16進でファイルに書き込む(同期領域を含む. 同期領域部分の値は0にしている) (./output_data/data_*.hex)
     - サンプルとして, 画素のビット反転を行っている (reverseq.sv)
  1. [hex2img.py](hex2img.py)
     - 処理後の16進データを読み込み, 画像を生成する
  1. (gif画像生成)



***
## 使用方法
### 準備
- pythonの `PIL`, `cv2`, `numpy` が使えるマシンを用意する
- 連続画像を`input_imgディレクトリ`に入れる (000.png, 001.png,... のように命名しておく)
  - もし他のディレクトリを指定したかったり, 別の拡張子が良いというときは img2hex.py の __init__ のところを変更する
- パラメータ設定
  - [img2hex.py](img2hex.py) (ImageRom のインスタンス化時に指定)
    - 輝度値のbit幅 (0～255で表現されるなら8)
    - クロック周期[ns]
    - 自作モジュールのインスタンス名(使ってないのでテキトーで良い)
    - frame数
    - 自作モジュールのレイテンシ
    - V_DISP(横:有効画素)
    - H_DISP(縦:有効画素)
    - HEIGHT(横:有効画素 + 同期領域)
    - WIDTH (縦:有効画素 + 同期領域)
  - [hex2img.py](hex2img.py) (プログラム上部で指定)
    - 画像サイズを指定. V_DISP・H_DISP・HEIGHT・WIDTH
    - 同期領域の部分も画像にしたければ DISP_SYNC=True に


### SystemVerilogでやりたい処理を追加
1. やりたい処理を書いた.svファイルを用意する
1. [selfmade_wrapper.sv](selfmade_wrapper.sv)内でそのモジュールをインスタンス化する
   - 適宜wireとか用意していい感じにつなぐ
1. (レイテンシに応じて, #(CLOCK_PERIOD) とか入れながら $fdisplay を開始するタイミングを調整する)
   - output_data/data_*.hex は 1行目に1frame目の左上の画素データが入ることを想定している


### 実行
- 以下のコマンドで全ての処理が実行される
```
make all
```
- `testbench.sv が更新されるので testbench.sv に変更を加えた場合は注意`
  - img2hex.py の test.makeTestbench() を実行しないようにコメントアウトしましょう. または img2hex.py より後の処理だけをしましょう. 



***
## TODO
- [x] 有効画素領域だけでなく, 同期領域を含めたシミュレーションができるようにする.
- [ ] 今はr,g,bそれぞれのファイルを用意しているが, それを一つにまとめる.



