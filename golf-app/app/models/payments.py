""" This class is used to process the payout of a simple marks golf game
    This can be used for as many people as you need it for.
    The dataset is a list of lists
    data = [["Brad", -1], ["Mattie", 1], ["Jon", 1], ["Rocco", 0]]
"""
from typing import List, Dict, Optional

delimiter = "-"


def processdata(player1_name, player2_name, player1_marks, player2_marks, results):
    if player2_name != player1_name:  # process this record
        if player1_marks > player2_marks:
            # print(player2_name + delimiter + player1_name)
            # print(str(player1_marks - player2_marks))
            key = player2_name + delimiter + player1_name
            results[key] = str(player1_marks - player2_marks)

        elif player1_marks < player2_marks:
            # print(player1_name + delimiter + player2_name)
            # print(str(player2_marks - player1_marks))
            key = player1_name + delimiter + player2_name
            results[key] = str(player2_marks - player1_marks)


# We want to combine payments to like people as to eliminate and
# unnecessary payments
def crunchdata(name1, name2, name2_for_a, dataset):
    key1 = name1 + delimiter + name2_for_a
    key2 = name1 + delimiter + name2
    key3 = name2 + delimiter + name2_for_a

    if dataset.get(key1) and dataset.get(key2) and dataset.get(key3):
        value1 = int(dataset[key1])
        value2 = int(dataset[key2])
        value3 = int(dataset[key3])
        dataset[key1] = value1 + (value2 if (value3 - value2) > 0 else value3)
        dataset[key2] = 0 if (value2 - value3) < 0 else value2 - value3
        dataset[key3] = 0 if (value3 - value2) < 0 else value3 - value2


def calculate(dataset) -> Dict:
    results = {}
    arr_player1 = []
    arr_player2 = []
    player1s = []

    for player1 in dataset:
        player1s.append(player1)
        player1_name = player1[0]
        player1_marks = player1[1]
        for player2 in dataset:
            if player2 not in player1s:
                player2_name = player2[0]
                player2_marks = player2[1]
                processdata(
                    player1_name, player2_name, player1_marks, player2_marks, results
                )
    # print("RAW:")
    # print(results)
    keys = results.keys()
    # get name from keys and split them
    for names in keys:
        name = names.split(delimiter)
        arr_player1.append(name[0])
        arr_player2.append(name[1])

    # loop through player 2 array and determine if there is a record
    # in player 1 array with the same name.
    # If so then crunch the data
    for index2, name2 in enumerate(arr_player2):
        for index1, name1 in enumerate(arr_player1):
            if index2 != index1 and name2 == name1:
                crunchdata(arr_player1[index2], name2, arr_player2[index1], results)
    # print("CRUNCHED:")
    # print(results)
    # Remove entries with zero amounts. Clean the dictionary
    final_dict = {}
    for key, val in results.items():
        if int(val) > 0:
            newkey = key.replace(delimiter, " owes ")
            final_dict[newkey] = val

    print("FINAL:")
    print(final_dict)


# data = [["Brad", -1], ["Mattie", 1], ["Jon", 1], ["Rocco", 0]]
# data = [["Brad", -1], ["Mattie", -1], ["Jon", 1], ["Rocco", -2], ["Don", -3]]
# data = [["Brad", 2], ["Mattie", 1], ["Rocco", 2], ["Jon", -6]]
# calculate(data)
# compare to these results:
# {'Brad owes Mattie': 3, 'Brad owes Jon': ' 2', 'Rocco owes Jon': ' 1'}

#########python crap
# def fun_x(x):
#     x=x+'2'
#     x=x*2
#     return x
# print(fun_x("python"))


# x=[(3,2),(2,3)]
# x.sort()
# print(x)
