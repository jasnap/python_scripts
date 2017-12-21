from binarytree import tree, bst, heap
from random import randint
import numpy as np
import itertools

my_tree = tree(height=3, is_perfect=True)
print my_tree

num_of_classes = randint(2, 5)
num_of_attr = randint(2, 5)
classes = [i for i in range(1, num_of_classes+1)]
print "number of classes: ", num_of_classes
print(my_tree.leaf_count)
print len(my_tree)
print "*****************************"


def is_child_leaf(node, a_tree):
    if(node.left is not None) or (node.right is not None):
        if (node.left in a_tree.leaves) or (node.right in a_tree.leaves):
            return False
        else:
            return True


def leaf_ptrs(node, a_tree):
    print "node is: ", node.value

    for i in a_tree.leaves:
        if node.left == i:
            temp1 = int("8"+ str(i.value%num_of_classes))
        if node.right == i:
            temp2 = int("8"+ str(i.value%num_of_classes))
    return temp1, temp2


def gen_vectors(a_tree):
    vector = []
    input = []
    j = 0
    for node in range(len(a_tree) - a_tree.leaf_count):
        #print a_tree[node].value
        attributes = np.random.randint(0, 255, num_of_attr)
        vector.append(attributes)
        vector = list(itertools.chain(*vector))
        vector.append(0)
        vector.append(randint(0, 255))
        if node == 1:
            vector.append(0)
            vector.append(1)
        else:
            if is_child_leaf(a_tree[node], a_tree):
                vector.append(0)
                vector.append(1)
            else:
                ptrs = leaf_ptrs(a_tree[node], a_tree)
                vector.append(ptrs[0])
                vector.append(ptrs[1])

        input.append(vector)
        print vector
        del vector[:]

    print input

gen_vectors(my_tree)

