/**
  Module name:  ex_module2
  Author: P Trujillo (pablo@controlpaths.com)
  Date: Dec 2019
  Description: Module example with code notes.
  Revision: 1.0 Module created.
**/

module ex_module3 (
  input clk, /* Example clk input */
  input rst, /* Example rst input */

  input [31:0] data_in, /* Example vector data input */
  input ce, /* Example data input */
  output reg data_valid, /* Example output reg data */
  output reg signed [31:0] data_out /* Example vector data out signed */
  );

  wire w_example; /* Wire example */
  reg r_example; /* Register example */
  wire signed [31:0] ws32_example; /* Wire signed vector example */

  /*
  md::
  #### Example
  ***This is*** an example of code notes.
  - list1
  - list2
  /md::
  */

  reg [31:0] r32_example; /* Reg vector example */

endmodule
