# numbers=int(input("Enter a number\n"))
#
# match numbers:
#     case 1:
#         print("You have entered number 1")
#
#     case 2:
#         print("You have entered number 2")
#
#     case 3:
#         print("You have entered number 3")
#
#     case 4:
#         print("You have entered number 4")
#
#     case 5:
#         print("You have entered number 5")
#
#     case _:
#         print("No Idea")

Names=str(input("Enter a name\n")).lower()

match Names:
    case "krishna":
        print("You are Krishna")

    case "sunil":
        print("You are Sunil")

    case _:
        print("No Idea")