from data import *
from book import Book
#It would be better to call the Class stored in book.py directly. Using that method results in traceback call issues. 
#This code imports the data_list we are analyzing and the 'Book' Class we are using to compare several 
#similar yet distinct items in the data_list. 


def run_analysis(book_list):
    books = create_book_list(book_list)
    print('')
    print("*******************************************************************")
    print('')
    example_analysis(books)
    analysis_one(books)
    analysis_two(books)
    analysis_three(books)
    # print('')
    # print("*******************************************************************")
    # print('')
    # analysis_one(books)
    # print('')
    # print("*******************************************************************")
    # print('')
    # analysis_two(books)
    # print('')
    # print("*******************************************************************")
    # print('')
    # analysis_three(books)

def create_book_list(data_list):
    book_list = []
    # TODO: Write a function that will loop through data_list, and create a Book object for each list item
    for book_dict in data_list:
        new_book = Book(book_dict)
        book_list.append(new_book)
    # TODO: Then, add each Book item to book_list
    # TODO: Finally, return book_list for use in analysis questions!
    print(book_list)
    return book_list

def example_analysis(book_list):
    print("Analysis of which book had the highest price in 2016")
    # Find all books from 2016
    # Use a Lambda filter function to find books who have a year of 2016
    # Converting to a list, and saving as variable books_2016
    books_2016 = list(filter(lambda book: book.year == 2016, book_list))
    # Calculating the maximum price, and saving that book as highest_cost_book
    # Using max(), with Lambda function
    highest_cost_book = max(books_2016, key=lambda book: book.price)
    # Print that book's name & price to terminal
    print(
        f"The most expensive book in 2016 was {highest_cost_book.name} with a price of {highest_cost_book.price}")

def analysis_one(book_list):
    print("Analysis of which book had the lowest number of reviews in 2018")
    # Find all books from 2018
    # Use a Lambda filter function to find books who have a year of 2018
    # Converting to a list, and saving as variable books_2018
    books_2018 = list(filter(lambda book: book.year == 2018, book_list))
    # identifying lowest number of reviews in that year, saving as least_reviewed_book
    # using min(), with lambda function
    least_reviewed_book = min(books_2018, key=lambda book: book.number_of_reviews)
    print(
        f"The book that had the lowest number of reviews in 2018 was {least_reviewed_book.name}")

def analysis_two(book_list):
    print("Analysis of which genre (fiction or non-fiction) has appeared the most in the top 50's list")
    #Find all books on the best seller list from 1-50 using Lambda. 
    fiction_counts = sum(map(lambda book: book.genre == 'Fiction',book_list))
    non_fiction_counts = sum(map(lambda book: book.genre == 'Non Fiction',book_list))
    print('Number of Fiction books in the Top 50s list:',fiction_counts)
    print('Number of Non-Fiction books in the Top 50s list:',non_fiction_counts)
    #if fiction_counts > non_fiction_counts:
    #    print('There were more Fiction books than Nonfiction books om the Top 50 List for a total of',fiction_counts,'Fiction books')
    #    elif fiction_counts = non_fiction_counts
    #        print('The number of Fiction and Nonfiction books in the Top 50 List was',fiction_counts)
    #    elif non_fiction_counts > fiction_counts:
    #        print('There were more Non Fiction books than Fiction in the Top 50 List for a total of',non_fiction_counts,'Non Fiction books')
    #    break

def analysis_three(book_list):
    print("Analysis of which book has appeared the most in the top 50's list, and how many times it has appeared")
    
    list_of_years = set([book.year for book in book_list])
 
    print(list_of_years)

    for loop_year in list_of_years:
        books_specfic_to_year = [book for book in book_list if book.year == loop_year]

    
    #list(filter(lambda book: book.year == 2018, book_list))
    # Create a list of lists
        # This list will contain lists for every year
        # Each year list, will conatin all of the books in that year
        # Removed duplicate values from each year list
    # Recombine all of the distinct year lists together
    # Count which book shows up the most

    #unique_books = top50_list['title']
    #uniqueValues = empDfObj['title'].unique()
    
    #print(uniqueValues)
    
    #unique_books = 0
    #for item in top50_list:
    #    if item not in unique_books:
    #        unique_books.append(int(item))
    #        unique_books +=1
    #print(unique_books)
# BONUS USER STORIES:


def bonus_analysis_one(book_list):
    print("Analysis of which author has shown up on the top 50's list the most (Distinct books only!)")


def bonus_analysis_two(book_list):
    print("Analysis of the top book for each year, based on the book's user ratings and number of reviews")


def bonus_analysis_three(book_list):
    print("Analysis of which book has appeared the most consecutively on top 50's list")


run_analysis(data_list)
