`timescale 1ns/1ps
`default_nettype none

module selfmade_wrapper
  #(
    P_IMGDEPTH = -1,
    HEIGHT = -1,
    WIDTH = -1
    )
   (
    input wire 			      clk,
    input wire 			      rst,

    input wire [$clog2(WIDTH+1)-1:0]  h_count_in,
    input wire [$clog2(HEIGHT+1)-1:0] v_count_in,
    
    input wire [P_IMGDEPTH-1:0]       r_in,
    input wire [P_IMGDEPTH-1:0]       g_in,
    input wire [P_IMGDEPTH-1:0]       b_in,
    output wire [P_IMGDEPTH-1:0]      r_out,
    output wire [P_IMGDEPTH-1:0]      g_out,
    output wire [P_IMGDEPTH-1:0]      b_out
    );
   
   
   reverseq reverseq_r(
   		       .clk(clk),
   		       .q(r_in),
   		       .revq(r_out)
   		       );
   reverseq reverseq_g(
   		       .clk(clk),
   		       .q(g_in),
   		       .revq(g_out)
   		       );
   reverseq reverseq_b(
   		       .clk(clk),
   		       .q(b_in),
   		       .revq(b_out)
   		       );
   
   
endmodule // selfmade_wrapper

`default_nettype wire
