from Kingdom import Kingdoms
from Classifier import Classifier

if __name__ == '__main__':
    classifier = Classifier()
    allies = set([])
    counter = 0
    while counter <= 4:
        length = allies.__len__()
        question = input()
        if length == 0 and counter == 0 and question == "Ruler?":
            print("None1")
            counter += 1
        elif length == 0 and counter == 1 and question == "Allies?":
            print("None2")
            counter += 1
        elif counter == 2:
            condition = True
            while condition:
                ally_input = input("Input: ")
                if ally_input is "":
                    condition = False
                    counter += 1
                    break
                else:
                    ally = classifier.checker(ally_input)
                    allies.add(ally)
        elif length > 0 and counter == 3 and question == "Ruler?":
            print("King Shan")
            counter += 1
        elif length > 0 and counter == 4 and question == "Allies?":
            if None in allies:
                allies.remove(None)
            print(', '.join(allies))
            counter += 1
        else:
            print("Wrong question bugger")
