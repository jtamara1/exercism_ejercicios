def convert(number):
    array = ["Pling" if number % 3 == 0 else "",
             "Plang" if number % 5 == 0 else "",
             "Plong" if number % 7 == 0 else ""]
    return "".join(array) if len("".join(array)) > 0 else f"{number}"
