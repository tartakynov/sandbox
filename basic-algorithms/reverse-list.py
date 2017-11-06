#!/usr/bin/env python


class Node(object):
    def __init__(self, value, next_node):
        self.value = value
        self.next_node = next_node

    def __str__(self):
        return "Node(%d, %s)" % (self.value, self.next_node)


def reverse_list_destructive(root):
    prev = None
    while root:
        tmp = root.next_node
        root.next_node = prev
        prev = root
        root = tmp
    return prev


def reverse_list_immutable(root, prev=None):
    r = Node(root.value, prev)
    if root.next_node:
        return reverse_list_immutable(root.next_node, r)
    return r


def main():
    print reverse_list_destructive(Node(1, Node(2, Node(3, Node(4, Node(5, None))))))
    print reverse_list_immutable(Node(1, Node(2, Node(3, Node(4, Node(5, None))))))


if __name__ == "__main__":
    main()
