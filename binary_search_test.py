def binary_search(nums: int, target: int):
    """ Utilizes a binary search tree to search for the number """
    highest_num = input("What is the highest number? ")
    target = input("What is the target number? ")
    left = 0
    right = len(highest_num - 1)
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return None


def main():
    print("Welcome!")
    print()
    binary_search(

