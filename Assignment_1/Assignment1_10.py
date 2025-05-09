
def ChkLen(text):
    print("Output :" , len(text))

def main():
    print("Enter the text to calculate the len :", end = "")
    text = input()
    ChkLen(text.strip())

if __name__=="__main__":
    main()