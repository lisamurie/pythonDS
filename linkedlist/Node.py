__author__ = 'lisa'

class Node(object):
    def __init__(self, data):
        self.nextNode = None
        self.data = data

    def remove(self, data, previousNode):

        if self.data == data:
            previousNode.nextNode = self.nextNode
            del self.data
            del self.nextNode

        else:
            if self.nextNode is not None:
                self.nextNode.remove(self, data)
