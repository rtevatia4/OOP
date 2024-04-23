"""
The Movie class has an interface with public methods for communication.

The private members (variables or functions) cannot be accessed directly from the outside, 
but public read and write functions allow access to them. This, in essence, is data encapsulation.
"""
class Movie:
    def __init__(self, title=None, year=None, genre=None):
        self.__title = title
        self.__year = year
        self.__genre = genre
    
    def get_title(self):
        return self.__title

    def get_year(self):
        return self.__year

    def get_genre(self):
        return self.__year
    
    def set_title(self, title):
        self.__title = title

    def set_year(self, year):
        self.__year = year

    def set_genre(self, genre):
        self.__genre = genre

    def display(self):
        print("Movie Title:", self.__title)
        print("Movie Year:", self.__year)
        print("Movie Genre:", self.__genre)

if __name__ == "__main__":
    movie = Movie("Forest Gump", 1994, "Drama")
    movie.display()
