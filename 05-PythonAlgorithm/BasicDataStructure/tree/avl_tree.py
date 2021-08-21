#!/Users/tnt/Documents/虚拟环境/Py4E/bin/python3
# -*- encoding: utf-8 -*-
# Time  : 2021/07/14 20:25:39
# Theme : avl树
#! /usr/bin/python3
# -*- coding:utf-8 -*-
from collections.abc import MutableSequence
from copy import deepcopy


AUTHER = 'ArianX'
GITHUB = 'https://github.com/Arianxx'
BLOG = 'https://arianx.me'


class Node:
    """
    Pure binary tree's node.
    """

    def __init__(self, key):
        """
        Build the node instance.

        @param key: The object that implements the __lt__ and __gt__ method.
        """
        self.key = key
        self.count = 1
        self.left = None
        self.right = None
        self.parent = None

    def __repr__(self):
        return 'Node({key})'.format(key=self.key)

    def is_root(self):
        """
        Is this is the root node.(have not parent node)
        """
        return bool(self.parent)

    def is_leaf(self):
        """
        Is this is a leaf node.(have not any left or right point)
        """
        return not bool(self.left) and not bool(self.right)

    def is_branch(self):
        """
        Is this is a branch node.(have the left point or right point)
        """
        return bool(self.left) ^ bool(self.right)


class BiTree:
    Node = Node

    """
    The Binary Tree's main object. Should include a Node property to
    directly assign which class should be used as the ndoe.
    """

    def __init__(self, args=None):
        """
        @param args: A iterable object whose element
                                will be inserted in the tree later.
        """
        self.root = None
        self.size = 0

        if args:
            for arg in args:
                self.insert(arg)

    def __repr__(self):
        return 'BiTree<root={root}, size={size}>'.format(
            root=self.root,
            size=self.size)

    def __add__(self, tree):
        return self.merge(tree)

    def __iadd__(self, tree):
        for node in tree.as_list(0):
            self.insert(node)
        return self

    def __lt__(self, tree):
        return self.size < tree.size

    def __gt__(self, tree):
        return self.size > tree.size

    def __le__(self, tree):
        return self.size <= tree.size

    def __ge__(self, tree):
        return self.size >= tree.size

    def __iter__(self):
        return self

    def __next__(self):
        if not getattr(self, "Iterator", None):
            self.Iterator = iter(self.as_list(0))
        try:
            return next(self.Iterator)
        except StopIteration:
            self.Iterator = iter(self.as_list(0))
            raise

    def _insert(self, key, node):
        """
        The `insert` method's inside implemention whose arguments
        should always include `node` directly.

        @param key: A object that implement
                    the __lt__ mehtod and __gt__ method.
        @param node: A node which is in this tree. The `key` arguments
                    will be inserted along the node chain.
        """
        if not node:
            self.root = self.Node(key)
            self.size = 1
            return self.root

        new_node = None
        if key < node.key:
            if node.left:
                new_node = self._insert(key, node.left)
            else:
                new_node = self.Node(key)
                new_node.parent = node
                node.left = new_node
                self.size += 1
        elif key > node.key:
            if node.right:
                new_node = self._insert(key, node.right)
            else:
                new_node = self.Node(key)
                new_node.parent = node
                node.right = new_node
                self.size += 1
        else:
            node.count += 1

        return new_node

    def _lookup(self, key, node):
        """
        The `lookup` method's inside implemention like the `_insert` method.
        """
        if not node:
            return False

        if key < node.key:
            return self._lookup(key, node.left)
        elif key > node.key:
            return self._lookup(key, node.right)
        else:
            return node

    def insert(self, key, node=None):
        """
        Insert the `key` to the tree along the `node`.

        @param key: A object that can be compared.
        @param node: The first node of the subtree
                                that will be searched to insert the `key`.
        """
        if not node:
            node = self.root

        return self._insert(key, node)

    def lookup(self, key, node=None):
        """
        Similar to the `insert` method but for searching.
        """
        if not node:
            node = self.root

        return self._lookup(key, node)

    def as_list(self, arrow):
        """
        Traverse the tree by different mode to get a list
        which include all of the node's data in this tree.

        @param arrow:  The mode's code for traversing.
                                   -1 for preorder
                                    0 for inorder
                                    1 for postorder
                                    2 for tier order
        """
        if arrow == -1:
            return self.preorder()
        elif arrow == 0:
            return self.inorder()
        elif arrow == 1:
            return self.postorder()
        elif arrow == 2:
            return self.tierorder()
        else:
            raise ValueError("arrow must in [-1, 0 ,1]")

    def preorder(self, node=None, result=None):
        if not self.root:
            return False
        elif not node:
            node = self.root

        if not isinstance(result, MutableSequence):
            result = []

        result.append(node.key)
        if node.left:
            self.preorder(node.left, result)
        if node.right:
            self.preorder(node.right, result)

        return result

    def inorder(self, node=None, result=None):
        if not self.root:
            return False
        elif not node:
            node = self.root

        if not isinstance(result, MutableSequence):
            result = []

        if node.left:
            self.inorder(node.left, result)
        result.append(node.key)
        if node.right:
            self.inorder(node.right, result)

        return result

    def postorder(self, node=None, result=None):
        if not self.root:
            return False
        elif not node:
            node = self.root

        if not isinstance(result, MutableSequence):
            result = []

        if node.left:
            self.postorder(node.left, result)
        if node.right:
            self.postorder(node.right, result)
        result.append(node.key)

        return result

    def tierorder(self, node_list=None, result=None):
        if not self.root:
            return False
        elif not node_list:
            node_list = [self.root]

        if not isinstance(result, MutableSequence):
            result = []

        tier_result = []
        for node in list(node_list)[::-1]:
            tier_result.append(node.key)
            node_list.pop()
            if node.left:
                node_list.insert(0, node.left)
            if node.right:
                node_list.insert(0, node.right)
        result.append(tier_result)

        if node_list:
            self.tierorder(node_list, result)

        return result

    def merge(self, tree):
        """
        Merge two binary tree by inserting
        the every node of the tree to another tree.
        """
        nodes = self.as_list(0)
        new_tree = deepcopy(tree)
        for node in nodes:
            new_tree.insert(node)
        return new_tree


class AvlNode(Node):
    """
    The binary searching tree. Inherit from theo `Node` class.
    """

    def __init__(self, key):
        super().__init__(key)
        self.height = 0

    def __repr__(self):
        return 'AvlNode(key={key})'.format(key=self.key)

    @property
    def max_child_height(self):
        """
        The leaf node's height is 0. So the null node's height is -1.
        """
        return max(self.left.height if self.left else -1,
                   self.right.height if self.right else -1)

    def adjust_height(self):
        """
        Search from this node to its ancestor node
        until the height doesn't change.
        """
        old_height = self.height
        self.height = self.max_child_height + 1
        if self.height != old_height and self.parent:
            self.parent.adjust_height()

    @property
    def balance(self):
        """
        The null node's height is deemed as -1.
        """
        return (self.left.height if self.left else -1) \
            - (self.right.height if self.right else -1)


class AvlBiTree(BiTree):
    Node = AvlNode

    """
    The AVL Binary Tree's main object.
    """

    def __repr__(self):
        return 'AvlBiTree<root={root}, size={size}, height={height}>'.format(
            root=self.root,
            size=self.size,
            height=self.height)

    @property
    def height(self):
        return self.root.height + 1 if self.root else 0

    def __ll_rotate(self, node):
        """
        SHOULDN'T be directly invoked by user in any cases.
        It will lead to the breakings of the balance if pass a error node
        which shouldn't be rotated.
        """
        parent = node.parent
        left = node.left
        left_right = left.right

        left.right = node
        node.parent = left

        node.left = left_right
        if left_right:
            left_right.parent = node

        if not parent:
            self.root = left
            left.parent = None
        else:
            if parent.left == node:
                parent.left = left
            else:
                assert(parent.right == node)
                parent.right = left
            left.parent = parent

        node.adjust_height()
        left.adjust_height()

    def __lr_rotate(self, node):
        parent = node.parent
        left = node.left
        left_right = left.right

        left.right = left_right.left
        if left_right.left:
            left_right.left.parent = left

        left_right.left = left
        left.parent = left_right

        node.left = left_right.right
        if left_right.right:
            left_right.right.parent = node

        left_right.right = node
        node.parent = left_right

        if not parent:
            self.root = left_right
            left_right.parent = None
        else:
            if parent.left == node:
                parent.left = left_right
            else:
                assert(parent.right == node)
                parent.right = left_right
            left_right.parent = parent

        node.adjust_height()
        left.adjust_height()

    def __rr_rotate(self, node):
        parent = node.parent
        right = node.right
        right_left = right.left

        right.left = node
        node.parent = right

        node.right = right_left
        if right_left:
            right_left.parent = node

        if not parent:
            self.root = right
            right.parent = None
        else:
            if parent.left == node:
                parent.left = right
            else:
                assert(parent.right == node)
                parent.right = right
            right.parent = parent

        node.adjust_height()
        right.adjust_height()

    def __rl_rotate(self, node):
        parent = node.parent
        right = node.right
        right_left = right.left

        right.left = right_left.right
        if right_left.right:
            right_left.right.parent = right

        node.right = right_left.left
        if right_left.left:
            right_left.left.parent = node

        right_left.right = right
        right.parent = right_left

        right_left.left = node
        node.parent = right_left

        if not parent:
            self.root = right_left
            right_left.parent = None
        else:
            if parent.left == node:
                parent.left = right_left
            else:
                assert(parent.right == node)
                parent.right = right_left
            right_left.parent = parent

        node.adjust_height()
        right.adjust_height()

    def __remove_leaf(self, node):
        """
        SHOULDN'T be directly invoked by user in any cases
        because it will lead to the breakings of the balance.
        """
        assert(node.is_leaf())
        if not node.parent:
            self.root = None
            self.size = 0
        else:
            if node.parent.left == node:
                node.parent.left = None
            else:
                assert(node.parent.right == node)
                node.parent.right = None
            self.size -= 1
        return node

    def __remove_branch(self, node):
        assert(node.is_branch())
        if not node.parent:
            self.root = node.left or node.right
        else:
            if node.parent.left == node:
                node.parent.left = node.left or node.right
            else:
                assert(node.parent.right == node)
                node.parent.right = node.left or node.right
        self.size -= 1
        return node

    def __remove_node(self, node):
        # Exchange the node that is located
        # the bottom of the longer subtree then remove it.
        if node.left.height > node.right.height:
            swap_node = self.get_biggest_node(node.left)
        else:
            swap_node = self.get_smallest_node(node.right)
        self._assign_then_remove_last(node, swap_node)
        self.size -= 1

    def _assign_then_remove_last(self, node1, node2):
        node1.key = node2.key
        node1.count = node2.count
        self._remove(node2)

    def _remove(self, node):
        """
        Directly remove the node no matter how many counts in the node.

        @param node: the node in this tree which will be removed later.
        """
        parent = node.parent
        if node.is_leaf():
            self.__remove_leaf(node)
        elif node.is_branch():
            self.__remove_branch(node)
        else:
            assert(node.left and node.right)
            self.__remove_node(node)
            return node

        while parent:
            # Remove the node will lead the breakings of
            # the balance on its parent node.
            # So reset the balance then remove it.
            parent.height = parent.height - 1
            if parent.balance not in [-1, 0, 1]:
                self.rebalance(parent)
                break
            parent = parent.parent
        return node

    def remove(self, key):
        """
        Remove the appointed key from the tree.
        """
        node = self.lookup(key)
        if not node:
            raise ValueError("ree hasn't element '{}'".format(key))
            return False

        if node.count > 1:
            node.count -= 1
            return True
        else:
            assert(node.count == 1)
            return self._remove(node)

    def get_smallest_node(self, node=None):
        if not self.root:
            return False
        if not node:
            node = self.root

        while node.left:
            node = node.left
        return node

    def get_biggest_node(self, node=None):
        if not self.root:
            return False
        if not node:
            node = self.root

        while node.right:
            node = node.right
        return node

    def insert(self, key, node=None):
        """
        Insert the key to the tree.
        """
        new_node = super().insert(key, node=node)
        if new_node:
            parent = new_node.parent
            while parent:
                # It has no effect on the node itself
                # but may change its parents' blance.
                assert(not parent.is_leaf())
                parent.height = parent.max_child_height + 1
                if parent.balance not in [-1, 0, 1]:
                    self.rebalance(parent)
                    break
                parent = parent.parent

    def rebalance(self, node):
        """
        Rotate the appointed node if the balance had been breaked.
        """
        if node.balance == 2:
            if node.left.balance == 1:
                # LL rotate
                self.__ll_rotate(node)
            else:
                assert(node.left.balance == -1)
                # LR rotate
                self.__lr_rotate(node)
        else:
            assert(node.balance == -2)
            if node.right.balance == -1:
                # RR rotate
                self.__rr_rotate(node)
            else:
                assert(node.right.balance == 1)
                # RL rotate
                self.__rl_rotate(node)
