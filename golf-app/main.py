""" The main starting point for the application
"""

from app.models.payments import calculate


def start_app():
    """ calculate() will take in a List of Lists
    INPUT: Each List contains the golfer's name and their net chip count
    OUTPUT: Dictionary with golfer's name and what they owe to whom
    """
    data = [["Brad", 2], ["Mattie", 1], ["Rocco", 2], ["Jon", -6]]
    calculate(data)


if __name__ == "__main__":
    start_app()
