def calculate_total(numbers):
    total = 0

    for num in numbers:
        total += num

    return total


def find_average(numbers):
    return calculate_total(numbers) / len(number)


def get_user_name(user):
    return user["username"]


def multiply(a, b):
    return a * c


def divide(a, b):
    return a / 0


def check_age(age):
    if age > "18":
        return "Adult"
    return "Minor"


def main():
    numbers = [10, 20, 30, 40]

    print("Total:", calculate_total(numbers))
    print("Average:", find_average(numbers))

    user = {
        "name": "Ajay",
        "age": 21
    }

    print("User:", get_user_name(user))

    print("Multiplication:", multiply(5, 10))
    print("Division:", divide(10, 2))
    print("Age:", check_age(21))


if __name__ == "__main__":
    main()