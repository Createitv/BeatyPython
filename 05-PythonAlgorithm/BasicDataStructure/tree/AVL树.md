## AVL 树

将普通二叉树直接用于查找，平均情况下，仅需要查找一个分支，其时间复杂度为 O(log n)。想要使查找时间尽可能短，就要使树的高度经可能短，使二叉树保持平衡状态。如果一个二叉树变得越来越不平衡，最后，其时间复杂度就变成了 O(n)，相当于从头到尾遍历所有节点。

AVL 是最先发明的一种自平衡二叉查找树，像普通二叉树一样组织数据。所不同的是，AVL 的每一个节点都附带了一个`平衡因子`，其值代表了左子树和右子树的高度之差。对于每一次改变其平衡性的操作，AVL 树都通过执行一次`旋转`操作来使其重新平衡。每一次插入和删除操作最多可能有`log n`个节点被旋转。因此，AVL 树的插入、删除、查找操作的时间复杂度都在 O(log n)。

下面使用 python 来实现 AVL 树。

## 节点

由普通二叉树的节点继承而来：

```
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
```

普通二叉树的节点：

```
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
```

与普通二叉树节点不同，AVL 树的节点附带了树的高度信息，以此来判断这个节点是否处于平衡状态。如果这个节点的左子树与右子树高度差的绝对值大于 1，就视这个节点为不平衡的，应该在稍后执行旋转操作。

并且 AVL 树的节点还又一个 adjust_height 方法，用于在进行一个会改变树高的操作后，重新计算这个节点所属的整个子树的高度，直到高度不再变化，代表调整完毕。

## 插入操作

AVL 树的插入操作和普通二叉树类似。只不过在每一次插入后，需要重新计算子树高度（调用插入节点的 adjust_height 方法）。如果这次插入操作改变了树的平衡性，就需要旋转节点以使树重新平衡。

插入操作的关键代码如下：

```
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
```

这是 AvlBiTree 类的一个方法，用于为 AVL 数插入节点。它继承自代表普通二叉树的 BiTree 类。因此，这里的插入方法覆盖了 BiTree 的插入方法。在其中调用了父类的 insert 方法来普通插入节点。之后，再调整树的高度。并且逐一遍历其父节点查看平衡性是否受到破坏。如果平衡新被破坏，就调用 rebalance 方法旋转节点，使树重新平衡。

如果进行了一次 rebalance 旋转操作，代表已经消除了这次插入操作的副作用使树重新平衡。那么，其上所有祖先节点的平衡性都不受这次插入操作的影响。因此，break 结束对祖先节点的遍历。代表本次插入操作完成。

## 旋转结点使树重新平衡

关键代表如下：

```
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
```

可见，这实际上接近于一个调度方法，根据平衡性的情况，执行不同的旋转操作。

## 具体旋转操作：

### 左旋

#### ll

如果插入一个节点后使得父节点（平衡性受到破坏的节点）的左节点的平衡性为 1（左子树高度大于右子树），需要对左子树进行一次旋转操作。

令父节点为 A，左子节点为 B，旋转步骤为：

1. 将 A 的左子树替换为 B 的右子树。
2. 将 B 的右子树替换为 A。
3. 将指向 A 的节点执行 B。

代码如下：

```
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
```

#### lr

如果插入一个节点后，使得父节点的左子树的平衡性为-1，那么，在左旋一次后，树依然是不平衡的，需要再进行一次左旋操作。

令父节点为 A，A 的左节点为 B，B 的右节点为 C。
总体的步骤如下：

1. 将 B 的右节点替换为 C 的左节点。
2. 将 A 的左节点替换为 C 的右节点。
3. 将 C 的左节点替换为 B。
4. 将 C 的右节点替换为 A。
5. 将指向 A 的节点指向 C。

代码如下：

```
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
```

### 右旋

#### rr

如左旋的 ll，只不过方向相反。

#### rl

如左旋的 lr，只不过方向相反。

## 删除操作

和普通的二叉树相比，AVL 树的删除操作稍显复杂，因为涉及到调整平衡性的问题。

不妨考虑以下四种情况

-   如果删除的是叶子节点。
    -   如果删除的是叶子节点（没有左右子节点），直接删除。这个节点（None)的平衡性不受影响。
-   如果删除的是分支节点。
    -   如果删除的是分支上的节点（有左右子节点中的一个），将其替换为它的那个子节点。这个节点（子节点）的平衡性不受影响。
-   如果删除的节点有两个子节点
    -   如果删除的节点有两个子节点。如果其左子树的高度大于右子树，取其左子树上最大的那个节点；如果其右子树的高度大于左子树，取其右子树上最小的那个节点。然后用取的节点替换当前节点。最后，再删除取的那个节点。这样，这个节点（取的节点）的平衡性不受影响。
-   如果要删除的不是本节点
    -   如果要删除的节点不是本节点，而是本节点的子节点。那么，本节点的平衡性可能回受影响，在删除操作完毕后，需要对其进行重新平衡（旋转）操作。

可以看出，实际上，可以用类似递归的方法处理删除操作。关键代码如下：

```
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
```

## 参考

《算法精解-C 语言描述》

[https://zh.wikipedia.org/wiki/AVL%E6%A0%91](https://zh.wikipedia.org/wiki/AVL树)

http://www.cnblogs.com/linxiyue/p/3659448.html

https://segmentfault.com/a/1190000007054898

## AVL 树 python 实现的完整代码

放在了 github gist 里，可能需要 vpn:

https://gist.github.com/Arianxx/5226596ee425a6ee0b1be074a7f85d13

```python
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
```
