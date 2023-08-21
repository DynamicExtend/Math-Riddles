def solve_hat_puzzle(prisoner_count, hat_colors):
    
    red_hat_count = hat_colors.count("red")

    if red_hat_count > 0:
        if red_hat_count == 1:
            return "Prisoner 1: Black Hat"
        else:
            return "Prisoner 0: Red Hat"   
    else:
        return "No one can determine their hat color"

prisoner_count = 3
hat_colors = ["red", "black", "black"]

result = solve_hat_puzzle(prisoner_count, hat_colors)
print(result)