# palindrome
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        str_x = str(x)
        left = 0
        right = len(str_x) - 1

        while left < right:
            if not str_x[left] == str_x[right]:
                return False
            left += 1
            right -= 1
        return True


# intToRoman
def intToRoman(num):
    """
    :type num: int
    :rtype: str
    """
    values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    roman_letters = [
        "M",
        "CM",
        "D",
        "CD",
        "C",
        "XC",
        "L",
        "XL",
        "X",
        "IX",
        "V",
        "IV",
        "I",
    ]
    roman = []
    for i in range(len(values)):
        while num >= values[i]:
            num -= values[i]
            roman.append(roman_letters[i])
    return "".join(roman)


# romantoint
r = "XLV"
roman = [
        ["I", 1],
        ["V", 5],
        ["X", 10],
        ["L", 50],
        ["C", 100],
        ["D", 500],
        ["M", 1000],
    ]

result1 = 0

prev_value = 0

for i in range(len(r) - 1, -1, -1):
    for j in range(len(roman)):
        if r[i] == roman[j][0]:
            if roman[j][1] < prev_value:
                result1 -= roman[j][1]
            else:
                result1 += roman[j][1]
            prev_value = roman[j][1]
            
print(result1)

        



