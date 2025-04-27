# Data Structure: BST()

Background: A Binary Search Tree (or BST) is a data structure used for organizing and storing data in a sorted manner. Each node in a Binary Search Tree has at most two children, a left child and a right child, with the left child containing values less than the parent node and the right child containing values greater than the parent node.

### Functions
get_item() - Returns the item stored in the current node.

insert() - Inserts a new item into the BST, maintaining the BST property (overloaded).\
add() - Inserts a new item into the BST, maintaining the BST property (overloaded).

display() - Prints the BST structure with indentation.

sum_at_depth() - Returns the sum of all nodes at a given depth.

find_depth_of_item() - Returns the depth of a specified item, or -1 if not found.

smallest() - Returns the smallest item in the BST.

largest() - Returns the largest item in the BST.

find() - Returns True if a specified item exists in the BST, False otherwise.

print_at_depth() - Prints all nodes at a given depth.

sum_of_nodes() - Returns the sum of all items in the BST.

num_of_nodes() - Returns the total number of nodes in the BST.

extract_to_list() - Extracts all items from the BST into a sorted list.

build_BST() - Builds a balanced BST from a sorted list.

height() - Returns the height of the BST.

preorder_iter() - Performs an iterative preorder traversal and returns the visited nodes.

inorder_iter() - Performs an iterative inorder traversal and returns the visited nodes.

postorder_iter() - Performs an iterative postorder traversal and returns the visited nodes.

lowest_common_ancestor() - Finds the lowest common ancestor of two nodes (by value).

kth_num() - Returns the kth smallest element in the BST.
