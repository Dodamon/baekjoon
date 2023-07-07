import sys
input = sys.stdin.readline

def next_permutation(nums, N) -> list:

    # 바뀌는 순열 인덱스를 찾는다
    i = N-1
    while i > 0 and nums[i-1] <= nums[i]: i -= 1
    if i == 0: return {-1}

    j = N-1
    while j > i-1 and nums[i-1] <= nums[j]: j -= 1


    # swap
    nums[i-1], nums[j] = nums[j], nums[i-1]
    return nums[:i] + sorted(nums[i:], reverse=True)


def solution() -> None:
    N = int(input())
    nums = list(map(int, input().split()))
    print(*next_permutation(nums, N), sep=" ")


solution()