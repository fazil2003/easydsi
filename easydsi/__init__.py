import sys
sys.path.append(r'D:/Projects/Python/easydsi')

import linear.array.array as a

myArr = a.array([4,5,6,7])
print(myArr.index(3))
myArr.display()