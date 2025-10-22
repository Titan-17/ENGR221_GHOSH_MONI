import os, sys 

sys.path.append(os.path.dirname(__file__))

from myHashMap import MyHashMap
from entry import Entry

class Box:
    def __init__(self):
        self.nicknameMap = MyHashMap()
        self.populateBox()

    """
    Adds Entries to the Box from inputFile. Assume that each
    line in inputFile corresponds to an Entry."""
    def populateBox(self, inputFile='entries.txt'):
        # Open the file as read only
        with open(inputFile, 'r') as f:
            # Add each value in the file as an Entry to the Box
            for line in f:
                # Set the first word in the line as the nickname, and
                # the second as species
                nickname, species = line.split()
                # Add the new entry to the Box
                self.add(nickname, species)

    """
    Create an Entry object with the given information and add it
    to the nicknameMap. 
    Returns true if the Entry is successfully added to the Box, and
    false if the nickname already exists in the Box. """
    def add(self, nickname, species):
        if self.nicknameMap.containsKey(nickname):
            return False
        entry = Entry(nickname, species)
        self.nicknameMap.put(nickname, entry)
        return True

    """
    Return a single Entry object with the given nickname and species.
    Should not modify the Box itself. 
    Return None if the Entry does not exist in the Box. """
    def find(self, nickname, species):
        entry = self.nicknameMap.get(nickname)
        if entry is None:
            return None
        # Prefer accessor if present; otherwise fall back to name-mangled attr
        try:
            entry_species = entry.getSpecies()
        except AttributeError:
            entry_species = entry._Entry__species
        if entry_species == species:
            return entry
        return None

    """ 
    Return a list of nickanames representing all unique 
    nicknames in the Box. Should not modify the Box itself.
    Return an empty list if the Box is empty. """
    def findAllNicknames(self):
        return self.nicknameMap.keys()

    """ 
    Return an Entry with the given nickname. Should not modify
    the Box itself. 
    Return an empty list if the nickname is not in the Box. """
    def findEntryByNickname(self, nickname):
        entry = self.nicknameMap.get(nickname)
        return entry if entry is not None else []

    """
    Remove the Entry with the given nickname from the Box. 
    Return true if successful, or false otherwise."""
    def removeByNickname(self, nickname):
        return self.nicknameMap.remove(nickname)

    """ 
    Remove the Entry with the given nickname and species. 
    Return true if successful, or false otherwise. """
    def removeEntry(self, nickname, species):
        entry = self.nicknameMap.get(nickname)
        if entry is None:
            return False
        try:
            entry_species = entry.getSpecies()
        except AttributeError:
            entry_species = entry._Entry__species
        if entry_species == species:
            return self.nicknameMap.remove(nickname)
        return False

if __name__ == '__main__':
    b = Box()

    print("Initial nicknames:", b.findAllNicknames())
    print("Total loaded:", len(b.findAllNicknames()))

    print("\nAdd new entry:")
    print("Add Shadow (Gengar):", b.add("Shadow", "Gengar"))
    print("Add duplicate Peeko (Wingull):", b.add("Peeko", "Wingull"))

    print("\nFind entries:")
    print("Find Volty Pikachu:", b.find("Volty", "Pikachu"))
    print("Find Volty Voltorb:", b.find("Volty", "Voltorb"))

    print("\nRemove entries:")
    print("RemoveByNickname Rocky:", b.removeByNickname("Rocky"))
    print("RemoveEntry Fluffy Mareep:", b.removeEntry("Fluffy", "Mareep"))

    print("\nFinal nicknames:", b.findAllNicknames())
    print("Total remaining:", len(b.findAllNicknames()))
