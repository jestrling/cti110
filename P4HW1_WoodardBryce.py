# Bryce Woodard
# Date: 04 25, 2025
# P4HW1_WoodardBryce
# This program collects a user-specified number of scores, validates them,
# calculates the average after dropping the lowest score, and assigns a letter grade.


def get_valid_score():
    """Prompts the user to enter a score and validates if it's between 0 and 100."""
    while True:
        try:
            score_str = input("Enter score #: ")
            score = int(score_str)
            if 0 <= score <= 100:
                return score
            else:
                print("INVALID Score entered!!!!")
                print("Score should be between 0 and 100")
        except ValueError:
            print("Invalid input. Please enter a whole number.")

def calculate_average(scores):
    """Calculates the average of a list of numbers."""
    if not scores:
        return 0
    return sum(scores) / len(scores)

def determine_grade(average):
    """Determines the letter grade based on the average score."""
    if 90 <= average <= 100:
        return 'A'
    elif 80 <= average < 90:
        return 'B'
    elif 70 <= average < 80:
        return 'C'
    elif 60 <= average < 70:
        return 'D'
    else:
        return 'F'

def main():
    """Main function to run the score analysis program."""
    while True:
        try:
            num_scores_str = input("How many scores do you want to enter? ")
            num_scores = int(num_scores_str)
            if num_scores > 0:
                break
            else:
                print("Please enter a positive number of scores.")
        except ValueError:
            print("Invalid input. Please enter a whole number.")

    score_list = []
    for i in range(1, num_scores + 1):
        while True:
            score = get_valid_score()
            if score is not None:
                score_list.append(score)
                break

    if score_list:
        lowest_score = min(score_list)
        print(f"\nLowest score entered: {lowest_score}")

        modified_score_list = score_list[:]  # Create a copy to avoid modifying the original
        modified_score_list.remove(lowest_score)
        print("Score List after dropping lowest score:", modified_score_list)

        if modified_score_list:
            average_score = calculate_average(modified_score_list)
            print(f"The average of scores in modified list: {average_score:.2f}")
            letter_grade = determine_grade(average_score)
            print(f"Letter grade for the calculated average: {letter_grade}")
        else:
            print("No scores left to calculate the average after dropping the lowest.")
    else:
        print("No valid scores were entered.")

if __name__ == "__main__":
    main()
