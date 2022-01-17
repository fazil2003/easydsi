import sys
sys.path.append(r'D:/Projects/Python/easydsi')

from linear.linked_list.linked_list import *

li = linked_list([100, 200])
li.addAtFirst( 5)
li.addAtLast( 10)
li.addAtLast( 9)
li.removeAtLast()
print(li.getLength())
print(li.getElements())