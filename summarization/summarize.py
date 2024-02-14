import json
import sys

from pathlib import Path

def remove_map(obj1, obj2, entity_obj):
    if (obj1['annotations']['operation'] == "mmap"):
        if (entity_obj['annotations']['path'][-12:] == 'lib-dynload/'):
           return 1
        if ('lib64/' in entity_obj['annotations']['path']):
           return 1
        if ('[eventpoll]' in entity_obj['annotations']['path']):
           return 1
    
    return 0

# this does not work
# making up for the way thoth captures file paths. Once the file paths can be larger (and do not get truncated), we can remove this
def fix_truncated_map(edge_line, entity_line):
    new_entity_line = entity_line
    if ("mmap" in edge_line):
        if ('.' in entity_line):
            new_entity_line = entity_line.replace('."', '.so"')
        if ('.s"' in entity_line):
            new_entity_line = entity_line.replace('.s"', '.so"')
        if ('linux-gn"' in entity_line):
            new_entity_line = entity_line.replace('linux-gn"', 'linux-gnu.so"')
        if ('linux-g"' in entity_line):
            new_entity_line = entity_line.replace('linux-g"', 'linux-gnu.so"')
    return new_entity_line


def compare_obj(obj1, obj2):
    # print(obj1)
    # print(obj2)
    if obj1['to'] != obj2['to']:
        return 0
    if obj1['from'] != obj2['from']:
        return 0
    if obj1['type'] != obj2['type']:
        return 0
    if obj1['annotations']['operation'] != obj2['annotations']['operation']:
        return 0
    # lastly compare operation in the annotations, but lets see if that ever arises (it does)
    return 1

# read three lines from a file
# prov logs should be written such that there are three lines per entry (Entity, Activty and Edge)
# ... this might change when we add the network stuff... but probably it will still be the case that every third entry is an edge
def read_entry(file):
    entity = file.readline()
    activity = file.readline()
    edge = file.readline()
    return edge


# remove duplicate edges in prov log
# each line in the file should be a json object (as per SPADE format)
# an edge is a duplicate if it has the same to, from, type and operation as the previous line 
def prov_summarize_edges(prov_file_name):
    try:
        f_prov = open(prov_file_name, "r")        
    except FileNotFoundError:
        msg = prov_file_name + " does not exist."
        print(msg)
        return

    str = Path(prov_file_name).stem
    new_log_name = str + "_summarized.json"
    print("opening file " + new_log_name)

    new_log = open(new_log_name, "a")

    prev_edge = {}
    curr_edge = {}

    # read first line
    line = f_prov.readline()

    # while read entry (3 lines)
        # compare edge to prev edge
        # if same then do not record
        # if different then record all three lines

    # read until end of file
    while line:
        print(line)
        
        entity_line = line
        activity_line = f_prov.readline()
        edge_line = f_prov.readline()

        entity_line = fix_truncated_map(edge_line, entity_line)

        curr_edge = json.loads(edge_line)
        curr_entity = json.loads(entity_line)

     #   new_entity = fix_truncated_map(curr_edge, curr_entity)

     #   new_entity_line = json.dumps(new_entity)

       # curr_obj = json.loads(line)
        if prev_edge == {}:
            new_log.write(entity_line)
            new_log.write(activity_line)
            new_log.write(edge_line)
            # still want to add it to the log.. making base case explicit for now

        elif compare_obj(prev_edge, curr_edge) == 1:
    #        # do not add it to the new log, it is a duplicate
            print("not adding line")

        elif remove_map(curr_edge, curr_edge, curr_entity) == 1:
            print("not adding")

        else:
            new_log.write(entity_line)
            new_log.write(activity_line)
            new_log.write(edge_line)

        prev_edge = curr_edge
        line = f_prov.readline()


def main():
    if len(sys.argv) > 1:
        prov_file_name = sys.argv[1]
        prov_summarize_edges(prov_file_name)
    else:
        print("please provide provenance log")

if __name__ == "__main__":
    main()
