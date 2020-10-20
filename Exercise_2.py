
# list of employees
employees = ("Max","Naru","Smol","Ginger","Devil","Bitz","Bear","Ruka","Khael","LRavellie")
# sorts employees alphabetical
Sortedemployees = sorted(employees)

# Prints employee list in a list and aplhabetical order
for x in Sortedemployees:
  print(x)
print("--------------")
# prints every other employee in the list
for everyother in Sortedemployees[::2]:
   print(everyother)
print("--------------")