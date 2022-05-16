contacts = {
  "Codeka" : {
    "country" : "Peru",
    "email" : "karem@able.co",
    "phone" : "+51 987654321"
  },
  "Teddy" : {
    "country" : "Bolivia",
    "email" : "teddy@able.co",
    "phone" : "+51 987654321"
  },
  "Andre" : {
    "country" : "Peru",
    "email" : "atavara@able.co",
    "phone" : "+51 9871236547"
  }
}

def display():
  print("-" * 50)
  print("All your contacts:")
  for element in contacts:
    print("-", element)
  print("-" * 50)

def add():
  name = input("Name: ")
  country = input("Country: ")
  email = input("Email: ")
  phone = input("Phone: ")
  contacts[name] = {"country": country, "email" : email, "phone" : phone}

def show():
  name = input("Contact name: ")
  print("-" * 50)
  try:
    print("Country: ", contacts[name]["country"])
    print("Email: ", contacts[name]["email"])
    print("Phone: ", contacts[name]["phone"])
  except:
    print("Contact does not exist")
  print("-" * 50)

def update():
  name = input("Contact name: ")
  print("-" * 50)
  try:
    country = input("Country: ")
    email = input("Email: ")
    phone = input("Phone: ")
    contacts[name] = {"country": country, "email" : email, "phone" : phone}
  except:
    print("Contact does not exist")
  print("-" * 50)

def delete():
  name = input("Contact name: ")
  print("-" * 50)
  try:
    del contacts[name]
    print(name,"has been deleted")
  except:
    print("Contact does not exist")
  print("-" * 50)

def exit_app():
  pass

options = {
  "display" : display,
  "add" : add,
  "show" : show,
  "update" : update,
  "delete" : delete,
  "exit" : exit_app
}

print("-" * 50)
print("Welcome to Contacs")
print("-" * 50)
print("What would you like to" + '\33[34m' + " do " + '\33[0m' + "next?")
print("-- Type " + '\33[33m' + "'display'" + '\33[0m' + " to display all contacts")
print("-- Type " + '\33[33m' + "'add'" + '\33[0m' + " to add a contact")
print("-- Type " + '\33[33m' + "'show'" + '\33[0m' + " to show the details of a contact")
print("-- Type " + '\33[33m' + "'update'" + '\33[0m' + " to update a contact")
print("-- Type " + '\33[33m' + "'delete'" + '\33[0m' + " to delete a contact")
print("-- Type " + '\33[33m' + "'exit'" + '\33[0m' + " to " + '\33[92m' + "exit" + '\33[0m' + " the program")
choice = input("action: ")
options[choice]()

while choice != "exit":
  print("What would you like to" + '\33[34m' + " do " + '\33[0m' + "next?")
  choice = input("action: ")
  options[choice]()
