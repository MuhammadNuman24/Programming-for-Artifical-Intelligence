# Compatibility fix for Python 3.10+
import collections
import collections.abc
if not hasattr(collections, "Hashable"):
    collections.Hashable = collections.abc.Hashable

import json
from kanren import Relation, facts, run, conde, var

# Check if 'x' is the parent of 'y'
def parent(x, y):
    return conde([father(x, y)], [mother(x, y)])

# Check if 'x' is the grandparent of 'y'
def grandparent(x, y):
    temp = var()
    return conde((parent(x, temp), parent(temp, y)))

# Check if 'x' is the sibling of 'y'
def sibling(x, y):
    temp = var()
    return conde((parent(temp, x), parent(temp, y)))

# Check if 'x' is the uncle of 'y'
def uncle(x, y):
    temp = var()
    return conde((father(temp, x), grandparent(temp, y)))


if __name__ == "__main__":
    father = Relation()
    mother = Relation()

    # Load data from relationships.json
    with open("relationships.json") as f:
        d = json.loads(f.read())

    # Add father facts
    for item in d["father"]:
        facts(father, (list(item.keys())[0], list(item.values())[0]))

    # Add mother facts
    for item in d["mother"]:
        facts(mother, (list(item.keys())[0], list(item.values())[0]))

    x = var()

    # John's children
    name = "John"
    output = run(0, x, father(name, x))
    print("\nList of " + name + "'s children:")
    for item in output:
        print(item)

    # William's mother
    name = "William"
    output = run(0, x, mother(x, name))[0]
    print("\n" + name + "'s mother:\n" + output)

    # Adam's parents
    name = "Adam"
    output = run(0, x, parent(x, name))
    print("\nList of " + name + "'s parents:")
    for item in output:
        print(item)

    # Wayne's grandparents
    name = "Wayne"
    output = run(0, x, grandparent(x, name))
    print("\nList of " + name + "'s grandparents:")
    for item in output:
        print(item)
