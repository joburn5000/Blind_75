"""
A trie (pronounced as "try") or prefix tree is a tree data 
structure used to efficiently store and retrieve keys in a 
dataset of strings. There are various applications of this 
data structure, such as autocomplete and spellchecker.

Implement the Trie class:

Trie() Initializes the trie object.

void insert(String word) Inserts the string word into the 
trie.

boolean search(String word) Returns true if the string word 
is in the trie (i.e., was inserted before), and false otherwise.
boolean startsWith(String prefix) Returns true if there is a 
previously inserted string word that has the prefix prefix, 
and false otherwise.
 

Example 1:

Input
["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
[[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
Output
[null, null, true, false, true, null, true]

Explanation
Trie trie = new Trie();
trie.insert("apple");
trie.search("apple");   // return True
trie.search("app");     // return False
trie.startsWith("app"); // return True
trie.insert("app");
trie.search("app");     // return True
 

Constraints:

1 <= word.length, prefix.length <= 2000
word and prefix consist only of lowercase English letters.
At most 3 * 104 calls in total will be made to insert, search, and startsWith.

Difficulty: Medium
Completed: 7/4/2022
"""

class TrieNode:
    def __init__(self, char = ""):
        self.char = char
        self.children = {}
        self.end = False

class Trie:
    # initialize the root as ""
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word: str) -> None:
        # temp node
        node = self.root
        for char in word:
            # if the char is found in the children, we don't need to create a new node
            if char in node.children:
                node = node.children[char]
            else:
                # create a new child node
                new_node = TrieNode(char)
                node.children[char] = new_node
                node = new_node
        # mark that that node is the end of the entry
        node.end = True
        

    def search(self, word: str) -> bool:
        node = self.root
        for char in word:
            # if it is not in children, the entry is not found in the trie
            if char not in node.children:
                return False
            # increment the node
            node = node.children[char]
        # must be the end of the entry
        return node.end
        

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        # must not necessarily be the end of the entry
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

"""
Explanation:

A trie starts with "" and its children are all the first letters
of the words. For each node in the children of "", that node's 
children are all the second letters that start with the node's
letter, and so on.

Time Complexity: O(N)
Space Complexity: O(1)
"""
