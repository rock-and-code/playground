from data_structures import Trie
import unittest

class TrieTest(unittest.TestCase):
    """
    A unit test for the Trie class
    """
    def test_get_word_list(self) -> None:
        print("#" * 5  + " Testing insert and get word list method " + "#" * 5)
        instance: Trie = Trie()
        instance.insert("pie")
        instance.insert("treat")
        instance.insert("treasure")
        instance.insert("treatment")
        instance.insert("treacherous")
        instance.insert("app")
        instance.insert("apple")
        instance.insert("application")
        instance.insert("appreciate")
        instance.insert("appropriate")
        instance.insert("approach")
        prefix: str = "app"
        expResult: list[str] = ["app", "apple", "application", "appreciate", "approach", "appropriate"]
        word_list: list[str] = instance.get_word_list(prefix)
        print(f"ge_word_list({prefix}) -> {word_list}")
        self.assertEqual(expResult, word_list)

if __name__ == "__main__":
    unittest.main()