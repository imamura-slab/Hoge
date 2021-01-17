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


