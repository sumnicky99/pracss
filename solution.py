def solution(A, F, M):
    num_known_rolls = len(A)
    sum_known_rolls = sum(A)
    total_rolls = num_known_rolls + F
    required_sum = total_rolls * M - sum_known_rolls
    
    # Check if the required sum is possible
    if required_sum < F or required_sum > 6 * F:
        return [0]
    
    # Generate the possible results for the missing rolls
    missing_rolls = []
    remaining_sum = required_sum
    
    for _ in range(F):
        # Calculate the maximum we can assign to the current roll
        roll = min(6, remaining_sum - (F - len(missing_rolls) - 1))
        missing_rolls.append(roll)
        remaining_sum -= roll
    
    return missing_rolls

# Example usage
print(solution([3, 2, 4, 3], 2, 4))  # [6, 6]
