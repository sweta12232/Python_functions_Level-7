def is_palindrome(n):
    temp = n
    rev = 0
    while temp > 0:
        rem = temp % 10
        rev = rev * 10 + rem
        temp = temp // 10
    return n == rev

def palindrome_range(start, end):
    palindromes = []
    
    for num in range(start, end + 1):
        if is_palindrome(num):
            palindromes.append(num)
    
    return palindromes

# Find palindromic numbers between 500 and 1000
palindromic_numbers = palindrome_range(500, 1000)
print("Palindromic numbers between 500 and 1000:", palindromic_numbers)
