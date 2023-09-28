

class Trie(object):
    """
    A custom implementation of the Trie data structure
    To store and retrieve strings efficiently
    """

    class TrieNode(object):
        """
        A custome implementation of a Trie Node
        to support the Trie implementation and 
        non-contiguous memory allocation
        """
        def __init__(self) -> None:
            self.word: str = None
            self.children: list[Trie.TrieNode] = [None for _ in range(26)]

    def __init__(self) -> None:
        self.root: Trie.TrieNode = Trie.TrieNode()

    def get_index(self, letter: str) -> int:
        """
        Returns the ASCII value of a given character by substracting it with ASCII value of letter "a"
        """
        return ord(letter) - ord("a")

    def insert(self, word: str) -> None:
        """
        Inserts a new word in this trie
        """
        # lower case given word to use the same 26 character to traverse and insert the trie
        lowercased_word: str = word.lower()
        self.insert_helper(lowercased_word)

    def insert_helper(self, word: str) -> None:
        """
        Helper function to insert a new word in this trie
        """
        current: Trie.TrieNode = self.root
        # traverse the trie using the character in the given word
        for letter in word:
            index: int = self.get_index(letter)
            if current.children[index] == None:
                current.children[index] = Trie.TrieNode()
            current = current.children[index]
        # insert new word
        current.word = word

    def get_word_list(self, prefix: str) -> list[str]:
        """
        Returns a list of strings in the trie that matches the given prefix
        """
        word_list: list[str] = []
        self.get_word_list_helper(prefix, word_list, self.root, 0)
        return word_list
    
    def get_word_list_helper(self, prefix: str, word_list: list[str], trie_node: TrieNode, i: int) -> None:
        # base case
        if trie_node != None:
            if i == len(prefix) - 1:
                # iterates through the children of the current node children while children is not None
                for child in trie_node.children:
                    if child != None and child.word != None:
                        word_list.append(child.word)
                    self.get_word_list_helper(prefix, word_list, child, i)
            else:
                # calculate the next index to visit
                index: int = self.get_index(prefix[i])
                if trie_node.children[index] != None and index == len(prefix) - 1 \
                    and trie_node.children[index].word != None:
                    word_list.append(trie_node.children[index].word)
                self.get_word_list_helper(prefix, word_list, trie_node.children[index], i + 1)

if __name__ == '__main__':
    instance: Trie = Trie()
    instance.insert("pie")
    instance.insert("treat")
    instance.insert("treasure")
    instance.insert("treatment")
    instance.insert("treacherous")
    instance.insert("apple")
    instance.insert("app")
    instance.insert("application")
    instance.insert("appreciate")
    instance.insert("appropriate")
    instance.insert("approach")

    word_list: list[str] = instance.get_word_list("app")

    print(word_list)

            