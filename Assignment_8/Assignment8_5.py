import threading

def forward(no):
    for i in range(no):
        print(i)
def reverse(no):
    print("Reverse Count")
    for i in range(no, 0, -1):
        print(i)
def main():
    
    f  = threading.Thread(target=forward, args=(50,))
    r   = threading.Thread(target=reverse, args=(50,))

    f.start()
    f.join()

    r.start()
    r.join()

if __name__ == "__main__":
    main()
