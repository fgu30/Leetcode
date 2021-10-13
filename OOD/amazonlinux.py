__author__ = 'deepika'



class Filter:
    def __init__(self):
        pass

    def apply(self, file):
        pass

class SizeFilter(Filter):
    def __init__(self, size):
        self.size = size

    def apply(self, file):
        return file.size > self.size

class ExtensionFilter(Filter):
    def __init__(self, ext):
        self.extension = ext
    def apply(self, file):
        return file.extension == self.extension

class File:
    def __init__(self, name, size):
        self.name = name
        self.isDirectory = False if '.' in name else True
        self.size = size
        self.extension = name.split(".")[1] if '.' in name else ""
        self.children = []

    def __repr__(self):
        return "{" + self.name + "}"

class FileSystem:

    def __init__(self):
        self.filters = []

    def addFilter(self, f):

        if isinstance(f, Filter):
            self.filters.append(f)

    
    # This implementation is OR implementation of filter. 
    def traverse(self, root):

        result = []
        def traverseUtil(root, result):
            for r in root.children:
                if r.isDirectory:
                    traverseUtil(r, result)
                else:

                    for _f in self.filters:
                        if _f.apply(r):
                            print("result:", result)
                            result.append(r)
        #return result
        traverseUtil(root, result)
        return result

f1 = File("StarTrek.txt", 5)
f2 = File("StarWars.xml", 10)
f3 = File("JusticeLeague.txt", 15)
f4 = File("IronMan.txt", 9)
f5 = File("Spock.jpg", 1)
f6 = File("BigBangTheory.txt", 50)
f7 = File("MissionImpossible", 10)
f8 = File("BreakingBad", 11)
f9 = File("root", 100)

f9.children = [f7, f8]
f7.children = [f1, f2, f3]
f8.children = [f4, f5, f6]

filter1 = SizeFilter(5)
filter2 = ExtensionFilter("txt")

fs = FileSystem()
fs.addFilter(filter1)
fs.addFilter(filter2)
print(fs.traverse(f9))
