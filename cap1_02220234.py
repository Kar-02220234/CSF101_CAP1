
# Function to read input data from a file and parse it into a list of tuples
def read_input(file_name):
    file_path = "input_4_cap1.txt"
    with open(file_path, "r") as file:
        lines = file.readlines()
        return [line.strip().split() for line in lines]

# Function to calculate the total score based on AI actions
def calculate_score(data):
    # Define the score table
    score_table = {
        ('A', 'X'): 1, ('A', 'Y'): 4, ('A', 'Z'): 7,
        ('B', 'X'): 2, ('B', 'Y'): 5, ('B', 'Z'): 8,
        ('C', 'X'): 3, ('C', 'Y'): 6, ('C', 'Z'): 9
    }

    # Initialize total score
    total_score = 0
    for ai_actions in data:
        ai_actions = tuple(ai_actions)
        # Look up the score for the given AI actions
        total_score += score_table.get(ai_actions, 0)
    
    return total_score

# Run the program
data = read_input("input_2_cap1.txt")
if data:
    total_score = calculate_score(data)
    print(f"Total Score: {total_score}")
else:
    print("No data to calculate score.")
