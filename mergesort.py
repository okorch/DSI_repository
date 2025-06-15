import matplotlib.pyplot as plt


def assigment(new_list, i, old_list, j):
    new_list[i] = old_list[j]


def mergeSort(arr):

    if len(arr) <= 1:
        return

    else:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        mergeSort(left)
        mergeSort(right)

        left_index = 0
        right_index = 0
        i = 0

        while left_index < len(left) and right_index < len(right):
            if left[left_index] <= right[right_index]:
                assigment(new_list=arr, i=i, old_list=left, j=left_index)
                left_index += 1
            else:
                assigment(new_list=arr, i=i, old_list=right, j=right_index)
                right_index += 1
            i += 1

        while left_index < len(left):
            arr[i] = left[left_index]
            left_index += 1
            i += 1

        while right_index < len(right):
            arr[i] = right[right_index]
            right_index += 1
            i += 1


import matplotlib.pyplot as plt

def plot_list(data, title):
    plt.figure(figsize=(10, 4))
    x = range(len(data))
    plt.bar(x, data, color='skyblue')
    plt.title(title)
    plt.xlabel("Index")
    plt.ylabel("Value")
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show()


my_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]

plot_list(my_list, "Before Merge Sort")

mergeSort(my_list)

plot_list(my_list, "After Merge Sort")
