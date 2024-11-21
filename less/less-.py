# def degrees(num, max_degree):
#     i = 0
#     for deg in range(max_degree):
#         yield num**i
#         i += 1
#
#
# res = degrees(5, 4)
# print(res)
#
# for i in res:
#     print(i)
#
# print("===============")
#
# for i in res:
#     print(i)

def new_degrees(num):
    i = 0
    while True:
        result = num ** i
        yield result
        if result > 10**5:
            return
        i += 1

res = new_degrees(5)
print(res)

for num in res:
    print(num)