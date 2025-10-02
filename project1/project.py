# Function to read adjacency info from file
def read_adjacency(filename):
    adjacency = {}
    with open(filename, 'r') as file:
        for line in file:
            if ':' in line:
                province, neighbors = line.strip().split(':')
                adjacency[province.strip()] = [n.strip() for n in neighbors.split(',')]
    return adjacency


# Function to read coastal states from file
def read_coastal_states(filename):
    with open(filename, 'r') as file:
        return [line.strip() for line in file.readlines()]


# Load data from files
adjacent_states = read_adjacency("adjacent_states.txt")
coastal_states = read_coastal_states("coastal_states.txt")

# Take user input
province = input("Enter a province name: ").strip()

# Show results
if province in adjacent_states:
    print("\nAdjacent provinces of", province, ":", adjacent_states[province])
    if province in coastal_states:
        print(province, "is a coastal province.")
    else:
        print(province, "is landlocked (no coast).")
else:
    print("Province not found in data.")
