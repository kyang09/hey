import random

# A class to represent a node in the hi tree.
class CharNode:
    def  __init__(self, nchar="", isWord=False, nextNodes={}):
        self.character = nchar
        self.isWord = isWord
        self.nextNodes = nextNodes

# Build the hi tree.
def buildWordTree(words):
    root_node = CharNode()
    for word in words:
        cur_node = root_node
        for c in word:
            if c not in cur_node.nextNodes:
                cur_node.nextNodes[c] = CharNode(c, False, {})
            cur_node = cur_node.nextNodes[c]
        cur_node.isWord = True
    return root_node

# Get a random word in the tree.
def getRandomWord(root_node):
    word = ""
    cur_node = root_node
    continue_search = random.choice([True, False])
    while (not cur_node.isWord or continue_search) and cur_node.nextNodes != {}:
        word += cur_node.character
        random_choice = random.choice(cur_node.nextNodes.keys())
        cur_node = cur_node.nextNodes[random_choice]
    word += cur_node.character
    return word

# Just used this to check if words actually existed in the tree.
def checkWordExists(root_node, word):
    cur_node = root_node
    for c in word:
        if c not in cur_node.nextNodes:
            return False
        cur_node = cur_node.nextNodes[c]      
    return True


def main():
    # A simple way to say hi, a slightly cooler way to say hi, and a whole tree of ways to say hi.
    words = ["hi", "hey", "heya", "heyo", "hiyo", "hiya", "hello", "howdy"];
    print("%s %s %s %s" % ("hi", random.choice(words), getRandomWord(buildWordTree(words)), "007. Agent 007."))
    
if __name__ == "__main__":
    main()