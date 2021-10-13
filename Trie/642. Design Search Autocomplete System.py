class TrieNode():
    
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.times = 0
        
class Trie():
    
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, sentence, times):
        root = self.root
        for c in sentence:
            root = root.children[c]
        root.times += times
        
    def lookup(self, root, sentence):
        def dfs(root, path):
            if root.times > 0:
                res.append((path, root.times))
            for c in root.children:
                dfs(root.children[c], path+c)
        
        root = self.root
        path = ""
        for c in sentence:
            if c not in root.children:
                return []
            root = root.children[c]
            path += c

        res = []
        dfs(root, path)
        return res
        
class AutocompleteSystem(object):

    def __init__(self, sentences, times):
        """
        :type sentences: List[str]
        :type times: List[int]
        """
        self.trie = Trie()
        for i in range(len(sentences)):
            self.trie.insert(sentences[i], times[i])
        self.sentence = ""

    def input(self, c):
        """
        :type c: str
        :rtype: List[str]
        """
        n = 3 # return top 3 results
        if c=="#":
            self.trie.insert(self.sentence, 1)
            self.sentence = ""
            return []
        else:
            self.sentence += c
            res = self.trie.lookup(self.trie.root, self.sentence)
            return [x[0] for x in sorted(res, key=lambda x: (-x[1], x[0]))][:n]


# Your AutocompleteSystem object will be instantiated and called as such:
# obj = AutocompleteSystem(sentences, times)
# param_1 = obj.input(c)
