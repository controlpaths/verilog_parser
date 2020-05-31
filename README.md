![image](./example/doc/logo.png)
## Verilog automatic documentation modules.

### Version history
- ***v1.0***  
First version.  
- ***v2.0***  
Code refactor.  
Added *wireandreg* command to config file.  
Added *logo* command
Added function *code notes*.

### Description
This parser can be used to document all verilog files of one project. The output documentation uses **Markdown** (.md) as documentation language. IN examples directory can found a documentation example of 2 example modules.

### Coding instructions.
- Header, and **only header**, has to be defined into double asteriscs comment.

```
/**
...
Header
...
**/
```
- On header, colon (:), is reserved character, and only is used for separate a field (description, author,...), and its value.
- Only one signal declaration by line.
- Signal description is optional.
- parameter word has to be found in each line where parameter found.
- input word has to be found in each line where input found.
- output word has to be found in each line where output found.

#### Code notes
Parser gives the developer the possibility of describe code parts. This documentation must to be write in markdown format, since this text will be added directly to documentation. Verilog parser do not check the syntax of this markdown code.  
##### Structure
```
/*
md::

Text in markdown format

/md::
*/
```

### Verilog structures supported.
- module declaration.
- input
- input vector.
- input vector signed.
- output
- output registered
- output vector
- output vector registered
- output vector signed
- output vector registered signed
- wire
- wire vector.
- wire vector signed.
- wire matrix.
- wire matrix signed.
- reg
- reg vector.
- reg vector signed.
- reg matrix.
- reg matrix signed.

### Configuration file.
For configure the parser, a configuration file is needed. This configuration file will contain the instructions for the parser. The instructions available in this version are:
- **file** : This instruction will be used to specify a file to document. Each file has to be indicated one by one. The path indicated in file instruction has to be relative to parser path.
```
file ../example/hdl/cen_generator_v1_0.v
```
- **outputdir** : This instruction is used to set the output directory for the documentation. The path indicated in outputdir instrucion has to be relative to parser path.
```
outputdir ../example/doc
```
- **wireandreg**: When this instruction is present in config file, wires and registers are added to documentation. Otherwise wires and registers are no added.
- **logo**: This instruction is used to use a logo on all markdown documents. Instruction must be followed by the path to logo from the markdown output file, since this file is who has to read it.

### Calling parser from terminal.
Parser is designed to be called from terminal. Call need one argument for set the configuration file path. This argument is mandatory, and the script will repor a error (Err1: Function needs a config file) if this argument is missing.
```
python3 ./generate_docu.py ../example/hdl/docu_config.cnfg
```
### To Do.
- Identify module dependencies.
- Integration with Sphinx.
- Use regular expresions for select files.

### Credits.
***Pablo Trujillo** (FPGA developer)  
***Sara Martínez** (Python developer and QA analyst)
