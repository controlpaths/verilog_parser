![image](logo.png)
#  ex_module1
 --- 
 **File:** ../example/hdl/ex_module1.v  
**Module name**\: ex_module1  
**Author**\: P Trujillo (pablo@controlpaths.com\)  
**Date**\: Dec 2019  
**Description**\: Module example with parameters.  
**Revision**\: 1.0 Module created.  
### Parameter list  
|**Name**|**Default Value**|**Description**|  
|-|-|-|  
|param1|23|Example param1 description|  
|param2|32|Example param2 description|  

### Input list  
|**Name**|**Width**|**Description**|  
|-|-|-|  
|clk|[0:0]|Example clk input|  
|rst|[0:0]|Example rst input|  
|data_in|[31:0]|Example vector data input|  
|ce|[0:0]|Example data input|  

### Output list  
|**Name**|**Width**|**Description**|  
|-|-|-|  
|data_valid|[0:0]|Example output reg data|  
|data_out|[31:0]|Example vector data out signed|  

### Wire list  
|**Name**|**Width**|**Description**|  
|-|-|-|  
|w_example|[0:0]|Wire example|  
|ws32_example|[31:0]|Wire signed vector example|  

### Register list  
|**Name**|**Width**|**Description**|  
|-|-|-|  
|r_example|[0:0]|Register example|  
|r32_example|[31:0]|Reg vector example|  

### Instantiation example 
 ```verilog   
ex_module1 #(  
.param1(23),  
.param2(32)
)ex_module1_inst0(  
.clk(),  
.rst(),  
.data_in(),  
.ce(),  
.data_valid(),  
.data_out()   
);   
```

Automatic documentation generator. (https://github.com/controlpaths/verilog_parser)