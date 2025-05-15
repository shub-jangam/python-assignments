def main():
    print("Enter no : ", end = "")
    no = input()
    result = 0
    for i in no:
        result = result+int(i)
    print("output", result)
        
if __name__ == "__main__":
    main()