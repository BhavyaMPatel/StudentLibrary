class library:
    def __init__(self,listofbook):
        self.books=listofbook  
        
        print("****HELLO ,wel-come to great central library ,****")
        
    def displayogbook(self):
        print("AVAILABE BOOKS ARE")
        for book in self.books:
            print('*** '+book+"***")


    def borrowbook(self,bookname):
        if bookname in self.books :
            print(f"{bookname} IS AVAILABLE & RETURN WHITHIN 30 DAYS")
            self.books.remove(bookname)
        else:
            print(f"{bookname} IS NOT AVAILABLE")


    def returnbook(self,bookname):
        self.books.append(bookname)
        print("THANK YOU FOR COME IN CENTRAL LIBRARY HOPE YOU COME AGAIN !!")

class student():
    def __init__(self,name):
        self.name=name
    
    def requestbook(self):
        
        
        self.book=input(f"hi {self.name} \n"+"enter which book do you want to take !!!!\n" )
        return self.book    

    def returnbook(self):
        self.book=input("ENTER BOOK NAME")
        return self.book

centrallib=library(['a','b','c','d'])
name=input("enter the name")
student=student(name)

# centrallib.displayogbook()2
while(True):
    welcomemsg='''
    ===== Wel-come To Central Library =====
            Please choose an option:
            1.listing all books
            2.Request To book
            3.Return a book
            4.Exit te library
    '''
    print(welcomemsg)
    try:
        a=int(input("Enter a choice ; \n--=>"))
    except Exception as e :
        print(e)
    if a==1:
        centrallib.displayogbook()
        
    elif a==2:
        centrallib.borrowbook(student.requestbook())
        False
    elif a==3:
        centrallib.returnbook(student.returnbook())
    elif a==4:
        print("*****")
        print("Thank you for visiting central libray")
        print("*****")
        exit()
    else:
        print("invalid !!!!")
        
        
        
        
