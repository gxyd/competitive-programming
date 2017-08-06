#!/usr/bin/python3

def merge(arr, aux, low, mid, high):
    k = low
    i = low
    j = mid + 1
    while i <= mid and j <= high:
        if arr[i] <= arr[j]:
            aux[k] = arr[i]
            k += 1
            i += 1
        else:
            aux[k] = arr[j]
            k += 1
            j += 1

    while i <= mid:
        aux[k] = arr[i]
        k += 1
        i += 1

    for i in range(low, high+1):
        arr[i] = aux[i]
