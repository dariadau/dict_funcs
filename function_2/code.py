def count_variatons(self, nums: [int]) -> int:
    pairs_tuple = tuple(x * y for i, x in enumerate(nums) for y in nums[i + 1:])
    pairs_dict = {}
    result = 0
    for pair in pairs_tuple:
        if pair not in pairs_dict:
            pairs_dict[pair] = 1
        else:
            pairs_dict[pair] += 1
    for value in pairs_dict.values():
        if value > 1:
            # Формула для выбора 2 элементов из n (где порядок не важен) — это комбинации,
            # которая равна  C(n, 2) = (n(n-1))/2
            result += (value * (value - 1) * 8) // 2
    return result
