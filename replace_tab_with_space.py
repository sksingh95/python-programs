import os
import re


if __name__ == "__main__":
    all_files = []
    
    for (path, subdirs, files) in os.walk("./"):
        #file_list = [os.path.join(path,file) for file in files if ".c" in file or ".h" in file]
        file_list = [os.path.join(path,file) for file in files if re.match(".*(\.c|\.h)", file)]
        for file in file_list : all_files.append(file)
    
    for file in all_files:
        file_all_line = []
        print(file)
        with open(file, "r") as file_in:
            for line in file_in:
                line = re.sub('\t', "    ", line)
                file_all_line.append(line)
                
        with open(file, "w") as file_out:
            for line in file_all_line:
                file_out.write(line)
                