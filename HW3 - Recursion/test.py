def fun1(n):
    if(n == 1):
        return 0
    else:
        return 1 + fun1(n//2)

print(fun1(6))

def foo(a, b):
    if (b == 0):
        return 0
    if (b % 2 == 0):
        return foo(a + a, b//2)
    
    return foo(a + a, b//2) + a

print(foo(6,10))

def prod_two(nums):
  return (nums[0] if len(nums) % 2 else 1) * prod_two(nums[1:]) if nums else 1

print(prod_two([1,2,3,4,5]))

print("Hello World".lower())