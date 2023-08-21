import random

def simulate_prisoners():
    # Create an array to represent the prisoners' hat colors
    # 0 represents black hat, 1 represents red hat
    hat_colors = [0, 0, 1]  # One red hat and two black hats initially
    
    # Shuffle the hat colors randomly
    random.shuffle(hat_colors)
    
    # Determine the index of the prisoner with the red hat
    red_hat_prisoner_index = hat_colors.index(1)
    
    # Remove the red hat prisoner's hat from the array for others' perspectives
    hat_colors_without_red = hat_colors[:red_hat_prisoner_index] + hat_colors[red_hat_prisoner_index + 1:]
    
    # Prisoner's responses based on their perspectives
    responses = []
    for i in range(3):
        prisoner_perspective = hat_colors_without_red[i]
        other_prisoners_perspective = [hat_colors_without_red[j] for j in range(3) if j != i]
        
        if prisoner_perspective == 0:
            # If the prisoner sees two red hats, he knows he has a black hat
            responses.append("Black")
        else:
            # If the prisoner sees only one red hat, he knows he has the red hat
            responses.append("Red")
    
    return responses

# Run the simulation multiple times to observe the results
num_simulations = 10000
correct_count = 0

for _ in range(num_simulations):
    responses = simulate_prisoners()
    if responses.count("Red") == 1:
        correct_count += 1

print(f"Percentage of correct identifications: {correct_count / num_simulations * 100}%")