import multiprocessing

def square(templist):
    for i in templist:
        print(i**2)

def main():
    templist = [1,2,3,4,5,6,7,8,9]
    T1 = multiprocessing.Process(target = square, args = (templist,))
    T1.start()
    T1.join()

if __name__ == "__main__":
    main()