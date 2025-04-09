import os
from datetime import datetime as dt

if __name__ == '__main__':
        
    def displayHeader():
        os.system('cls')
        print("-----  L I B R A R Y  -----".center(100, ' '))
    displayHeader()

    name = input("What is your name? ")
    file_name = f'{name}_info.txt'

    def get_books():
        book_file_name = 'list.txt'
        books = []
        author = []
        description = []
        with open(book_file_name, 'r') as file:
            file.readline()
            for line in file:
                row = line.split(';')
                books.append(row[0])
                author.append(row[1])
                description.append(row[2])
        return books, author, description

    Books, Author, Description = get_books()

    class Book:
        def __init__(self, author, title, description):
            self.author = author
            self.title = title
            self.description = description

    class Borrowed_book(Book):
        count = 0
        
        @classmethod
        def incrementcount(cls):
            cls.count += 1
            
        def __init__(self, author, title, description, borrower_name):
            super().__init__(author, title, description)
            self.borrower = borrower_name
            self.time_borrowed = dt.now().time()
            Borrowed_book.incrementcount()
            
        def force_width(self):
            result = ""
            for i in range(0, len(self.description), 50):
                result += self.description[i:i+50] + "\n"
            return result.strip()

        def append_borrowed_info(self,name, option, count):
                    
            to_format = 'WINGSTON LIBRARY'.center(100,'-') if count == 0 else ''
            to_format += f'\n[Borrower\'s name]{' '* ((100 - len('[Borrower\'s name]')) - len('[Time]'))}[Time]' if count == 0 else ''
            to_format += f'\n{name}{' ' * ((100- len(name)) - len(str(self.time_borrowed)))}{str(self.time_borrowed)}' if count == 0 else ''
            to_format += '\n'
            to_format += f"--------- BORROWED {i+1} ---------".center(100,' ')
            to_format += f'\n[Book_Borrowed]{' '*72}[Book_Author]'
            to_format += f'\n{self.title}{' ' * ((100 - len(self.title)) - len(self.author))}{self.author}'
            to_format += f"\n\n[Description]\n{self.force_width()}\n"
            
            with open(f"{name}_info.txt", option) as file:
                file.write(to_format)

        @staticmethod
        def read_borrowed_info():
            with open(file_name, 'r') as file:
                print(file.read())

    print("[1] : Borrow A Book")
    print("[2] : Exit\n")
    user_input = input("> ").strip()
    if user_input == '2':
        exit()
    displayHeader()
    if user_input == '1': # Display available books
        for i in range(len(Books)):
            print(f'{i+1} : {Books[i]}') 
            
        pickedBooks = [] # Dito mapupunta yung mga books ng user
        pickedAuthors = [] # Dito mapupunta yung author ng book
        pickedDescription = [] # Dito mapupunta yung description ng book na napili
        user_input = None

        while user_input != -1:
            try:
                previous = user_input # This is to avoid repeating books
                user_input = int(input(">"))
                
                if user_input > len(Books):
                    print("Select a valid option!")
                    continue
                
                elif user_input == previous:
                    print("You already picked this book!")
                    continue
                else:
                    pickedBooks.append(Books[user_input-1])
                    pickedAuthors.append(Author[user_input-1])
                    pickedDescription.append(Description[user_input-1])
            except:
                print("An error has occured, make sure you type a valid option!")

    count = 0
    option = 'w+'
    for i in range(len(pickedBooks)):
        if count != 0:
            option = 'a'
        
        Borrowed = Borrowed_book(pickedAuthors[i], pickedBooks[i], pickedDescription[i], name)
        Borrowed.append_borrowed_info(name, option, count)
        count += 1

    Borrowed.read_borrowed_info()
