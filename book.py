# TODO: Create a Book class with the following instance variables:
# name
# author
# user_rating
# number_of_reviews
# price
# year
# genre


class Book:
    def __init__(self, singular_book):
        self.id = singular_book['id']
        self.name = singular_book['name']
        self.author = singular_book['author']
        self.user_rating = singular_book['user_rating']
        self.number_of_reviews = singular_book['number_of_reviews']
        self.price = singular_book['price']
        self.year = singular_book['year']
        self.genre = singular_book['genre']
    pass
