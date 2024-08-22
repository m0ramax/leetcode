def intToRoman(num: int) -> int:
    roman = {
        1: "I",
        4: "IV",
        5: "V",
        9: "IX",
        10: "X",
        40: "XL",
        50: "L",
        90: "XC",
        100: "C",
        400: "CD",
        500: "D",
        900: "CM",
        1000: "M",
    }
    count = ""

    for i in sorted(roman.keys(), reverse=True):
        while num >= i:
            count += roman[i]
            num -= i
    return count 


def romanizer(numbers):
    return [intToRoman(num) for num in numbers]


print(romanizer([1, 49, 23]))  # 3
