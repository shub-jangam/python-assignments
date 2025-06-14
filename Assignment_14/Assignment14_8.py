class Vehicle():
    def Start():
        print("start from Vehicle")

class Car(Vehicle):
    def Start():
        print("Start from Car")

def main():
    Vobj = Vehicle()
    Cobj = Car()

    Vobj.Start()
    Cobj.Start()

if __name__ == "__name__":
    main()
    
