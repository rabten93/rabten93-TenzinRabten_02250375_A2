# TenzinRabten_02250375_A2_PA.py
# Part A: Searching Algorithms Implementation
# --------------------------------------------
# This program allows the user to perform Linear Search and Binary Search
# using hardcoded lists. It demonstrates understanding of searching algorithms.

def linear_search(student_ids, target):
    comparisons = 0
    for i, sid in enumerate(student_ids):
        comparisons += 1
        if sid == target:
            return i + 1, comparisons
    return -1, comparisons


def binary_search(scores, target):
    low = 0
    high = len(scores) - 1
    comparisons = 0
    while low <= high:
        mid = (low + high) // 2
        comparisons += 1
        if scores[mid] == target:
            return mid + 1, comparisons
        elif scores[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1, comparisons


def main():
    student_ids = [1001, 1005, 1002, 1008, 1003, 1010, 1004, 1009, 1007, 1012,
                   1011, 1006, 1013, 1014, 1015, 1016, 1017, 1018, 1019, 1020]
    sorted_scores = [45, 52, 58, 63, 67, 72, 75, 78, 82, 85, 88, 90, 92, 95, 98, 99, 100, 102, 105, 108]

    while True:
        print("\n=== Searching Algorithms Menu ===")
        print("1. Linear Search - Find Student ID")
        print("2. Binary Search - Find Score")
        print("3. Exit program")

        choice = input("Enter your choice (1-3): ")

        if choice == '1':
            print(f"Searching in the list: {student_ids}")
            target = int(input("Enter Student ID to search: "))
            position, comparisons = linear_search(student_ids, target)
            if position != -1:
                print(f"Result: Student ID {target} found at position {position}")
            else:
                print("Student ID not found")
            print(f"Comparisons made: {comparisons}")

        elif choice == '2':
            print(f"Sorted scores: {sorted_scores}")
            target = int(input("Enter score to search: "))
            position, comparisons = binary_search(sorted_scores, target)
            if position != -1:
                print(f"Result: Score {target} found at position {position}")
            else:
                print("Score not found")
            print(f"Comparisons made: {comparisons}")

        elif choice == '3':
            print("Thank you for using the search program!")
            break

        else:
            print("Invalid choice! Please select 1-3.")
            continue

        again = input("Would you like to perform another search? (y/n): ")
        if again.lower() != 'y':
            print("Thank you for using the search program!")
            break


if __name__ == "__main__":
    main()
