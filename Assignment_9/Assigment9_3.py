import multiprocessing

def factorial(no):
    fact= 1
    for i in range(no,0,-1):
        fact = fact*i
    return fact

def main():
    p = multiprocessing.Pool()
    ret = p.map(factorial,[2,5])
    print(ret)

if __name__ == "__main__":
    main()