from parse_verilog import parse_verilog
import sys
import os

if len(sys.argv) < 2:
    print("Err1: Function needs a config file")
    exit()

config_file_name = sys.argv[1]

print("Config file selected: " + config_file_name)

## Read configuration file
wireandreg_flag = False
onefile_flag = False
outputdir = ""

file_config = open(config_file_name)
file_list = []

for line in file_config.readlines():
    check_command = line.strip().split(' ')[0]

    if check_command == "wireandreg":
        wireandreg_flag = True

    if check_command == "onefile":
        onefile_flag = True

    if check_command == "outputdir":
        outputdir = line.strip().split(' ')[1]

    if check_command == "file":
        file_list.append(line.strip().split(' ')[1])

for file_name in file_list:
    print(file_name)
    module_name, doc_string = parse_verilog(file_name, True)
    file_doc_name = outputdir + module_name + "_doc.md"

    file_md = open(file_doc_name,"wt")
    file_md.write(doc_string)
    file_md.close()
