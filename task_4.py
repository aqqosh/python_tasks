def less_digits_than_n (digits, n):
    cnt = 0
    for i in range (1, len(str(n))):
        cnt += len(digits)** i
    return cnt
    
def same_digits_than_n (digits, n):
    s = str(n)
    cnt = 0 
    for i in range (len(s)):
        valid_digits_counter = 0
        for d in digits:
            if d < s[i]:
                valid_digits_counter+=1
        cnt+= valid_digits_counter * (len(digits)**(len(s)-i-1))
        if s[i] not in digits:
            break
        cnt+=1 if i==len(s)-1 else 0
    return cnt
                    
            
def atMostNGivenDigitSet(digits,n) -> int:
    return less_digits_than_n(digits, n) + same_digits_than_n(digits,n)

digits = ["5","6","7"]
n = 190

atMostNGivenDigitSet(digits=digits, n=n)