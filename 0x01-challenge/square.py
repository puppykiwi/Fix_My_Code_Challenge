#!/usr/bin/python3

class Square():
    
    width = 0
    height = 0

    def __init__(self, *args, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def area_of_my_square(self):
        """ Area of the square """
        return self.width * self.width

    def perimeter_of_my_square(self):
        """ Perimeter of the square """
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        square_str = ''
        for _ in range(self.height):
            square_str += '#' * self.width + '\n'
        return square_str

if __name__ == "__main__":
    s = Square(width=4, height=4)
    print(s)
    print(s.area_of_my_square())
    print(s.perimeter_of_my_square())
