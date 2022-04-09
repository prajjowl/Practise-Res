# Practise-Res
#CREATE A LIBRARY clASS

#display book
#lend book-(who owns te book if not present)
#add book
#return book
#haryLibrary=Library(list of books,Library name
# creat a name of function and run an infinite while loop asking users for their input

class library:
    def __init__(self,booklist,bookname):
        self.booklist=booklist
        self.bookname=bookname
        self.bookdict={}
    def display_book(self):
        print("f(you have the all the goo book in dictionary{self.booklist}")
    def add_book(self):
        a=input("\t\tPlease enter the name of the bopok you want to add")
        self.booklist.append(a)
    def lend(self):
        bnm=input("enter the name of book you want  to lend ")
        pnm=input("Enter the name of book to whom you are landing")
        if bnm in self.booklist:
          # KEY IS BOOK AND value is none
           self.booklist.remove(bnm)
           self.bookdict.update({bnm:pnm})
        elif bnm in self.bookdict.keys():
            a=self.bookdict[bnm]
            print(f"book is already lended to {a}")
        else:
            print("This book is not availale in library")

    def return_book(self):
        a=input("\t\tplease enter the name of the returned book ")
        self.booklist.append(a)
        del self.bookdict[a]

if __name__== "__main__" :
 harry_library=library(["book1","book2","book3","book4"],"harry library")
 while True:
     user=input("\nD for Display , for add,for lend and for returning book  arey bhai good good good for exit   ")
     if user=="good":
         break
     elif user=="Display":
         harry_library.display_book()
     elif user=="Add":
         harry_library.add_book()
     elif user=="lend":
         harry_library.lend()
     elif user=="Return":
         harry_library.return_book()
     else:
         print("It is invalid ")
