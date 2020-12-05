`timescale 1ns/1ps
`default_nettype none

`define P_PXADDR 26
`define P_IMGDEPTH 8


module testbench();
   localparam real CLOCK_PERIOD = 20; //[ns]

   localparam int V_DISP = 240;
   localparam int H_DISP = 320;
   localparam int HEIGHT = 300;
   localparam int WIDTH  = 400;

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
      
      #1444800010
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
      #(CLOCK_PERIOD*1)
      
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
   
   
   parameter P_maxword = `P_PXADDR'd46233599;
   reg [`P_IMGDEPTH-1:0] 	  mem[0:P_maxword];
   reg [`P_PXADDR-1:0] 		  pxADDR;

   
   initial begin
      $readmemh(FILENAME, mem, `P_PXADDR'd0, `P_PXADDR'd46233599);
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
