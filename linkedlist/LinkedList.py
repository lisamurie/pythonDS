__author__ = 'lisa'
from linkedlist.Node import Node

class LinkedList(object):
    def __init__(self):
        self.head = None
        self.counter = 0

    def traverseList(self):

        while self.head is not None:
            print(" %d " % self.head.data)
            self.head = self.head.nextNode

    def size(self):
        return self.counter

    def insertStart(self, data):
        self.counter += 1
        newNode = Node(data)

        if not self.head:
            self.head = newNode

        else:
            newNode.nextNode = self.head
            self.head = newNode

    def insertEnd(self, data):
        self.counter += 1
        newNode = Node(data)
        actualNode = self.head

        if not self.head:
            self.insertStart(data)
            return

        while actualNode.nextNode is not None:
            actualNode = actualNode.nextNode

        actualNode.nextNode = newNode

    def remove(self, data):
        self.counter -= 1
        if self.head:
            if self.head.data == data:
                self.head = self.head.nextNode


            else:
                self.head.remove(data, self.head)


