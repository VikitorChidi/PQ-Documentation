{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [],
   "source": [
    "class BinarySearchTreeNode:\n",
    "    def __init__(self, key):\n",
    "        self.key = key\n",
    "        self.left = None\n",
    "        self.right = None\n",
    "\n",
    "    def add_child(self, key):\n",
    "        if key == self.key: #Bst can't have duplicate\n",
    "            return\n",
    "        \n",
    "        if key < self.key:\n",
    "            # add key in left subtree\n",
    "            if self.left: #if element in left subtree has some value. Not a leave node.\n",
    "                self.left.add_child(key)\n",
    "            else:\n",
    "                self.left = BinarySearchTreeNode(key)\n",
    "        else:\n",
    "            if self.right:\n",
    "                self.right = BinarySearchTreeNode(key)\n",
    "            else:\n",
    "                # add key in right subtree\n",
    "                self.right = BinarySearchTreeNode(key)\n",
    "    \n",
    "    def in_order_traversal(self):\n",
    "        elements = []\n",
    "\n",
    "        # visit left tree\n",
    "        if self.left:\n",
    "            elements += self.left.in_order_traversal()\n",
    "        \n",
    "        #visit base  node\n",
    "        elements.append(self.key)\n",
    "\n",
    "        #visit right tree\n",
    "        if self.right:\n",
    "            elements += self.right.in_order_traversal()\n",
    "\n",
    "        return elements\n",
    "    \n",
    "    def search(self, val):\n",
    "        if self.key == val:\n",
    "            return True\n",
    "        if val < self.key:\n",
    "            if self.left:\n",
    "                self.left.search(val)\n",
    "            else:\n",
    "                return False\n",
    "        if val > self.key:\n",
    "            if self.right:\n",
    "                self.right.search(val)\n",
    "            else:\n",
    "                return False\n",
    "\n",
    "def build_tree(elements):\n",
    "    root = BinarySearchTreeNode(elements[0])\n",
    "\n",
    "    for i in range(1, len(elements)):\n",
    "        root.add_child(elements[i])\n",
    "\n",
    "    return root"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "None\n"
     ]
    }
   ],
   "source": [
    "numbers = [17, 4, 1, 20, 9, 23, 18, 34]\n",
    "numbers_tree = build_tree(numbers)\n",
    "print(numbers_tree.search(34))"
   ]
  }
 ],
 "metadata": {
  "interpreter": {
   "hash": "280c69e192096dbf5e0114d23531d05abe687d28e6fdd5e808a52b9bd3aa5d06"
  },
  "kernelspec": {
   "display_name": "Python 3.9.6 64-bit",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.6"
  },
  "orig_nbformat": 4
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
