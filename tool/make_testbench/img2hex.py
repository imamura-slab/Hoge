import numpy as np
from PIL import Image
import math
import os
import glob


class ImageRom:
    def __init__(self, bit, clk, topmodule, frames, latency, v_disp, h_disp, height, width):
        self.bit       = bit            # 画素のビット幅(10進)
        self.hexbit    = bit // 4       # 画素のビット幅(16進)
        self.clk       = clk            # clk周波数[ns]
        self.topmodule = topmodule
        self.path      = './input_img/' # 画像があるディレクトリ        
        self.extention = '.png'         # 画像の拡張子
        self.frames    = frames         # frame数
        self.latency   = latency        # レイテンシ
        self.v_disp    = v_disp    
        self.h_disp    = h_disp
        self.height    = height
        self.width     = width
        
        
    def makereadh(self):
        """ convert images to .hex file """

        maxword  = 0 
        filelist = []
        for i in range(602):
            filelist.append(self.path + str(i).zfill(3) + self.extention)
        
        wf_r = open("./hex_file/img_r.hex", 'w')
        wf_g = open("./hex_file/img_g.hex", 'w')
        wf_b = open("./hex_file/img_b.hex", 'w')
        # wf = open("./hex_file/img.hex", 'w')
        for filename in filelist:
            pilin = Image.open(filename)
            maxcol, maxrow = pilin.size
            maxword += maxcol*maxrow
            frame = np.asarray(pilin)
            for i in range(maxrow):
                for j in range(maxcol):
                    hexcon = hex(frame[i, j, 0])
                    hexsplit = "{0}".format(hexcon.replace('0x', '')).rjust(int(self.hexbit), '0')
                    wf_r.write("{0}\n".format(hexsplit))

                    hexcon = hex(frame[i, j, 1])
                    hexsplit = "{0}".format(hexcon.replace('0x', '')).rjust(int(self.hexbit), '0')
                    wf_g.write("{0}\n".format(hexsplit))

                    hexcon = hex(frame[i, j, 2])
                    hexsplit = "{0}".format(hexcon.replace('0x', '')).rjust(int(self.hexbit), '0')
                    wf_b.write("{0}\n".format(hexsplit))

                    # hexcon_r   = hex(frame[i, j, 0])
                    # hexsplit_r = "{0}".format(hexcon_r.replace('0x', '')).rjust(int(self.hexbit), '0')
                    # hexcon_g   = hex(frame[i, j, 1])
                    # hexsplit_g = "{0}".format(hexcon_g.replace('0x', '')).rjust(int(self.hexbit), '0')
                    # hexcon_b   = hex(frame[i, j, 2])
                    # hexsplit_b = "{0}".format(hexcon_b.replace('0x', '')).rjust(int(self.hexbit), '0')
                    # wf.write("{0} {1} {2}\n".format(hexsplit_r, hexsplit_g, hexsplit_b))

                    
        wf_r.close()
        wf_g.close()
        wf_b.close()
        # wf.close()

        
        self.word = maxword
        self.wordaddr = math.ceil(math.log2(maxword))

        print("success making hexfile")


    def makeTestbench(self):
        """ make testbench.sv """
        wf = open("testbench.sv", 'w')
        testbench = """`timescale 1ns/1ps
`default_nettype none

`define P_PXADDR {0}
`define P_IMGDEPTH {1}


module testbench();
   localparam real CLOCK_PERIOD = {2}; //[ns]

   localparam int V_DISP = {6};
   localparam int H_DISP = {7};
   localparam int HEIGHT = {8};
   localparam int WIDTH  = {9};

   reg clk, rst;
   wire [`P_IMGDEPTH-1:0] q_r, q_g, q_b;
   wire [`P_IMGDEPTH-1:0] retq_r, retq_g, retq_b;

   reg [$clog2(WIDTH+1)-1:0]  h_count;
   reg [$clog2(HEIGHT+1)-1:0] v_count;
   wire                       sync_flag;
   
   initial begin
      clk <= 0;
      rst <= 0;
      
      #(CLOCK_PERIOD)
        rst <= 1;
      
      #{3}
        $finish;
   end
   
   always #(CLOCK_PERIOD/2)
     clk <= ~clk;


   always_ff@(posedge clk or negedge rst) begin
      if(!rst) begin
	 h_count <= '0;
	 v_count <= '0;
      end
      else begin
	 if(h_count==WIDTH-1)begin
	    h_count <= '0;
	    if(v_count==HEIGHT-1)begin
	       v_count <= '0;
	    end
	    else begin
	       v_count <= v_count + 'd1;
	    end
	 end
	 else begin
	    h_count <= h_count + 'd1;
	    v_count <= v_count;
	 end
      end
   end
   assign sync_flag = (H_DISP <= h_count || V_DISP <= v_count) ? 1'b1 : 1'b0;

   
   imgROM
     #(
       .FILENAME("hex_file/img_r.hex")
       )
   imgROM_r
     (
      .clk(clk),
      .rst(rst),
      .sync_flag(sync_flag),
      .q(q_r)
      );

      imgROM
     #(
       .FILENAME("hex_file/img_g.hex")
       )
   imgROM_g
     (
      .clk(clk),
      .rst(rst),
      .sync_flag(sync_flag),
      .q(q_g)
      );

      imgROM
     #(
       .FILENAME("hex_file/img_b.hex")
       )
   imgROM_b
     (
      .clk(clk),
      .rst(rst),
      .sync_flag(sync_flag),
      .q(q_b)
      );

   
   // self made module wrapper
   selfmade_wrapper #(
		      .P_IMGDEPTH(`P_IMGDEPTH),
		      .HEIGHT(HEIGHT),
		      .WIDTH(WIDTH)
		      ) wrap_inst (
				   .clk(clk),
				   .rst(rst),
				   .h_count_in(h_count),
				   .v_count_in(v_count),
				   .r_in(q_r),
				   .g_in(q_g),
				   .b_in(q_b),
				   .r_out(retq_r),
				   .g_out(retq_g),
				   .b_out(retq_b)
				   );


   int filehandle1;
   int filehandle2;
   int filehandle3;
   
   initial begin
      filehandle1 = $fopen("output_data/data_r.hex", "w");
      filehandle2 = $fopen("output_data/data_g.hex", "w");
      filehandle3 = $fopen("output_data/data_b.hex", "w");
      #(CLOCK_PERIOD*{5})
      
      forever begin
	 #(CLOCK_PERIOD)	 
	 if(retq_r !== 'x) begin
	    $fdisplay(filehandle1, "%2h", retq_r);
	    $fdisplay(filehandle2, "%2h", retq_g);
	    $fdisplay(filehandle3, "%2h", retq_b);
	 end
	 else begin
	    //
	 end
      end
   end


   
   initial begin
      $shm_open("./sim_result/testbench.shm");
      $shm_probe(wrap_inst, "AMS");
   end
     
endmodule // testbench



module imgROM
  #(
    parameter string FILENAME = -1
    )
   (
    input wire 			  clk,
    input wire 			  rst,
    input wire                    sync_flag,
    output wire [`P_IMGDEPTH-1:0] q
    );
   
   
   parameter P_maxword = `P_PXADDR'd{4};
   reg [`P_IMGDEPTH-1:0] 	  mem[0:P_maxword];
   reg [`P_PXADDR-1:0] 		  pxADDR;

   
   initial begin
      $readmemh(FILENAME, mem, `P_PXADDR'd0, `P_PXADDR'd{4});
   end
   
   always_ff@(posedge clk or negedge rst) begin
      if(!rst | pxADDR==P_maxword)
        pxADDR <= `P_PXADDR'd0;
      else if(sync_flag)
        pxADDR <= pxADDR;
      else
        pxADDR <= pxADDR + `P_PXADDR'd1;
   end
   assign q = (sync_flag) ? '0 : mem[pxADDR];
   
endmodule // imgROM


`default_nettype wire
""".format(self.wordaddr,
           self.bit,
           self.clk,
           self.height*self.width*self.frames*self.clk + self.clk//2, # self.word*self.clk + self.clk//2,
           self.word-1,
           self.latency,
           self.v_disp,
           self.h_disp,
           self.height,
           self.width)
        wf.write(testbench)
        wf.close()
        print("success making testbench.sv")


    

if __name__ == '__main__':
    
    # [0] : bit幅
    # [1] : クロック周期 [ns]
    # [2] : 自分のトップモジュールのインスタンス名
    # [3] : frame数
    # [4] : レイテンシ
    # [5] : V_DISP
    # [6] : H_DISP
    # [7] : V_DISP + 垂直同期領域
    # [8] : H_DISP + 水平同期領域
    test = ImageRom(8, 20, "reverseq", 602, 1, 240, 320, 300, 400) 

    test.makereadh()
    test.makeTestbench()
    
        
