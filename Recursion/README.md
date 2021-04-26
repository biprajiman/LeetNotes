# Description
Problems in this category can be solved with recursion.

# Generic Format:
``` Python
def some_function(parameter):
    if parameter == base_case:
        return
    
    some_function(updated_parameter)
```

# General Notes:
- Think about base case.
- Some the brute force solution could be recursion problem.

# Problem Note:
- Convert non-negative integer number to its English words representation ([Leetcode Problem 273](https://leetcode.com/problems/integer-to-english-words/))
    - Brute force the solution.
    - Talk through for the upper bound relevant for the problem. Assumption less than or equal to billion.
    - Handle default case of 0.
    - Create dictionary for ones, tens and between 11 and 20.
    - Recurse with multiple if statement.
    - If n >= BILLION:
        return f(n//BILLION) + 'Billion ' + f(n % BILLION)
    - If n >= MILLION:
        return f(n//MILLION) + 'Million ' + f(n % MILLION)
    - If n >= THOUSAND:
        return f(n//THOUSAND) + 'Thousand ' + f(n % THOUSAND)
    - If n >= 100:
        return f(n//100) + 'Hundred ' + f(n % 100)
    - If 10 <= n <= 19: return d[n] + ' '
    - If n > 10:
        return tens[n // 10] + ' ' + f(n % 10)
    - default: return ones[n] if n == 0 else ones[n] + ' '