# Calculate the number of children and grandchildren

# Count the number of direct children of a person

# Count the number of grandchildren of a person

# Use recursion to count all descendants

# Consider only living descendants

# Exclude step-children and adopted children

class Person:
    def __init__(self, name, is_alive=True):
        self.name = name
        self.is_alive = is_alive
        self.children = []

    def add_child(self, child):
        self.children.append(child)

def count_direct_children(person):
    return sum(child.is_alive for child in person.children)

def count_grandchildren(person):
    grandchildren_count = 0
    for child in person.children:
        if child.is_alive:
            grandchildren_count += count_direct_children(child)
    return grandchildren_count

def count_all_descendants(person):
    if not person.is_alive:
        return 0
    
    total_descendants = count_direct_children(person)
    
    for child in person.children:
        total_descendants += count_all_descendants(child)
    
    return total_descendants

# Example usage
grandparent = Person("Grandparent")
parent1 = Person("Parent 1")
parent2 = Person("Parent 2")

child1 = Person("Child 1", is_alive=True)
child2 = Person("Child 2", is_alive=True)
grandchild1 = Person("Grandchild 1", is_alive=True)
grandchild2 = Person("Grandchild 2", is_alive=True)

parent1.add_child(child1)
parent1.add_child(child2)
child1.add_child(grandchild1)
child2.add_child(grandchild2)

grandparent.add_child(parent1)
grandparent.add_child(parent2)

direct_children_count = count_direct_children(grandparent)
grandchildren_count = count_grandchildren(grandparent)
all_descendants_count = count_all_descendants(grandparent)

print("Direct Children Count:", direct_children_count)
print("Grandchildren Count:", grandchildren_count)
print("All Descendants Count:", all_descendants_count)
