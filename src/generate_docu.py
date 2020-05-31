from parse_verilog import parse_verilog
import sys

parser_version = "2.0"

if len(sys.argv) < 2:
    print("Err1: Function needs a config file")
    exit()

config_file_name = sys.argv[1]

print("Verilog parser version: " + parser_version)

print("Config file selected: " + config_file_name)

# Read configuration file
wireandreg_flag = False
onefile_flag = False
logo_flag = False
logoName = ""
outputdir = ""

file_config = open(config_file_name)
file_list = []

for line in file_config.readlines():
    check_command = line.strip().split(' ')[0]

    if check_command == "wireandreg":
        wireandreg_flag = True
        print("wireandreg option detected.")

    if check_command == "logo":
        logo_flag = True
        logoName = line.strip().split(' ')[1]
        print("logo option detected.")

    if check_command == "onefile":
        onefile_flag = True

    if check_command == "outputdir":
        outputdir = line.strip().split(' ')[1]
        print("Output directory: " + outputdir)

    if check_command == "file":
        file_list.append(line.strip().split(' ')[1])

print("Starting parser...")

for file_name in file_list:
    print(file_name)
    module_name, doc_string = parse_verilog(file_name, wireandreg_flag)
    file_doc_name = outputdir + module_name + "_doc.md"

    file_md = open(file_doc_name, "wt")

    if logo_flag == True:
        imagemd = "![image](" + logoName + ")\n"
        file_md.write(imagemd)

    file_md.write(doc_string)
    file_md.close()
