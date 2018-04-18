from Kingdom import Kingdoms

kingdom = Kingdoms()


class Classifier:
    result = "Success"
    element = ""

    @staticmethod
    def coder(text):
        text_list = []
        for t in text.split(","):
            text_list.append(t.strip(" ").strip("\""))
        Classifier.element = text_list[0]
        k = kingdom.get_kingdom(text_list[0])
        text_list[0] = k
        return text_list

    @staticmethod
    def word_counter(lis):
        counter_dict = {}
        for i in lis:
            if i not in counter_dict.keys():
                counter_dict[i.lower()] = 1
            else:
                counter_dict[i.lower()] += 1
        return counter_dict

    def checker(self, text):
        verifier = Classifier.word_counter(Classifier.coder(text)[0])
        code = Classifier.word_counter(Classifier.coder(text)[1])
        for letter in verifier.keys():
            if letter in code.keys() and code[letter] >= verifier[letter]:
                continue
            else:
                self.result = "Failed"
                break
        if self.result == "Success":
            return self.element
        else:
            return None

