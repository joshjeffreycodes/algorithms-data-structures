from pydatalists import numbers_unique_sorted

# -----------------------------------------
# Iterative Binary Search
#
# O(log n + 1) - Logarithmic time
# O(log 100 + 1) = 6.64 -> 6 + 1 = 7
# Worst-cse, the algorithm will contiue dividng
# until it reaches a list with one value. 
#
# O(1) - Constant space
# Wost-case, the algorithm is only working
# with a single list. 
# -----------------------------------------

class BinarySearch():
  '''Uses logarithmic runtime to search a list for a target.  
  * Returns `(index, value)` tuple if found.
  * Returns `None` if target is not found. 
  * Returns `False` if passed an empty list.
  '''  
  def __init__(self, list, target):

    self.list = list
    self.target = target
    self.first = 0
    self.last = len(list) - 1
    self.operations = 0

  def do(self): 

    if len(self.list) == 0:
      self.operations += 1
      print('List is empty : %s operations' % self.operations)
      return False

    while self.first <= self.last:
      # Floor division rounds down
      midpoint = (self.first + self.last)//2 

      # Best case, target is found on first try.
      if self.target == self.list[midpoint]:
        self.operations += 1
        print('Target found : [%s] %s : %s operations' % (midpoint, self.list[midpoint], self.operations))
        return midpoint, self.list[midpoint]    

      # Target is bigger, so discard smaller half.
      elif self.target > self.list[midpoint]:
        self.operations += 1
        self.first = (midpoint + 1)

      # Target is smaller, so discard the bigger half. 
      else:
        self.operations += 1
        self.last = (midpoint - 1)

    print('Target not found : %s : %s operations' % (self.target, self.operations))
    return None


# -----------------------------------------
# Use
# -----------------------------------------
list_num = numbers_unique_sorted # 100 values
list_empty = []

target_01 = 50   # best-case
target_02 = 100  # worst-case
target_03 = 233  # not in list

search_01 = BinarySearch(list_num, target_01).do()
search_02 = BinarySearch(list_num, target_02).do()
search_03 = BinarySearch(list_num, target_03).do()
search_04 = BinarySearch(list_empty, target_01).do()
