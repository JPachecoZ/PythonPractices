string_array = ["1", "2", "3", "4"]

def string_to_square(string):
  return int(string) ** 2

def my_map(function, data):
  newData = []
  for element in data:
    new_element = function(element)
    newData.append(new_element)
  return newData

print(list(map(lambda x: int(x)**2, string_array)))

print(my_map(lambda x: int(x)**2, string_array))