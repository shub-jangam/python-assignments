def main():
    print("Enter word : ")
    word = input()

    wordlen = len(word)-1
    newword = ""

    for i in range(wordlen,-1,-1):
        newword = newword+word[i]
    if newword ==word:
        print("Palindrome")

if __name__ == "__main__":
    main()