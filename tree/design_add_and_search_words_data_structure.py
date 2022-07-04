"""
Design a data structure that supports adding new words and 
finding if a string matches any previously added string.

Implement the WordDictionary class:

WordDictionary() Initializes the object.
void addWord(word) Adds word to the data structure, it can 
be matched later.
bool search(word) Returns true if there is any string in the 
data structure that matches word or false otherwise. word may 
contain dots '.' where dots can be matched with any letter.
 

Example:

Input
["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
[[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]
Output
[null,null,null,null,false,true,true,true]

Explanation
WordDictionary wordDictionary = new WordDictionary();
wordDictionary.addWord("bad");
wordDictionary.addWord("dad");
wordDictionary.addWord("mad");
wordDictionary.search("pad"); // return False
wordDictionary.search("bad"); // return True
wordDictionary.search(".ad"); // return True
wordDictionary.search("b.."); // return True
 

Constraints:

1 <= word.length <= 25
word in addWord consists of lowercase English letters.
word in search consist of '.' or lowercase English letters.
There will be at most 3 dots in word for search queries.
At most 104 calls will be made to addWord and search.
Accepted
415,996
Submissions
949,675

Difficulty: Medium
Completed: 7/4/2022
"""

class TrieNode:
    def __init__(self, char=""):
        self.char = char
        self.children = {}
        self.end = False
        
class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for char in word:
            if char in node.children:
                node = node.children[char]
            else:
                new_node = TrieNode(char)
                node.children[char] = new_node
                node = new_node
        node.end = True

    def recursion(self, node, word):
        if not word: return node.end
        if word[0] == ".":
            for child in node.children:
                if self.recursion(node.children[child], word[1:]): return True
        elif word[0] in node.children:
            if self.recursion(node.children[word[0]], word[1:]): return True
        return False
    
    def search(self, word: str) -> bool:
        return self.recursion(self.root, word)
                    


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)

"""
Explanation:

We use a similar concept to Trie - see 
https://github.com/joburn5000/blind_75_challenge/blob/main/tree/implement_trie.py

The only difference in this problem is the option for "." to subsitute a letter.
To implement this difference, we make a function "recursion" that searches if a given
word is found in a given node. It has the feature that if the first letter of the word
is "." then we check all the children of that node.


Time Complexity: O(N)
Space Complexity: O(1)
"""
