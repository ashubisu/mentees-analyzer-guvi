import os

path = '.\\source_files'
source_file_list = []
# r=root, d=directories, f = files
for r, d, f in os.walk(path):
    for file in f:
        if '.csv' in file:
            source_file_list.append(file)

file_mapping_file = open("config\\file_mapping.csv","r")
file_mapping_dict = {}
fisrt_line_ignored = False
for line in file_mapping_file:
    if(not fisrt_line_ignored):
        fisrt_line_ignored = True
        continue
    # removes extra \n char
    line = line.strip()
    line_data = line.split(",");
    file_mapping_dict[line_data[0]] = line_data[1]
file_mapping_file.close()

for actual_name,new_name in file_mapping_dict.items():
    try:
        os.rename("source_files\\"+actual_name+".csv","source_files\\"+new_name+".csv")
    except FileNotFoundError:
        print("Files Already Renamed")
#print(file_mapping_dict)

# file merger

path = '.\\source_files'
source_file_list = []
# r=root, d=directories, f = files
for r, d, f in os.walk(path):
    for file in f:
        if '.csv' in file:
            source_file_list.append(file)

merged_file = open("intermediate_files\\merged.csv","w")
for file_name in source_file_list:
    print(file_name)
    current_file = open("source_files\\"+file_name,"r")
    fisrt_line_ignored = False
    for line in current_file:
        if(not fisrt_line_ignored):
            fisrt_line_ignored = True
            continue
        record = file_name + "," + line.strip()+"\n"
        merged_file.write(record)
    current_file.close()
merged_file.close()
