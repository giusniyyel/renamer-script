import os
import re

def sorted_alphanumeric(data):
    convert = lambda text: int(text) if text.isdigit() else text.lower()
    alphanum_key = lambda key: [ convert(c) for c in re.split('([0-9]+)', key) ] 
    return sorted(data, key=alphanum_key)

file_with_folios = open('folios.txt', mode='r', encoding='utf-8')
folios_list = file_with_folios.readlines()

certificates_dir = './certs'
certificates_list = sorted_alphanumeric(os.listdir(certificates_dir))

for i in range(len(folios_list)):
    old_file_name = certificates_dir + '/' + certificates_list[i]
    new_file_name = certificates_dir + '/' + folios_list[i].strip() + '.pdf'
    print("changing name of file:", old_file_name, "to", new_file_name)
    os.rename(old_file_name, new_file_name)

print("All files have been changed.")
