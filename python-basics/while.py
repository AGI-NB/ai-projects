total = 0
i = 1
while i <= 100:
    if i % 2 == 0:
        total += i
    i += 1
else:
    print(f"所有偶数的和为: {total}")

#优化一
total = 0
i = 2
while i <= 100:
    total += i
    i += 2
print(f"所有偶数的和为: {total}")
#优化二
total = (2 + 100) * 50 / 2
print(f"所有偶数的和为: {total}")