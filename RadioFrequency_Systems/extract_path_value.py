from sys import argv

if (len(argv) != 3):
    print("There are incorrect number of args; usage: python3 extract_path_value.py [path_to_file] [keyword]")
    raise SystemExit

path = argv[1]
try:
    f = open(path, "r")
except: 
    print("Error while opening file: incorrect path or not enough rights!")
    raise SystemExit

keyword = argv[2]
lines = f.readlines()

flag = 0
for line in lines:   
    if line.find(keyword) != -1:
        print(line[:len(line)-1]) # последний элемент - перенос строки, его не включаю
        flag = 1 

if not flag:
	print("There are no lines with such keyword!")
f.close()

