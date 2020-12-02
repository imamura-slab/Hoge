default: bench

bench:
	xmverilog +access+rw testbench.sv reverseq.sv \
	+libext+.v -y ${XILINX_VIVADO}/ids_lite/ISE/verilog/src/unisims \
	${XILINX_VIVADO}/ids_lite/ISE/verilog/src/glbl.v

mkhex:
	python3 img2hex.py

mkimg:
	python3 hex2img.py

gif:
	convert -delay 5 -loop 0 output_img/*.png anime.gif
	animate anime.gif


clean:
	rm -f output_img/*.png

all: clean mkhex bench mkimg gif


