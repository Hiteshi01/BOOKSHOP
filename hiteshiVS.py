# Code for display all books present in the library.
def displayBooks():
    print("Books present in the library are : ")
    for book in listOfBooks:
        print("*" + book)

# Issue the book from the library.
def bookAvailable():
    authorName = input("Enter Your full name: ")
    issueBooks = input("Enter the name of the book you want to issue: ")
    listOfBooks.remove(issueBooks)
    with open("authorName.txt","a") as f1:  # write the name of the student who issue the book
                f1.write(authorName+"\t"+issueBooks+"\n")
    print(f"{issueBooks} is issued in your name. So handle carefully and return within 30 days.")

# Return the book to the library.
def returnBook():
    returnName = input("Enter your full name: ")
    returnBooks = input("Enter the name of the book you want to return: ")
    listOfBooks.append(returnBooks)
    with open("returnBooks.txt",'a') as f2:# write the name of the student who return the book
                f2.write(returnName+"\t"+returnBooks+"\n")
    print("Thanks for returning this book. I hope you enjoying reading books and Visit Again.")
    return returnBooks

# -----Main Programe-----
try:
    listOfBooks = ['Python','Java','JavaScript','HTML','CSS','PHP']  # list of the books present in the library.
    while True:
        print()
        welcomMsg = '''=====WELCOME TO CENTRAL LIBRARY=====   
        Please choose the correct option:
        1. Display all the books present in the library.
        2. Request/Issue a book from library.
        3. Return a book.
        4. Exit from library.    
        '''   # Menu bar for user to choose their option.
        print(welcomMsg)
        a = int(input("Enter a choice: "))
        if a == 1:
            displayBooks()  # Display all books
        elif a == 2:            
            bookAvailable()
        elif a == 3:           returnBook()
        elif a == 4:
            print(f"Thank you {returnName} for visiting our library")
            break
        else:
            print("Please select correct option.")
except ValueError:
    print("This book is issued someone else")
