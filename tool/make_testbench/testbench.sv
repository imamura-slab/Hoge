`timescale 1ns/1ps
`default_nettype none

`define P_PXADDR 26
`define P_IMGDEPTH 8

module testbench();
   localparam real CLOCK_PERIOD = 20; //[ns]

   reg clk, rst;
   wire [`P_IMGDEPTH-1:0] q_r, q_g, q_b;
   wire [`P_IMGDEPTH-1:0] revq_r, revq_g, revq_b;
   
   initial begin
      clk <= 0;
      rst <= 0;
      
      #(CLOCK_PERIOD)
        rst <= 1;
      
      #924672010
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
   
   
   parameter P_maxword = `P_PXADDR'd46233599;
   reg [`P_IMGDEPTH-1:0] 	  mem[0:P_maxword];
   reg [`P_PXADDR-1:0] 		  pxADDR;

   
   initial begin
      $readmemh(FILENAME, mem, `P_PXADDR'd0, `P_PXADDR'd46233599);
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
