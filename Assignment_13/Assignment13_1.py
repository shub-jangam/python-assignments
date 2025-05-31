class BookStore:
    NoOfBooks = 0

    def __init__(self, a ,b):
        self.Name = a
        self.Auther = b
        BookStore.NoOfBooks = BookStore.NoOfBooks+1
    
    def Display(self):
        print(self.Name +" By "+ self.Auther +". No of Books count" ,BookStore.NoOfBooks)

    
def main():
    bookStore = BookStore(a= "Mr.AbC" , b = "Book1")
    bookStore.Display()
    bookStore1 = BookStore(a= "Mr.DEM" , b = "Book3")
    bookStore1.Display()
    bookStore = BookStore(a= "Mr.XYZ" , b = "Book2")
    bookStore1.Display()
    

    pass
if __name__ == "__main__":
    main()