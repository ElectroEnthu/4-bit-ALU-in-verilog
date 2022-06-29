module tb_alu;
  reg [3:0]a,b;
  reg [2:0] sel;
  wire [7:0] out;
  wire cflag,zflag;
  integer i;
  
  alu test_unit(a,b,sel,out,cflag,zflag);
  
  initial 
    begin
      $display("000-ADD 001-SUB 010-MUL 011-DIV 100-LSL 101-LSR 110-and 111-or");
      $display("|a  |b  |sel |out |cflag |zflag");
      $monitor("%b %b %b %b %b %b",a,b,sel,out,cflag,zflag);
      
      a=4'b1110;
      b=4'b1011;
      sel=3'b000;
      
      for(i=0;i<=7;i=i+1)
        
        begin
          
          sel = sel + 3'b001;
          #10;
         
        end
    
    end 
   //enabling the wave dump

  initial begin

    $dumpfile("dump.vcd"); 
    $dumpvars(0,tb_alu);

  end

endmodule
 
