## Verilog automatic documentation modules.

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
### Calling parser from terminal.
Parser is designed to be called from terminal. Call need one argument for set the configuration file path. This argument is mandatory, and the script will repor a error (Err1: Function needs a config file) if this argument is missing.
```
python3 ./generate_docu.py ../example/hdl/docu_config.cnfg
```
### To Do.
- Identify module dependencies.
- Documentation of code parts.
- Integration with Sphinx.
- Integrate logo on documentation.

### Credits.
***Pablo Trujillo** (FPGA developer)  
***Sara Martínez** (Python developer and QA analyst)
