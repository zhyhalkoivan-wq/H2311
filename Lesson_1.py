# a = int(input("enter a: "))
# b = int(input("enter b: "))
# print
# def line(count, simbol):
#     for i in range(count):
#         print(simbol, end=" ")
#     print()
#
# line(20, "#")
# line(50, "-")
# import numbers
#
# number = int(input("Enter a number: "))
# for i in range(2, 10):
#     print(f"{number} x {i} = {i * number}")

# a = 1
# while a < 6:
#     print(a, end = " ")
#     a = a + 1


#number = int(input("Enter a number: "))
#if number % 2 == 0:
 #   print("even")
#else:
#    print("not even")


def ramka(message, symbol):
    border = symbol * (len(message) + 4)
    print(border)
    print(f"{symbol} {message} {symbol}")
    print(border)


ramka("Я люблю Python", "*")


