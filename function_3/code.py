def check_mismatch(nums: [int]) -> [int]:
    chk_dict = {x: 0 for x in range(1, len(nums) + 1)}
    a = int()
    b = int()
    for num in nums:
        chk_dict[num] += 1
    for key in chk_dict:
        if chk_dict[key] == 2:
            a = key
        elif chk_dict[key] == 0:
            b = key
    return [a, b]
