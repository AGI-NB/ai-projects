# for i in range(7):
#     for j in range(1,i+1):
#         print(j, end=' ')
#     print()

# for i in range(7):
#     for j in range(1,i+1):
#         print("*", end=' ')
#     print()

for i in range(1,9):
    for j in range(1,9):
        if (j % 2 != 0 and i % 2 != 0 or j % 2 == 0 and i % 2 == 0):
            print("◆", end=' ')
        else:
            print("◇", end=' ')
    print(" ")