# Restaurant Menu

# dish = input("Enter any dish you wanna have:- ")

# match dish:
#     case "pizza":
#         print("Serving you the Pizza!")
#     case "burger":
#         print("Serving your burger!")
#     case "pasta":
#         print("Serving you the pasta")
#     case _:
#         print("Sorry for the inconvenience, but we don't serve that sir!")

marks = int(input("Enter your marks:- "))
# >90 A >80 b
match marks:
    case n if n > 90:
        print("A")
    case n if n >80:
        print("B")
    case n if n > 70:
        print("C")
    case n if n > 60:
        print("D")
    case _:
        print("Fail")
