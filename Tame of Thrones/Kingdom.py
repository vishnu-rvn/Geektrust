class Kingdoms:
    kingdom = ""

    def __str__(self):
        return "Five Kingdoms of Southeros"

    def get_kingdom(self, element):
        switcher = {
            "Air": "Owl",
            "Land": "Panda",
            "Water": "Octopus",
            "Ice": "Mammoth",
            "Fire": "Dragon",
            "Space": "Gorilla"
        }
        self.kingdom = switcher.get(element, "Your kingdom does not exist")
        return self.kingdom

