from __future__ import annotations

import cProfile
import enum
from random import randint
from typing import Protocol, TypeVar, SupportsIndex
import sys

sys.setrecursionlimit(2000)


class Comparable(Protocol):
    def __gt__(self, other: Comparable) -> bool:
        ...


def cmp(a: Comparable, b: Comparable) -> bool:
    return a > b


def swap(arr: list[Comparable], i: SupportsIndex, j: SupportsIndex) -> None:
    arr[i], arr[j] = arr[j], arr[i]


def bubble_sort(arr: list[Comparable]) -> list[Comparable]:
    for i in range(len(arr)):
        for j in range(len(arr) - 1):
            if cmp(arr[j], arr[j + 1]):
                swap(arr, j, j + 1)
    return arr


def quick_sort(arr: list[Comparable]) -> list[Comparable]:
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
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)


def merge(left: list[Comparable], right: list[Comparable]) -> list[Comparable]:
    result = []
    while left and right:
        if cmp(right[0], left[0]):
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    return result + left + right


def main() -> int:
    cProfile.run("bubble_sort(very_large_input)")
    cProfile.run("quick_sort(very_large_input)")
    cProfile.run("merge_sort(very_large_input)")

    return 0


if __name__ == "__main__":
    very_large_input = [randint(0, 1000) for _ in range(3000)]
    raise SystemExit(main())
