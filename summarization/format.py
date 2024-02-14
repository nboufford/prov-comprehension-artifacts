import json
import sys

from pathlib import Path

def get_activity_string(activity_obj):
    return "process with pid:" + activity_obj['id']

def get_args(entity_obj):
    print(entity_obj['annotations']['args_count'])
    args = 'with arguments: "'
    for i in range(1, int(entity_obj['annotations']['args_count'])):
        if (i == 1):
            args = args + entity_obj['annotations']['arg['+str(i)+']']
        else:
            args = args + ' ' + entity_obj['annotations']['arg['+str(i)+']']
    return args + '"'

def get_entity_string(entity_obj):
    annotations = entity_obj['annotations']
    if 'path' in annotations:
        return "file:" + entity_obj['annotations']['path']
    elif 'host_name' in annotations:
        return "ip:" + entity_obj['annotations']['host_name']
    elif 'host' in annotations:
        return "address:" + entity_obj['annotations']['host']
    elif 'command' in annotations:
        return '"' + entity_obj['annotations']['command'] + '" ' + get_args(entity_obj)
    else:
        return ""
    # if annotations['id'] == "file":
    #     return "file:" + entity_obj['annotations']['path']
    # if annotations['id'] == "socket":
    #     return "socket:" + entity_obj['annotations']['host']
    # else: 
    #     return "activiy" + entity_obj['id']

def get_edge_string(edge_obj):
    annotations = edge_obj['annotations']
    if annotations['operation'] == "read":
        return "read from"
    elif annotations['operation'] == "write":
        return "wrote to"
    elif annotations['operation'] == "execute":
        return "executed"
    elif annotations['operation'] == "mmap":
        return "loaded"
    elif annotations['operation'] == "socket_connect":
        return "connected to"
    elif annotations['operation'] == "socket_rcv_skb":
        return "received data from"
    elif annotations['operation'] == "executed_command":
        return "ran command"
    else:
        return ""
    
def get_date(edge_obj):
    annotations = edge_obj['annotations']
    return annotations['datetime'] + " "

def write_libs(edge_obj, entity_obj, libs_list):
    if (edge_obj['annotations']['operation'] == "mmap"):
        libs_list.write(entity_obj['annotations']['path'] + '\n')
    else: 
        libs_list.write('\n')

def prov_format_gpt(prov_file_name):
    try:
        f_prov = open(prov_file_name, "r")        
    except FileNotFoundError:
        msg = prov_file_name + " does not exist."
        print(msg)
        return

    str = Path(prov_file_name).stem
    new_log_name = str + "_gpt.log"
    print("opening file " + new_log_name)

    new_log = open(new_log_name, "a")

    libs_list = open(str + "_libraries_list.txt", "a")

    prov_lines = f_prov.readlines()

    i = 0
    while i < len(prov_lines):
    #for i in range(len(prov_lines)):
        entity_line = prov_lines[i]
        activity_line = prov_lines[i+1]
        edge_line = prov_lines[i+2]

        entity_obj = json.loads(entity_line)
        activity_obj = json.loads(activity_line)
        edge_obj = json.loads(edge_line)
        print(entity_obj)
        print(activity_obj)
        print(edge_obj)

        date = get_date(edge_obj)
        activity_str = get_activity_string(activity_obj)
        edge_str = get_edge_string(edge_obj)
        entity_str = get_entity_string(entity_obj)

        new_line = date + activity_str + " " + edge_str + " " + entity_str + '\n'
        print(new_line)
        new_log.write(new_line)

        write_libs(edge_obj, entity_obj, libs_list)

        i = i + 3

    return

def main():
    if len(sys.argv) > 1:
        prov_file_name = sys.argv[1]
        prov_format_gpt(prov_file_name)
    else:
        print("please provide provenance log")

if __name__ == "__main__":
    main()