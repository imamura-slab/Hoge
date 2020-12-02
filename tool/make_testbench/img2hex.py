import numpy as np
from PIL import Image
import math
import os
import glob


class ImageRom:
    def __init__(self, bit, clk, topmodule, frames):
        self.bit       = bit       # 画素のビット幅(10進)
        self.hexbit    = bit // 4  # 画素のビット幅(16進)
        self.clk       = clk
        self.topmodule = topmodule
        self.path      = './img/'  # 画像があるディレクトリ        
        self.extention = '.png'    # 画像の拡張子
        self.frames    = frames    # frame数

        
    def makereadh(self):
        """ convert images to .hex file"""

        maxword  = 0 
        
        filelist = []
        for i in range(602):
            filelist.append(self.path + str(i).zfill(3) + self.extention)

        
        wf = open("./hex_file/img_r.hex", 'w')
        for filename in filelist:
            pilin = Image.open(filename)
            maxcol, maxrow = pilin.size
            maxword += maxcol*maxrow
            frame = np.asarray(pilin)
            for i in range(maxrow):
                for j in range(maxcol):
                    hexcon = hex(frame[i, j, 0])
                    hexsplit = "{0}".format(hexcon.replace('0x', '')).rjust(int(self.hexbit), '0')
                    #print(hexsplit)
                    wf.write("{0}\n".format(hexsplit))
        wf.close()

        wf = open("./hex_file/img_g.hex", 'w')
        for filename in filelist:
            pilin = Image.open(filename)
            # maxcol, maxrow = pilin.size
            # maxword += maxcol*maxrow
            frame = np.asarray(pilin)
            for i in range(maxrow):
                for j in range(maxcol):
                    hexcon = hex(frame[i, j, 1])
                    hexsplit = "{0}".format(hexcon.replace('0x', '')).rjust(int(self.hexbit), '0')
                    #print(hexsplit)
                    wf.write("{0}\n".format(hexsplit))
        wf.close()

        wf = open("./hex_file/img_b.hex", 'w')
        for filename in filelist:
            pilin = Image.open(filename)
            # maxcol, maxrow = pilin.size
            # maxword += maxcol*maxrow
            frame = np.asarray(pilin)
            for i in range(maxrow):
                for j in range(maxcol):
                    hexcon = hex(frame[i, j, 2])
                    hexsplit = "{0}".format(hexcon.replace('0x', '')).rjust(int(self.hexbit), '0')
                    #print(hexsplit)
                    wf.write("{0}\n".format(hexsplit))
        wf.close()

        

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

   reg clk, rst;
   wire [`P_IMGDEPTH-1:0] q_r, q_g, q_b;
   wire [`P_IMGDEPTH-1:0] revq_r, revq_g, revq_b;
   
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

   
   imgROM
     #(
       .FILENAME("hex_file/img_r.hex")
       )
   imgROM_r
     (
      .clk(clk),
      .rst(rst),
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
      .q(q_b)
      );
   
   // add your instance module
   reverseq reverseq_r(
			  .clk(clk),
			  .q(q_r),
			  .revq(revq_r)
			  );
   reverseq reverseq_g(
			  .clk(clk),
			  .q(q_g),
			  .revq(revq_g)
			  );
   reverseq reverseq_b(
			  .clk(clk),
			  .q(q_b),
			  .revq(revq_b)
			  );


   int filehandle1;
   int filehandle2;
   int filehandle3;
   
   initial begin
      filehandle1 = $fopen("output_data/data_r.hex", "w");
      filehandle2 = $fopen("output_data/data_g.hex", "w");
      filehandle3 = $fopen("output_data/data_b.hex", "w");
      #(CLOCK_PERIOD)
      
      forever begin
	 #(CLOCK_PERIOD)	 
	 if(revq_r !== 'x) begin
	    $fdisplay(filehandle1, "%2h", revq_r);
	    $fdisplay(filehandle2, "%2h", revq_g);
	    $fdisplay(filehandle3, "%2h", revq_b);
	 end
	 else begin
	    //
	 end
      end
   end


   
   initial begin
      $shm_open("./sim_result/testbench.shm");
      $shm_probe(reverseq_r, "A");
      $shm_probe(reverseq_g, "A");      
      $shm_probe(reverseq_b, "A");
   end
     
endmodule // testbench



module imgROM
  #(
    parameter string FILENAME = -1
    )
   (
    input wire 			  clk,
    input wire 			  rst,
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
      else
        pxADDR <= pxADDR + `P_PXADDR'd1;
   end
   assign q = mem[pxADDR];
   
endmodule // imgROM


`default_nettype wire
""".format(self.wordaddr, self.bit, self.clk, self.word*self.clk + self.clk//2, self.word-1)
        wf.write(testbench)
        wf.close()
        print("success making testbench.sv")


    

if __name__ == '__main__':
    
    #bit幅, 1/クロック周波数 [ns], 自分のトップモジュールのインスタンス名, frame数
    test = ImageRom(8, 20, "reverseq", 602) 

    test.makereadh()
    test.makeTestbench()
    
        
