import os

def CheckFileExist(filename):
    if os.path.exists(filename):
            return True
    return False

def count_file(filename):
    try:
        with open(filename, 'r') as f1:
            lines = f1.readlines()
            
            line_count = len(lines)
            word_count = sum(len(line.split()) for line in lines)
            char_count = sum(len(line) for line in lines)

            print("Lines:", line_count)
            print("Words:", word_count)
            print("Characters:", char_count)
    except Exception as e:
        print("An error occurred: ", e)

def main():
    filename = input("Enter the path to the file: ")
    exist = CheckFileExist(filename)
    if exist ==True:
        print("File Exist in Folder !!")
        count_file(filename)
    else:
        print("File not found in Folder")

if __name__ == "__main__":
    main()