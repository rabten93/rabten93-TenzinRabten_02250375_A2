# TenzinRabten_02250375_A2_PB.py
# Part B: Sorting Algorithms Implementation
# -----------------------------------------
# This program implements Bubble Sort, Insertion Sort, and Quick Sort algorithms.

def bubble_sort(names):
    n = len(names)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if names[j] > names[j + 1]:
                names[j], names[j + 1] = names[j + 1], names[j]
    return names


def insertion_sort(scores):
    for i in range(1, len(scores)):
        key = scores[i]
        j = i - 1
        while j >= 0 and key < scores[j]:
            scores[j + 1] = scores[j]
            j -= 1
        scores[j + 1] = key
    return scores


def quick_sort(prices, depth=0):
    if len(prices) <= 1:
        return prices, 1
    pivot = prices[0]
    left = [x for x in prices[1:] if x <= pivot]
    right = [x for x in prices[1:] if x > pivot]

    left_sorted, left_calls = quick_sort(left, depth + 1)
    right_sorted, right_calls = quick_sort(right, depth + 1)

    total_calls = 1 + left_calls + right_calls
    return left_sorted + [pivot] + right_sorted, total_calls


def main():
    student_names = ["Kado", "Bobchu", "Zamu", "Nado", "Lemo", "Choden", "Pema", "Sonam",
                     "Ugyen", "Tashi", "Wangmo", "Dechen", "Dema", "Jigme", "Karma"]

    test_scores = [78, 45, 92, 67, 88, 54, 73, 82, 91, 59, 76, 85, 48, 93, 71, 89, 57, 80, 69, 62]

    book_prices = [450, 230, 678, 125, 890, 315, 450, 765, 980, 215, 540, 385, 610, 410, 280]

    while True:
        print("\n=== Sorting Algorithms Menu ===")
        print("1. Bubble Sort - Sort Student Names")
        print("2. Insertion Sort - Sort Test Scores")
        print("3. Quick Sort - Sort Book Prices")
        print("4. Exit program")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            print(f"Original: {student_names}")
            sorted_names = bubble_sort(student_names.copy())
            print(f"Sorted: {sorted_names}")

        elif choice == '2':
            print(f"Original scores: {test_scores}")
            sorted_scores = insertion_sort(test_scores.copy())
            print(f"Sorted scores: {sorted_scores}")
            print("Top 5 Scores:")
            for i, score in enumerate(sorted_scores[-5:][::-1], start=1):
                print(f"{i}. {score}")

        elif choice == '3':
            print(f"Original prices: {book_prices}")
            sorted_prices, calls = quick_sort(book_prices.copy())
            print(f"Sorted prices: {sorted_prices}")
            print(f"Recursive calls: {calls}")

        elif choice == '4':
            print("Thank you for using the sorting program!")
            break

        else:
            print("Invalid choice! Please enter 1-4.")
            continue

        again = input("Would you like to perform another sort? (y/n): ")
        if again.lower() != 'y':
            print("Thank you for using the sorting program!")
            break


if __name__ == "__main__":
    main()
