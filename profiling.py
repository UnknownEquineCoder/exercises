from __future__ import annotations

import cProfile
from random import randint
from typing import Protocol, SupportsIndex
import sys

# Python's stack frame limit is set to 1000 by default.
# This is not enough for the recursive quick sort algorithm.
# Increase this limit to your heart's content.
sys.setrecursionlimit(2000)


class Comparable(Protocol):
    """
    A protocol for types that can be compared to each other.
    """

    def __gt__(self, other: Comparable) -> bool:
        ...


def cmp(a: Comparable, b: Comparable) -> bool:
    """
    Quickest way to export the __gt__ method of any class.
    """
    return a > b


def swap(arr: list[Comparable], i: SupportsIndex, j: SupportsIndex) -> None:
    """
    Quickest way to export the tuple swap syntax.
    """
    arr[i], arr[j] = arr[j], arr[i]


def bubble_sort(arr: list[Comparable]) -> list[Comparable]:
    """
    Not the most efficient sorting algorithm, but it's easy to understand.
    """
    for _ in len(arr):
        for j in range(len(arr) - 1):
            if cmp(arr[j], arr[j + 1]):
                swap(arr, j, j + 1)
    return arr


def quick_sort(arr: list[Comparable]) -> list[Comparable]:
    """
    A recursive quick sort algorithm.
    """
    if len(arr) <= 1:
        return arr
    pivot = arr.pop()

    left: list[Comparable] = []
    right: list[Comparable] = []

    for el in arr:
        if cmp(pivot, el):
            left.append(el)
        else:
            right.append(el)

    return quick_sort(left) + [pivot] + quick_sort(right)


def merge_sort(arr: list[Comparable]) -> list[Comparable]:
    """
    Classic merge sort algorithm.
    """
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)


def merge(left: list[Comparable], right: list[Comparable]) -> list[Comparable]:
    """
    Merge two sorted lists into one sorted list.
    """
    result: list[Comparable] = []
    while left and right:
        if cmp(right[0], left[0]):
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    return result + left + right


def main() -> int:
    # Profile bubble sort
    cProfile.run("bubble_sort(very_large_input)")

    # Profile quick sort
    cProfile.run("quick_sort(very_large_input)")

    # Profile merge sort
    cProfile.run("merge_sort(very_large_input)")

    return 0


if __name__ == "__main__":
    # A list with 3k random numbers between 0 and 1000.
    very_large_input = [randint(0, 1000) for _ in range(3000)]

    raise SystemExit(main())
