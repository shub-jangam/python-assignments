def display(no):
    for i in range(1 , no+1 ,1):
        print(i,end = "\t")
        


def main():
    print("Enter the No ", end = "")
    no = int(input())
    for i in range(no):
        display(no)
        print()

if __name__ == "__main__":
    main()

# no =5
# pattern = "*"
# for i in range(no ,0, -1):
#     print()
#     for j in range(i):
#         print(pattern , end= "\t")