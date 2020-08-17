
# EXAMPLE :
#
# =======================================
#
# *runs the programme*
#
# path : c:\path\to\file-or-folder\mainFolder\
#
#  mainFolder
#   ├── music
#   │   ├── new-song
#   │   │	 ├── new1.mp3
#   │   │   └── new2.mp3
#   │   └── audio1.mp3 
#   ├── needs.tx
#   └── logo.svg
#
# INFO:
# 2-folders, 5-files
#
# =======================================


import os

# global variables
_turn = ['├', '└']
_line = '│'
_dash = '─'*2 + ' '
_space = "  "
numDir = 0
numFile = 0



def separator(path):
    files = []
    folders = []
    
    for var in os.listdir(path):
        new_path = path + "/" + var

        if os.path.isdir(new_path):
            folders.append(var)
        else:
            files.append(var)
    return {"files": files, "folders": folders, "file_count": len(files), "folder_count":len(folders), "count": len(files)+len(folders)}



def print_tree(path, n = 0, seq = _space):

    global numDir
    global numFile

    isdir = os.path.isdir(path)
    this_folder = ""
    if isdir:
        this_folder = separator(path)
        numDir += this_folder["folder_count"]
        numFile += this_folder["file_count"]

    if this_folder['folder_count'] != 0:
        folders = this_folder['folders']
        for folder in folders:
            if folders.index(folder) != (this_folder["count"] - 1):
                seq_extend = seq + _line + _space
                print(seq + _turn[0] + _dash + folder)
                print_tree(path + '/' + folder, seq = seq_extend)
            else:
                seq_extend = seq + _space
                print(seq + _turn[1] + _dash + folder)
                print_tree(path + '/' + folder, seq = seq_extend)
    
    if this_folder['file_count'] != 0:
        files = this_folder['files']
        for file in files:
            if (files.index(file) != (len(files) - 1)) :
                print(seq + _turn[0] + _dash + file)
            else:
                print(seq + _turn[1] + _dash + file)


def main():
    global numFile
    global numDir

    print("\n")

    try:
        path = input("Enter/Paste the complete of file PATH : ")
    except:
        print("Enter a valid input type")
        main()
        return 0
    
    path_exists = os.path.exists(path)

    if path_exists:
        folder_name = path.split('/')
        folder_name = folder_name[-1] if (folder_name[-1] != 0) else folder_name[-2]
        print(" " + folder_name)
        print_tree(path)

        info = f"|   {numDir} directories ,  {numFile} files   |"
        seq = "="*len(info)

        print("\n", seq, "\n", info, "\n", seq)

    else:
        print("The specified path does not exist!.")


if __name__ == "__main__":
    main()
