from pydatalists import alpha_unique_sorted

# -----------------------------------------
# Linear Search
# 
# O(n) - Linear Time
# The worst-case requires iterating over the entire list. 
#
# O(1) - Constant Space 
# The worst case uses a single list.
# -----------------------------------------

class LinearSearch:
  '''Uses linear runtime to search a list for a target.  
  * Returns target's `index` if found. 
  * Returns `None` if target is not found. 
  * Returns `False` if passed an empty list.
  '''  
  def __init__(self, list, target):

    self.target = target
    self.list = list
    self.operations = 0

  def do(self):

    if len(self.list) == 0:
      self.operations += 1
      print('List is empty : %s operations' % self.operations)
      return False

    for i in range(0, len(self.list)):

      self.operations +=1

      if self.list[i] == self.target:
        print('Target found : [%s] %s : %s operations' % (i, self.list[i], self.operations))
        return i

    print('Target not found : %s : %s operations' % (self.target, self.operations))
    return None


# -----------------------------------------
# Usage
# -----------------------------------------
list_alpha = alpha_unique_sorted
list_empty = []

target_01 = 'adfnogvt' # best-case
target_02 = 'zvubkrhd' # worst-case
target_03 = 'python'   # not in list

search_01 = LinearSearch(list_alpha, target_01).do()
search_02 = LinearSearch(list_alpha, target_02).do()
search_03 = LinearSearch(list_alpha, target_03).do()
search_04 = LinearSearch(list_empty, target_03).do()
