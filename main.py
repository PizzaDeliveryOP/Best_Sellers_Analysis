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
    analysis_one(book_list)
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
    # Find all books from 2018
    # Use a Lambda filter function to find books who have a year of 2018
    # Converting to a list, and saving as variable books_2018
    books_2018 = list(filter(lambda book: book.year == 2018, book_list))
    # identifying lowest number of reviews in that year, saving as least_reviewed_book
    # using min(), with lambda function
    least_reviewed_book = min(books_2018, key=lambda book: book.number_of_reviews)

    print(
        f"Analysis of which book had the lowest number of reviews in 2018, the book was {least_reviewed_book.name}")


def analysis_two(book_list):
    print("Analysis of which genre (fiction or non-fiction) has appeared the most in the top 50's list")


def analysis_three(book_list):
    print("Analysis of which book has appeared the most in the top 50's list, and how many times it has appeared")


# BONUS USER STORIES:


def bonus_analysis_one(book_list):
    print("Analysis of which author has shown up on the top 50's list the most (Distinct books only!)")


def bonus_analysis_two(book_list):
    print("Analysis of the top book for each year, based on the book's user ratings and number of reviews")


def bonus_analysis_three(book_list):
    print("Analysis of which book has appeared the most consecutively on top 50's list")


run_analysis(data_list)