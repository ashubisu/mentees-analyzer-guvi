import os
path = './source_files'
source_file_list = []
# r=root, d=directories, f = files
for r, d, f in os.walk(path):
    for file in f:
        if '.csv' in file:
            source_file_list.append(file)

file_mapping_file = open("config/file_mapping.csv","r")
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
        os.rename("source_files/"+actual_name+".csv","source_files/"+new_name+".csv")
    except FileNotFoundError:
        print("Files Already Renamed")
#print(file_mapping_dict)

# file merger

path = './source_files'
source_file_list = []
# r=root, d=directories, f = files
for r, d, f in os.walk(path):
    for file in f:
        if '.csv' in file:
            source_file_list.append(file)

merged_file = open("intermediate_files/merged.csv","w")
for file_name in source_file_list:
    print(file_name)
    current_file = open("source_files/"+file_name,"r",encoding="utf8")
    fisrt_line_ignored = False
    
    for line in current_file:
        if(not fisrt_line_ignored):
            fisrt_line_ignored = True
            continue
        try:
            record = file_name + "," + line.strip()+"\n"
            merged_file.write(record)
        except UnicodeEncodeError:
            pass
    current_file.close()
merged_file.close()


merged_source_file = open("intermediate_files/merged.csv",'r')
merged_records = merged_source_file.readlines();
merged_source_file.close()

mentees_details_file = open("config/mentees.csv")
mentees_record = mentees_details_file.readlines();
mentees_details_file.close()

mentee_emails = []
for mentee_record_line in mentees_record:
    record = mentee_record_line.split(",");
    mentee_emails.append(record[5].strip())

import datetime
now = datetime.datetime.now()
now = now.strftime("%d_%m_%Y_%H_%M_%S")
destination_file = open("destination_files/report_"+now+".csv","w")
destination_file.write("Source File,Sno,Name,Email,% Completed,Codekata points,Old Codekata submission count,Codekata submission count,Valid Codekata submission count,Department,Assignment Count,Quiz Count,Last Codekata Submitted date(IST),View HeatMap\n")
for mentee_email in mentee_emails:

    for record_line in merged_records:
        record = record_line.split(",")
        if(mentee_email in record):
            print(record_line)
            destination_file.write(record_line)

destination_file.close()