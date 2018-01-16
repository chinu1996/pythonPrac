class ArrayStack:
    """stack implementation using stack"""
    def __init__(self):
        """Create an empty Stack using python list as storage"""
        self._data = []

    def __len__(self):
        """Returns the number of items in the stack"""
        return len(self._data)

    def is_empty(self):
        """Check whether the list is empty or not"""
        return len(self._data)==0

    def push(self, e):

        self._data.append(e)   #New data in the end of the stack

    def top(self):
        """Return the top element of the stack or will raise an error if there are no items in the list"""

        if self.is_empty():
            raise Empty('Stack is empty')

        return self._data[-1]

    def pop(self):
        """Remove the last iten of the list if any"""
        if self.is_empty():
            raise Empty('Stack is empty')
        self._data.pop()  #Remove the last item of the list


 #Error trying to access the empty container
class Empty(Exception):
    pass




#reverse a list using stack (LIFO principle)
def reverse_file(filename):
    """Lines of a file getting reversed"""
    s= ArrayStack()
    original = open(filename)
    for line in original:
        s.push(line.rstrip('\n'))
    original.close()

    #now overwrite the contents in reverse order
    output = open(filename, 'w')
    while not s.is_empty():
        output.write(s.pop()+'\n')
    output.close()


