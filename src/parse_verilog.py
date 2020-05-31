import re

def parse_command(line, command=None):

    line = line.replace('/*', 'COMMENTINI').replace('*/', 'COMMENTEND')
    line = line.strip() + 'COMMENTINI COMMENTEND' if 'COMMENTINI' not in line else line
    excludes = ["reg", "signed"]
    for exclude in excludes:
        if len(line.strip().split()) > 1:
            if line.strip().split()[1] == exclude:
                line = line.replace(exclude + ' ', '', 1)
    param1 = None
    param2 = None
    param3 = None

    if command == 'parameter':
        find_params = re.findall('\w* (.*) = (.*)COMMENTINI(.*)COMMENTEND', line)[0]
        param1 = find_params[0].strip()
        param2 = find_params[1].replace(',', '').strip()
        param3 = find_params[2].strip()
    elif command != 'module':
        if '[' not in line.split()[1]:
            find_params = re.findall('\w* (.*)COMMENTINI(.*)COMMENTEND', line)[0]
            param1 = find_params[0].replace(',', '').replace(';', '').strip()
            param2 = '[0:0]'
        else:
            find_params = re.findall('\w* (\[.*\]) (.*)COMMENTINI(.*)COMMENTEND', line)[0]
            param1_aux = find_params[1].strip().replace(',', '').replace(';', '').split(' ')
            param1 = param1_aux[0]
            param2 = find_params[0].strip() if len(param1_aux) == 1 else str(find_params[0].strip()) + str(param1_aux[1])

        param3 = find_params[-1].strip()
    return param1, param2, param3


def parse_verilog (file_name, wireandregs):
    file_v = open(file_name, 'r')

    template_header = '#  {}\n --- \n **File:** {}  \n{}'
    template_parameters = '### Parameter list  \n|**Name**|**Default Value**|**Description**|  \n|-|-|-|  \n{}'
    template_input = '\n### Input list  \n|**Name**|**Width**|**Description**|  \n|-|-|-|  \n{}'
    template_output = '\n### Output list  \n|**Name**|**Width**|**Description**|  \n|-|-|-|  \n{}'
    template_wire = '\n### Wire list  \n|**Name**|**Width**|**Description**|  \n|-|-|-|  \n{}'
    template_register = '\n### Register list  \n|**Name**|**Width**|**Description**|  \n|-|-|-|  \n{}'
    template_codenotes = '\n### Code notes  \n{}'
    template_instantiation = '\n### Instantiation example \n {}\n'
    credits = '\nAutomatic documentation generator. (https://github.com/controlpaths/verilog_parser)'

    header = ''
    header_start = False
    header_end = False

    table_params = ''
    table_inputs = ''
    table_outputs = ''
    table_wire = ''
    table_reg = ''
    code_notes = ''
    code_notes_active = False
    module_name = ''

    param_detect = ''
    module_inst = ''

    for line in file_v.readlines():
        header_end = True if header_start and '**/' in line else header_end
        if header_start and not header_end:
            line = line.replace(")", "\)")
            if ': ' in line:
                descr = line.split(': ')[0].strip()
                name = line.replace(descr + ':', '').strip()
                header += '**{}**\: {}  \n'.format(descr, name)
            else:
                name = line.strip()
                header += '{}  \n'.format(name)
        header_start = True if '/**' in line else header_start

        if header_end:
            check_command = line.strip().split(' ')[0]
            line = line.strip()

            if check_command == '/md::':
                code_notes_active = False

            if code_notes_active == True:
                code_notes += line
                code_notes += '\n'

            if check_command == 'md::':
                code_notes_active = True


            if check_command == 'module' and code_notes_active == False:
                module_name = line.split()[1]

            if check_command == 'parameter' and code_notes_active == False:
                [param1, param2, param3] = parse_command(line, check_command)
                table_params += "|{}|{}|{}|  \n".format(param1, param2, param3)
                param_detect += '.{}({}),  \n'.format(param1, param2)

            if check_command == 'input' and code_notes_active == False:
                [param1, param2, param3] = parse_command(line, check_command)
                table_inputs += "|{}|{}|{}|  \n".format(param1, param2, param3)
                module_inst += '.{}(),  \n'.format(param1)

            if check_command == 'output' and code_notes_active == False:
                [param1, param2, param3] = parse_command(line, check_command)
                table_outputs += "|{}|{}|{}|  \n".format(param1, param2, param3)
                module_inst += '.{}(),  \n'.format(param1)

            if check_command == 'wire' and code_notes_active == False:
                [param1, param2, param3] = parse_command(line, check_command)
                table_wire += "|{}|{}|{}|  \n".format(param1, param2, param3)

            if check_command == 'reg' and code_notes_active == False:
                [param1, param2, param3] = parse_command(line, check_command)
                table_reg += "|{}|{}|{}|  \n".format(param1, param2, param3)

    if param_detect == '':
        module_inst_v = "```verilog   \n{} {}_inst0(  \n{}   \n);   \n```".format(module_name, module_name, module_inst[:-4])
    else:
        module_inst_v = "```verilog   \n{} #(  \n{}\n){}_inst0(  \n{}   \n);   \n```".format(module_name, param_detect[:-4], module_name, module_inst[:-4])

    output_string = template_header.format(module_name, file_name, header)

    if table_params != '':
        output_string += template_parameters.format(table_params)

    if table_inputs != '':
        output_string += template_input.format(table_inputs)

    if table_outputs != '':
        output_string += template_output.format(table_outputs)

    if table_wire != '' and wireandregs == True:
        output_string += template_wire.format(table_wire)

    if table_reg != '' and wireandregs == True:
        output_string += template_register.format(table_reg)

    if code_notes != '':
        output_string += template_codenotes.format(code_notes)

    output_string += template_instantiation.format(module_inst_v)
    output_string += credits

    #output_string = template.format(module_name, file_name, header, table_params, table_inputs, table_outputs, table_wire, table_reg, code_notes, module_inst_v)
    return module_name, output_string
