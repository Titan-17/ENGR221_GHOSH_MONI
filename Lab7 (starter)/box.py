import os, sys 

sys.path.append(os.path.dirname(__file__))

from myHashMap import MyHashMap
from entry import Entry

class Box:
    def __init__(self):
        # Initializes a Box object with an empty hash map
        # and populates it from a file
        # Input: None
        # Output: None
        self.nicknameMap = MyHashMap()
        self.populateBox()

    """
    Adds Entries to the Box from inputFile. Assume that each
    line in inputFile corresponds to an Entry.
    
    Input:
        inputFile (str) - filename containing entries (default 'entries.txt')
        Each line format: "<nickname> <species>"
    Output:
        None
    """
    def populateBox(self, inputFile='entries.txt'):
        with open(inputFile, 'r') as f:
            for line in f:
                nickname, species = line.split()
                self.add(nickname, species)

    """
    Create an Entry object with the given information and add it
    to the nicknameMap. 
    
    Input:
        nickname (str)
        species (str)
    Output:
        True  -> if entry is successfully added
        False -> if nickname already exists
    """
    def add(self, nickname, species):
        if self.nicknameMap.containsKey(nickname):
            return False
        entry = Entry(nickname, species)
        self.nicknameMap.put(nickname, entry)
        return True

    """
    Return a single Entry object with the given nickname and species.
    Should not modify the Box itself. 
    
    Input:
        nickname (str)
        species (str)
    Output:
        Entry object -> if match is found
        None         -> if no matching entry exists
    """
    def find(self, nickname, species):
        entry = self.nicknameMap.get(nickname)
        if entry is None:
            return None
        try:
            entry_species = entry.getSpecies()
        except AttributeError:
            entry_species = entry._Entry__species
        if entry_species == species:
            return entry
        return None

    """ 
    Return a list of nicknames representing all unique 
    nicknames in the Box. Should not modify the Box itself.
    
    Input:
        None
    Output:
        List[str] -> all nicknames
        []        -> if Box is empty
    """
    def findAllNicknames(self):
        return self.nicknameMap.keys()

    """ 
    Return an Entry with the given nickname. Should not modify
    the Box itself. 
    
    Input:
        nickname (str)
    Output:
        Entry object -> if found
        []           -> if nickname does not exist
    """
    def findEntryByNickname(self, nickname):
        entry = self.nicknameMap.get(nickname)
        return entry if entry is not None else []

    """
    Remove the Entry with the given nickname from the Box. 
    
    Input:
        nickname (str)
    Output:
        True  -> if removal successful
        False -> if nickname not found
    """
    def removeByNickname(self, nickname):
        return self.nicknameMap.remove(nickname)

    """ 
    Remove the Entry with the given nickname and species. 
    
    Input:
        nickname (str)
        species (str)
    Output:
        True  -> if matching entry removed
        False -> if not found or species mismatch
    """
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
    # Create a Box object (auto-loads entries from file)
    b = Box()

    # Expected Output:
    # List of nicknames loaded from entries.txt
    print("Initial nicknames:", b.findAllNicknames())
    print("Total loaded:", len(b.findAllNicknames()))

    # Expected Output:
    # True  -> if "Shadow" was not already in file
    # False -> duplicate nickname
    print("\nAdd new entry:")
    print("Add Shadow (Gengar):", b.add("Shadow", "Gengar"))
    print("Add duplicate Peeko (Wingull):", b.add("Peeko", "Wingull"))

    # Expected Output:
    # Entry object if exact match exists, otherwise None
    print("\nFind entries:")
    print("Find Volty Pikachu:", b.find("Volty", "Pikachu"))
    print("Find Volty Voltorb:", b.find("Volty", "Voltorb"))

    # Expected Output:
    # True/False depending on whether removal succeeded
    print("\nRemove entries:")
    print("RemoveByNickname Rocky:", b.removeByNickname("Rocky"))
    print("RemoveEntry Fluffy Mareep:", b.removeEntry("Fluffy", "Mareep"))

    # Expected Output:
    # Updated nickname list after removals
    print("\nFinal nicknames:", b.findAllNicknames())
    print("Total remaining:", len(b.findAllNicknames()))