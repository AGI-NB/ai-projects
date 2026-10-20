# for i in range(7):
#     for j in range(1,i+1):
#         print(j, end=' ')
#     print()

# for i in range(7):
#     for j in range(1,i+1):
#         print("*", end=' ')
#     print()

# for i in range(1,9):
#     for j in range(1,9):
#         if (j % 2 != 0 and i % 2 != 0 or j % 2 == 0 and i % 2 == 0):
#             print("◆", end=' ')
#         else:
#             print("◇", end=' ')
#     print(" ")

#优化逻辑
for row in range(1, 9):
    for col in range(1, 9):
        # 如果行号和列号相加是偶数，就打实心，否则打空心
        symbol = "◆" if (row + col) % 2 == 0 else "◇"
        print(symbol, end=' ')
    print()