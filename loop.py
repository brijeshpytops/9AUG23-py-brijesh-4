# range(start, stop, step)
# nums = list(range(0, 21, 2))
# print(nums)

# for var in range(1, 21):
#     print(var)

# how for work exactly?
# l = range(1, 6)
# l1 = iter(l)
# print(next(l1))
# print(next(l1))
# print(next(l1))
# print(next(l1))
# print(next(l1))
# print(next(l1))

# name = "python"
# for i in name:
#     print(i)

# for pos in range(len(name)):
#     # print(name[pos])

#     if name[pos] == 't':
#         continue
#     elif pos == 3:
#         pass
#     elif pos == 4:
#         break
    
#     print(name[pos])

# print("hello")


# product = {
#     'tomato':20,
#     'potato':50,
#     'pen':54
# }

# print(product.items())

# for k, v in product.items():
#     print(k, v)

# nums = [(1,2,3), (2,3,4), (3,4,5)]

# for a,b,c in nums:
#     print(a,b,c)

# for a,b in nums:
#     print(a,b)


# a,b,c = 10,20,30

num = 11

# for r in range(1, num):
#     for c in range(1, num):
#         print("*", end=" ")
# #     print("")

# * * * * * * * * * *
# * * * * * * * * * *
# * * * * * * * * * *
# * * * * * * * * * *
# * * * * * * * * * *
# * * * * * * * * * *
# * * * * * * * * * *
# * * * * * * * * * *
# * * * * * * * * * *
# * * * * * * * * * *


# for r in range(1, num):
#     for c in range(1, r+1):
#         print("*", end=" ")
#     print("")

# *
# * *
# * * *
# * * * *
# * * * * *
# * * * * * *
# * * * * * * *
# * * * * * * * *
# * * * * * * * * *
# * * * * * * * * * *


# for r in range(1, num):
#     for c in range(1, num-r):
#         print("*", end=" ")
#     print("")

# * * * * * * * * *
# * * * * * * * *
# * * * * * * *
# * * * * * *
# * * * * *
# * * * *
# * * *
# * *
# *

# for r in range(1, num):
#     for c in range(1, r+1):
#         print(" ", end=" ")
#     for c in range(1, num-r):
#         print("*", end=" ")
#     print("")

#   * * * * * * * * *
#     * * * * * * * *
#       * * * * * * *
#         * * * * * *
#           * * * * *
#             * * * *
#               * * *
#                 * *
#                   *

# for r in range(1, num):
#     for c in range(1, num-r):
#         print(" ", end=" ")
#     for c in range(1, r+1):
#         print("*", end=" ")
#     print("")

#                   *
#                 * *
#               * * *
#             * * * *
#           * * * * *
#         * * * * * *
#       * * * * * * *
#     * * * * * * * *
#   * * * * * * * * *
# * * * * * * * * * *

# for r in range(1, num):
#     for c in range(1, num-r):
#         print(" ", end=" ")
#     for c in range(1, r+1):
#         print("*", end=" ")
#     for c in range(1, r):
#         print("*", end=" ")
#     print("")

#                   *
#                 * * *
#               * * * * *
#             * * * * * * *
#           * * * * * * * * *
#         * * * * * * * * * * *
#       * * * * * * * * * * * * *
#     * * * * * * * * * * * * * * *
#   * * * * * * * * * * * * * * * * *
# * * * * * * * * * * * * * * * * * * *

# For assignment

# * * * * * * *
# *   *   *   *
# * * *   *   *
# *       *   * 
# * * * * *   *
# *           *
# * * * * * * * 

# while (condition):
    # block of code 

# while(1):
#     print("brijesh")




# while(1):
#     age = int(input("Enter your age : "))
#     if (age >= 18):
#         weight = int(input("Enter your weight : "))
#         if(weight >= 50):
#             print("You can donate")
#         else:
#             print("You can not donate")
#     else:
#         print("You can not donate")

# start = 1
# while(start<=10):
#     print("Num : ", start)
#     start += 1


# 0 1 1 2 3 5 8....
# n1 = 0
# n2 = 1
# num = 10
# i = 1
# while(i<=num):
#     if i == 1:
#         print(n1, end=" ")
#     elif i == 2:
#         print(n2, end=" ")
#     else: 
#         nth = n1 + n2  
#         n1 = n2
#         n2 = nth
        
#         print(nth, end=" ")
#     i += 1

# 1 * 2 * 3 * 4 * 5
# num = 5 # 120
# total = 1
# i = 1 
# while (num >= i):
#     total *= num
#     num -= 1
# print("Factorial: ", total)


