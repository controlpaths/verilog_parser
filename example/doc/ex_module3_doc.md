![image](logo.png)
#  ex_module3
 --- 
 **File:** ../example/hdl/ex_module3.v  
**Module name**\: ex_module2  
**Author**\: P Trujillo (pablo@controlpaths.com\)  
**Date**\: Dec 2019  
**Description**\: Module example with code notes.  
**Revision**\: 1.0 Module created.  

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

### Code notes  
#### Example
***This is*** an example of code notes.
- list1
- list2

### Instantiation example 
 ```verilog   
ex_module3 ex_module3_inst0(  
.clk(),  
.rst(),  
.data_in(),  
.ce(),  
.data_valid(),  
.data_out()   
);   
```

Automatic documentation generator. (https://github.com/controlpaths/verilog_parser)