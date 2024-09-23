def calculate(numbers):
    if all(1 <= num <= 100 for num in numbers):
        a, b, c, d = numbers
        if d >= b:
            return (d - b) * c + a
        else:
            return a
    else:
        raise ValueError(
            "Invalid input. Please enter numbers between 1 and 100.")


a, b, c, d = map(int, input().split())
numbers = [a, b, c, d]
result = calculate(numbers)
print(result)
