def romanToInt(s: str) -> int:
        roman_values = {
            "I" : 1,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000
        }
        result = 0
        
        nums = [roman_values[letter] for letter in s]
        
        for x in range(len(nums) - 1):
            if nums[x] < nums[x + 1]:
                result -= nums[x]
            else:
                result += nums[x]

        return result + nums[-1]
    
romanToInt(s="MIV")