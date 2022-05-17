candidates = []

def get_list(prompt, min, max):
  candidates_list = input(prompt).split()
  while len(candidates_list)<min or len(candidates_list) > max:
    print("The list should have between", min, "and", max, "elements")
    candidates_list = input(prompt).split()
  
  return candidates_list

def get_positive(prompt):
  voters = input(prompt)
  while voters.isdigit() == False or int(voters) <= 0:
    print("Number should be positive")
    voters = input(prompt)

  return int(voters)
    


def valid_vote(name):
  for element in candidates:
    if element["name"] == name:
      element["votes"] += 1
      return True
  
  return False

def print_winner():
  winners = []
  winner = 0
  for element in candidates:
    if element["votes"] > winner:
      winner = element["votes"]
      winners = [element["name"]]
    elif element["votes"] == winner:
      winners.append(element["name"])
  print("Winners: ", ", ".join(winners)) if len(winners)> 1 else print("Winners: ", winners[0])
  
names = get_list("Candidates names: ", 1, 9)

for i in names:
  candidate = { "name" : i, "votes" : 0 }
  candidates.append(candidate)

voters_count = get_positive("Number of voters: ")
print(voters_count)

print("-" * 20)

for i in range(1, voters_count + 1):
  prompt = "Voter " + str(i) + ": "
  name = input(prompt)
  while valid_vote(name) == False:  
    print("Invalid vote")
    name = input(prompt)

print("-" * 20)

print_winner()