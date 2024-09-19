#Trie practice

class Node:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = Node()

    #Insert A word in trie
    def insert(self, word:str) -> None:
        node = self.root
        for x in word:
            if x not in node.children:
                node.children[x] = Node()
            node = node.children[x]
            node.is_end = True

    #search for a value
    def search(self, word):
        node = self.root
        for x in word:
            if x not in node.children:
                return print(word, "does not found in this Trie")
            node = node.children[x]
        print(node.is_end, word," found this Trie")

    # def delete(self, word):
    #     def delete_recu(node, word, index):
    #         if len(word) == index:
    #             if not node.is_end:
    #                 return False
    #             node.is_end = False
    #             return len(node.children) == 0
    #         char = word[index]
    #         if char not in node.children:
    #             return False
    #         delete_node = delete_recu(node.children[char], word, index+1)
    #
    #         if delete_node:
    #             del node.children[char]
    #             return len(node.children) == 0 and not node.is_end
    #         return False
    #     delete_recu(self.root, word, 0)

    def delete(self, words):
        def delete_recurse(node, word, index):
            if len(word) == index:
                if not node.is_end:
                    return False
                node.is_end = False
                return len(node.children) == 0

            char = word[index]
            if not node.children[char]:
                return False
            delete_node = delete_recurse(node.children[char], word, index + 1)

            if delete_node:
                del node.children[char]
                return len(node.children) == 0 and not node.is_end
            return False

        delete_recurse(self.root, words, 0)


tr = Trie()
tr.insert("shafeeque")
tr.insert("shahab")
tr.insert("shahabath")

tr.search("Shafeeque")
tr.delete("shafeeque")
tr.search('shafeeque')

