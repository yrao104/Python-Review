#when two classes have same method names & attributes, they implement the same interface
#interface in Python usually refers to names of methods and arguments they take

#these two classes both implement the same method names and attributes, so they share the same interface
'''
class Chess:
    def __init__(self):
        self.board = setup_board()
        self.piece = add_chess_pieces()

    def play(self):
        print("Playing chess!")


class Checkers:
    def __init__(self):
        self.board = setup_board()
        self.piece = add_chess_pieces()

    def play(self):
        print("Playing checkers!")
'''

'''
Polymorphism is an abstract concept that covers a lot of ground, but defining class hierarchies that all
implement the same interface is a way of introducing polymorphism to our code
'''