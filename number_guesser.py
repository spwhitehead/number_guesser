
"""
Make a number guesser where the program tries to guess your number! You'll pick a number (don't give it to the program), 
then the program tries to guess it. If it's wrong, you'll tell it whether it was too high or too low, then it'll guess again. 
Use a binary search algorithm for the guessing.
"""

highest_num = 0

def binary_search(nums: int, target: int):
    """ Utilizes a binary search tree to search for the number """
    left = 0
    right = len(highest_num-1)
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1

        else:
            right = mid - 1
    return None



def is_it_right():
    """ Asks the user if the guessed number is correct and takes input from the user """
    target = False
    guess = 0 
    print(f"Is it {guess}? "
    while mid is target:
        high_or_low = input("Was that too high or too low (high or low): ")
        if high_or_low == "high":

        



def main():
    print()
    print("Welcome to the Number Guesser! Pick a number in your mind and I'll try to guess it!")
    user_ready = input("Are you ready (yes or no): ")
    print()
    highest_num = input("What is the highest number you want to go to? ")



if __name__ == "__main__":
    main()
