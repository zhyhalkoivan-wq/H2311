result = []

def divider(a, b):
    if a < b:
        raise ValueError
    if b > 100:
        raise IndexError
    return a / b

data = [(10, 2), (2, 5), ("123", 4), (18, 0), ([], 15), (8, 4)]

for a, b in data:
    try:
        res = divider(a, b)
        result.append(res)
    except ValueError as e:
        print("ValueError")
    except IndexError as e:
        print("IndexError")
    except TypeError as e:
        print("TypeError")
    except ZeroDivisionError as e:
        print("ZeroDivisionError")

print(result)