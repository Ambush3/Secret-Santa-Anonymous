import random

people = []
while True:
    person = input("Enter your name please: If done, type done. \n")
    if person == "done":
        break
    people.append(person)

random.shuffle(people)
offset = [people[-1]] + people[:-1]
for santa, receiver in zip(people, offset):
    print(santa, "buys for", receiver)
