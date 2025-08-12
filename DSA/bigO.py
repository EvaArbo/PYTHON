# DSA 
#bigO 
# Big O Notation
# Time Complexity
# Space Complexity


import time
def calculate_sum(n):
    total = 0
    for numb in range(1, n + 1):
        print(f"Sum= {total} , numb= {numb}")
        total= total + numb
        print(f"For {n} total is {total}")
    return total

start_time=time.time()
calculate_sum(10)
end_time=time.time()
diff=end_time-start_time
print(f"Speed is {diff}")
# Big O Notation
