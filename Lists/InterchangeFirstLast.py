#Python program to interchange first and last elements in a list

"""
Given a list, write a Python program to swap first and last element of the list.
"""

def InterchangeFirstLast(list):
  list[0], list[-1] = list[-1], list[0]
  return list

listOG = [1,2,3,4,5]
print(InterchangeFirstLast(listOG))
