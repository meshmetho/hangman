import csv


def read_books(file_name):
    books = []
    with open(file_name, 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            books.append(row)
    return books


def search_books_by_author(author_name, books):
    result = []
    for book in books:
        if book['author'] == author_name:
            result.append(book)
    return result


def search_book_by_isbn(isbn, books):
    for book in books:
        if book['ISBN'] == isbn:
            return {'title': book['title'], 'price': book['price']}
    return None


def search_books_by_price_range(min_price, max_price, books):
    result = []
    for book in books:
        price = float(book['price'])
        if price >= min_price and price <= max_price:
            result.append(book)
    return result


def add_book(file_name, book):
    with open(file_name, 'a', newline='') as csv_file:
        fieldnames = ['title', 'author', 'ISBN', 'price']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writerow(book)


def main():
    file_name = 'books.csv'
    books = read_books(file_name)

    while True:
        print('1. Search books by author')
        print('2. Search book by ISBN')
        print('3. Search books by price range')
        print('4. Add new book')
        print('5. Exit')
        choice = int(input('Enter your choice: '))

        if choice == 1:
            author_name = input('Enter author name: ')
            result = search_books_by_author(author_name, books)
            if result:
                print(f'{len(result)} books found:')
                for book in result:
                    print(book)
            else:
                print('No books found.')
        elif choice == 2:
            isbn = input('Enter ISBN: ')
            result = search_book_by_isbn(isbn, books)
            if result:
                print(f"Title: {result['title']}, Price: {result['price']}")
            else:
                print('Book not found.')
        elif choice == 3:
            min_price = float(input('Enter minimum price: '))
            max_price = float(input('Enter maximum price: '))
            result = search_books_by_price_range(min_price, max_price, books)
            if result:
                print(f'{len(result)} books found:')
                for book in result:
                    print(book)
            else:
                print('No books found.')
        elif choice == 4:
            title = input('Enter title: ')
            author = input('Enter author: ')
            isbn = input('Enter ISBN: ')
            price = input('Enter price: ')
            new_book = {'title': title, 'author': author,
                        'ISBN': isbn, 'price': price}
            add_book(file_name, new_book)
            print('Book added successfully.')
        elif choice == 5:
            break
        else:
            print('Invalid choice. Try again.')


if __name__ == '__main__':
    main()
