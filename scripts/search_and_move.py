import os
import shutil


def main():
    filepath = input("Enter file path to search keyword: ")
    keyword = input("Enter keyword to be searched: ")
    main_folder = filepath + '\\' + "valid_files"
    if not os.path.exists(main_folder):
        os.makedirs(main_folder)
    search_and_move_file(filepath, keyword, main_folder)


def search_and_move_file(filepath, keyword, main_folder):
    files = os.listdir(filepath)
    for f in files:
        if ".txt" in f:
            src_file = filepath + '\\' + f
            counter = 0
            with open(src_file, 'r') as src:
                for line in src:
                    if keyword in line:
                        counter = counter + 1
                        break
            dst_file = main_folder + '\\' + f
            if os.path.exists(dst_file):
                if os.path.samefile(src_file, dst_file):
                    continue
                os.remove(dst_file)
            if counter > 0:
                shutil.move(src_file, dst_file)


if __name__ == "__main__":

    main()
