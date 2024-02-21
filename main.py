
import csv

pokemons = []

# https://www.w3schools.com/python/python_file_handling.asp
# https://www.w3schools.in/python/file-handling
with open('pokemon.csv', newline='') as csv_file:
    file_reader = csv.reader(csv_file, delimiter = ',', quotechar='|')

    for row in file_reader:
        pokemons.append(row[0])

print(pokemons)

print("Pokemon list command:")

while True:
    print("1. Get pokemon by sequence number")
    print("2. Sort by A-Z")
    print("3. Sort by Z-A")
    print("4. Search by text in name")
    print("5. Search by length of name")
    print("6.izdrukat pirmos 10 pokemonu vardus")
    print("7.izdrukat pedejos 10 pokemonu vardus")
    print("8. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == '1':
        number= input("write a pokemon by sequence number")
        print(pokemons[:10])
        print(pokemons[int(number)])
        # https://www.w3schools.com/python/python_lists_access.asp
        pass
    elif choice == '2':
        pokemons.sort()
        print(pokemons)
        # https://www.w3schools.com/python/python_lists_sort.asp
        pass
    elif choice == '3':
        pokemons.sort(reverse = True)
        print(pokemons)
        # https://www.w3schools.com/python/python_lists_sort.asp
        pass
    elif choice == '4':
        matched = []
        insert=input("Write a pokemon name:")
        for pokemon in pokemons:
          if insert in pokemon:
             matched.append(pokemon)
        print(matched)

        # https://www.w3schools.com/python/python_lists_comprehension.asp
        # https://www.w3schools.com/python/ref_string_startswith.asp
        pass
    elif choice == '5':
      length = input("enter pokemon name in length:")
      Choose = [x for x in pokemons if len(x) == int(length)]
      print(Choose)
            
        # https://www.w3schools.com/python/python_lists_comprehension.asp
      if choice == '6':
         print("Pirmie 10 pokemoni no saraksta")
         print(pokemons[10])
        
      if choice == '7':
        print("Pedejie 10 pokemoni no saraksta")
        print(pokemons[-10])
        next = "n"
        while next == "n":
            print(pokemons[-10])
            next = input("Iziet?")
            
    elif choice == '8':
        print("Exiting")
        break
    else:
        print("Invalid choice, choose from 1 to 6")

    print("==========================")
