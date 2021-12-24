# Creating a node class
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    # Adding a child node in the tree
    def add_child(self, child):
        child.parent = self
        self.children.append(child)

def build_product_tree():
    root = TreeNode('Electronics')

    Laptop = TreeNode('Laptop')
    Laptop.add_child(TreeNode('Mac'))
    Laptop.add_child(TreeNode('Surface'))
    Laptop.add_child(TreeNode('Thinkpad'))

    cellPhone = TreeNode('Cell Phone')
    cellPhone.add_child(TreeNode('iphone'))
    cellPhone.add_child(TreeNode('Google Pixel'))
    cellPhone.add_child(TreeNode('Vivo'))

    tv = TreeNode('TV')
    tv.add_child(TreeNode('Samsung'))
    tv.add_child(TreeNode('LG'))
    tv.add_child(TreeNode('Sony'))

    root.add_child(Laptop)
    root.add_child(cellPhone)
    root.add_child(tv)
    
    return root

if __name__ : '__main__'
root = build_product_tree()

print(root)