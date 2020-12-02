module reverseq(
		input wire 	 clk,
		input wire [7:0] q,
		output reg [7:0] revq
		);

   always_ff@(posedge clk)begin
      revq <= ~q;
   end

endmodule // reverseq
