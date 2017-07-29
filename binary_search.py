#!/usr/bin/python3

if __name__ == '__main__':
    def binary_search(arr, element):
        length = len(arr)
        if arr[length // 2] == element:
            return length // 2
        elif arr[0] > element or arr[-1] < element:
            return None
        elif arr[length // 2] < element:
            return binary_search(arr[length // 2:], element)
        elif arr[length // 2 ] > element:
            return binary_search(arr[:length // 2 - 1], element)
        else:
            return None

    print(binary_search([1, 2, 4, 5, 6, 7, 8, 9, 10], 3))
