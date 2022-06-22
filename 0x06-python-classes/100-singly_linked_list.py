#!/usr/bin/python3
"""Define classes for a singly-linked list."""


class Node:
    """Represents a Node in a SinglyLinkedList"""
    def __init__(self, data, next_node=None):
        """
        Initializes a Node
        :param data: is an integer to store in node
        :param next_node: the next node
        """
        self.__data = data
        self.__next_node = next_node

    @property
    def next_node(self):
        """
        getters for next_node
        :return: returns the next_node
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """
        setter for next_node
        :param value: node
        :return: Always void.

        """
        if (value is not None and
                not isinstance(value, Node)):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value

    @property
    def data(self):
        """
        getter for data in a node
        :return: an integer data

        """
        return self.__data

    @data.setter
    def data(self, value):
        """
        Setter for data in a node
        :param value: is an integer to set as data
        :return: Always void
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value


class SinglyLinkedList:

    """Represents a SinglyLinkedList"""

    def __init__(self):

        """Initializes a SinglyLinkedList"""
        self.__head = None

    def sorted_insert(self, value):
        """
        Inserts a new node to the SinglyLinkedList

        The node is inserted into the linkedlist in the
        correct natural numeric position

        :param value: The new node to be inserted
        :return: void.

        """
        new = Node(value)
        if self.__head is None:
            self.__head.next_node = None
            self.__head = new
        elif self.__head.data > value:
            new.next_node = self.__head
            self.__head = new
        else:
            tmp = self.__head
            while (tmp.next_node is not None and
                   tmp.next_node.data < value):
                tmp = tmp.next_node
            new.next_node = tmp.next_node
            tmp.next_node = new

    def __str__(self):

        """Defines the print representation of a SinglyLinkedList"""

        lst = []
        tmp = self.__head
        while tmp is not None:
            lst.append(str(tmp.data))
            tmp = tmp.next_node
        return '\n'.join(lst)
