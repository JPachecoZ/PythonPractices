candidates = []

def get_list(prompt, min, max):
  candidates_list = input(prompt).split()
  while len(candidates_list)<min or len(candidates_list) > max:
    print("The list should have between", min, "and", max, "elements")
    candidates_list = input(prompt).split()
  
  return candidates_list

def get_positive(prompt):
  print(prompt)

def valid_vote(name):
  print(name)

def print_winner():
  print(candidates)

names = get_list("Candidates names: ", 1, 9)

for i in names:
  candidate = { "name" : i, "votes" : 0 }
  candidates.append(candidate)

voters_count = get_positive("Number of voters: ")

print("-") * 20

for i in range(1, voters_count + 1):
  prompt = "Voter " + str(i) + ": "
  name = input(prompt)
  while valid_vote(name) == False:  
    print("Invalid vote")
    name = input(prompt)

print("-") * 20

print_winner