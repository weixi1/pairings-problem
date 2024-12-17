def find_pairs(num_string):
  # Write your solution here!
  # input is str -> become int by spcae
  # ("7 3 99")
  # output is set of tuples of integers should be have order 
  # {(7, 99), (3, 7), (3, 99)}
  # no empty
  # how to handle the nagtive int

  # split input by space
  # do the one element case
  # init result set of tuples
  # outloop for get fist int 
  # innerloop for other int to pair 
  # have order for each pair
  # return the result

  num_str = num_string.split(" ")

  num_list = []
  for num in num_str:
    num_list.append(int(num))
  
  if len(num_list) < 1:
    return set()

  result_set = set()
  for first in num_list:
    for sec in num_list[num_list.index(first)+1:]:
      result_tuples = tuple(sorted((first, sec)))
      result_set.add(result_tuples)
  
  return result_set


# Test cases
assert find_pairs("7 3 99") == {(7, 99), (3, 7), (3, 99)}
assert find_pairs("2 1") == {(1, 2)}
assert find_pairs("24 7 365 94") == {(7, 94), (24, 94), (94, 365), (7, 365), (24, 365), (7, 24)}
assert find_pairs("94") == set()

print("All tests passed!")
print("Finished early? Discuss time & space complexity")