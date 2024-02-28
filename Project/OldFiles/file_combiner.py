import glob

class TheFile(object):

    def __init__(self):
        self.readfile()

    def getName(self):
        self.name_part = input("Sorting input: ")

    def readfile(self):
        nr_of_files = len(glob.glob("some/path/name/*.txt")) #counts
        for i in nr_of_files:
            self.filename = glob.iglob("some/path/name/*.txt") #iglob iteratively sorts through the dir.
            self.filecontent = open("demofile.txt", "r")

    def newName(self):
        new_file_name = str(name_part, "all")

    def combine():

