




# #Q1:
print("\n\n ---------> Question1: <---------")

person = {'First_Name' : 'Abdullah',
          'Last_Name' : 'Sohail',
           'Age' : '20',
           'City' : 'Sharjah'}
print(person["First_Name"])
print(person["Last_Name"])
print(person["Age"])
print(person["City"])




#Q2:
print("\n\n ---------> Question2: <---------")

Glossary = {
     "Variable" : "A memory or location where data is stored.",
     "Function" : "A block of reusable code that performs a specific task.",
     "List" : "A dynamic and ordered collection of elements enclosed within Square brackets[]",
     "Comment" : "A note in a program that the interpreter ignores.",
     "Dictionary" : "Data Structure that stores value in key.",
 }


word = 'Variable'
print("\n" + word.title() + ":" + Glossary[word])

word = 'Function'
print("\n" + word.title() + ":" + Glossary[word])

word = 'List'
print("\n" + word.title() + ":" + Glossary[word])

word = 'Comment'
print("\n" + word.title() + ":" + Glossary[word])

word = 'Dictionary'
print("\n" + word.title() + ":" + Glossary[word])







#Q3:
print("\n\n ---------> Question3: <---------")

Glossary = {
'Variable' : "A memory or location where data is stored.",
"Function" : "A block of reusable code that performs a specific task.",
"List" : "A dynamic and ordered collection of elements enclosed within Square brackets[]",
"Comment" : "A note in a program that the interpreter ignores.",
"Dictionary" : "Data Structure that stores value in key.",
 
 }

for word, defination in Glossary.items():
   print(f"{word}:\n{defination}\n")

#Adding 5 more python terms:

Glossary = {
'method':'A function associated with an object.',
'Arithmetic Operators': 'Are used to perform mathematical operations.',
'Output': 'Use the print statement to Output.',
'Attribute':  'A characteristic of an object.',
'Class' : 'A blueprint for making objects.',
 }


for word,defination in Glossary.items():
     print(f"{word}:\n{defination}\n")




#Q4:
print("\n\n ---------> Question4: <---------")

Rivers = {
 'Nile' : 'Egypt',
 'Amazon': 'Brazil',
 'Yangtze': 'China',
 }

for River, country in Rivers.items():
     print(f"The {River.title()} flows through {country}.")

print("\nRivers:")
for River in Rivers.keys():
  print(River.title())

print("\n Countries:")
for country in Rivers.values():
    print(country)









#Q5:
print("\n\n ---------> Question5: <---------")

# Make a list to store the pet dictionaries
pets = []


petnum1 = {
    'pet_kind': 'Snake',
    'pet_owner': 'Adil'
}
petnum2 = {
    'pet_kind': 'Dog',
    'pet_owner': 'Harry'
}
petnum3 = {
    'pet_kind': 'Spider',
    'pet_owner': 'Mark'
}


pets.append(petnum1)
pets.append(petnum2)
pets.append(petnum3)

for pet in pets:
    kind = pet['pet_kind']
    owner = pet['pet_owner']
    print(f"{owner}'s pet is a {kind}.")
    