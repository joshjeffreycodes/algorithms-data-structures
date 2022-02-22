from pydatalists import numbers_unique_sorted

# -----------------------------------------
# Recursevie Binary Search
#
# O(log n) - Logarithmic time
# Worst-case, the algorithm will contiue dividng
# until it reaches a list with one value. 
#
# O(log n) - Logarithmic space
# Each guess calls the function again using
# a new list that is half the size of the
# previous list.  
# -----------------------------------------

class RecursiveBinarySearch():
  '''Uses recursive, binary approach to search a list for a target. 
  * Returns target's `value` if found.
  * Returns `Falee` if passed an empty list.
  * Returns `False` if target is not found - which also results in an empty list.
  '''  
  def __init__(self, list, target):

    self.list = list
    self.target = target

  def do(self):

    if len(self.list) == 0:
      print('Target not found : %s' % self.target)
      return False

    midpoint = len(self.list)//2

    if self.target == self.list[midpoint]:
      print('Target found : %s' % (self.list[midpoint]) )
      return True

    elif self.target > self.list[midpoint]:
      return RecursiveBinarySearch(self.list[midpoint+1:], self.target).do()

    # Question - shouldn't this be `midpoint-1`?
    else: 
      return RecursiveBinarySearch(self.list[:midpoint], self.target).do()


# -----------------------------------------
# Use
# -----------------------------------------
list_num = numbers_unique_sorted
list_empty = []

target_01 = 50   # best-case
target_02 = 100  # worst-case
target_03 = 233  # not in list

search_01 = RecursiveBinarySearch(list_num, target_01).do()
search_02 = RecursiveBinarySearch(list_num, target_02).do()
search_03 = RecursiveBinarySearch(list_num, target_03).do()
search_04 = RecursiveBinarySearch(list_empty, target_01).do()

