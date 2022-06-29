//4-BIT ALU Design
module alu(a,b,sel,out,cflag,zflag);
  input [3:0]a,b;   //4-bit inputs a,b
  input [2:0] sel;  //3-bit select pin 
  output reg [7:0] out;// 8-bit output 
  output reg cflag=1'b0,zflag=1'b0;

  
  always @(a,b,sel)
    begin
      case(sel)
        3'b000: begin 
              out=a+b;// Addition
          cflag= out[4]; 
          zflag=(out==8'b0);
               end
        3'b001: begin 
          out=a-b; //Subtraction
          cflag= out[4]; 
          zflag=(out==8'b0);
               end
             
        3'b010: begin
          out=a*b; //Multiplication
          cflag= out[4]; 
          zflag=(out==8'b0);
               end
        3'b011: begin 
          out=a/b; //Division
          cflag= out[4]; 
          zflag=(out==8'b0);
               end
        3'b100: begin
          out=a<<1; // logical shift left
          cflag= out[4]; 
          zflag=(out==8'b0);
               end
        3'b101: begin 
          out=a>>1; //logical shift right
          cflag= out[4]; 
          zflag=(out==8'b0);
               end
        3'b110: begin 
          
          out=a & b; //and
           cflag= out[4]; 
          zflag=(out==8'b0);
               end
        3'b111: 
          begin
            out=a|b; //or
             cflag= out[4]; 
          zflag=(out==8'b0);
               end
        default: out=a+b;
      endcase
    end 
endmodule
  
