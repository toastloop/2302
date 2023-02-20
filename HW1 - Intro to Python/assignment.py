print("\nFizzBuzz\n")

"""
Exercise 1: Write a program that prints the numbers from 1 to n, but on 
multiples of 3 will print "fizz", on multiples of 5 will print "buzz", 
and on multiples of both 3 and 5 will print "fizzbuzz". For example, the 
start of your output should look like:

1:
2:
3: fizz
4:
5: buzz
6: fizz
7:
8:
9: fizz
10: buzz
11:
12: fizz
13:
14:
15: fizzbuzz
16:
"""

def fizzbuzz(n: int) -> None:
    for i in range(1,n+1):
        print(f"{i}: {'' if i%3 else 'fizz'}{'' if i%5 else 'buzz'}")

fizzbuzz(35)

print("\nNested Parentheses\n")

"""
Exercise 2: Given a string, return true if it is a nesting of zero or more 
pairs of parenthesis, like "(())" or "((()))". Suggestion: check the first 
and last chars, and then recur on what's inside them.

nest_paren("(())") → True
nest_paren("((()))") → True
nest_paren("(((x))") → False
"""

def nest_paren(s: str) -> bool:
    cache: list[str] = []
    opening: str = "([{<"
    closing: str = ")]}>"
    pair: dict[str, str] = dict(zip(closing, opening))
    for char in s:
        if char in opening: cache.append(char)
        if char in closing:
            if len(cache) == 0 or cache[-1] != pair.get(char): 
                return False
            else: cache.pop()
    return len(cache) == 0

print(nest_paren(s="(())"))
print(nest_paren(s="((())"))
print(nest_paren(s="(((x))"))
print(nest_paren(s="<hello{[()]}>[world]"))

print()