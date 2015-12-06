__author__ = 'lisa'

from linkedlist.LinkedList import LinkedList

newlinkedlist = LinkedList()
newlinkedlist.insertStart(21)
newlinkedlist.insertStart(23)
newlinkedlist.insertStart(25)
newlinkedlist.insertStart(30)
newlinkedlist.insertStart(35)
newlinkedlist.remove(35)
print("second run")
newlinkedlist.traverseList()