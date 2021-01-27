# install

icarus verilog compiler
```
$brew install icarus-verilog
```

波形観測ツール gtkwave
```
$brew install cask/gtkwave
```


# 波形ダンプ
- $shm_openや$shm_probeではなく`$dumpfile`, `$dumpvars`を使う
```verilog
initial begin
	$dumpfile("ファイル名.vcd");
	$dumpvars(0, トップモジュールのインスタンス名);
end
```


# コンパイル
- SystemVerilogの場合 `-g2005-sv` を入れる
  - 最新のSysyemVerilogに対応していないのか, コンパイルエラーになってしまう記述もある...... 
```
$ iverilog -g2005-sv *.sv *.sv *.sv ...
$ vvp a.out
```

