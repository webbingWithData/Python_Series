# try:
#     num = int(input("Enter a number: "))
#     print("You entered:", num)
# except ValueError:
#     print("That's not a valid number!")
# finally:
#     print("This will always execute, no matter what.")


# else block
# try:
#     num = int(input("Enter a number: "))
# except ValueError:
#     print("That's not a valid number!")
# else:
#     print("Great! You entered a valid number:", num)


try:
    num = int(input("Enter a number: "))
except ValueError:
    print("Invalid input!")
else:
    print("You entered:", num)
finally:
    print("Execution completed.")