import copy

count_num, count_create_digits = map(int, input().split())
numbers = list(map(int, input().split()))


def get_raz(num):
    return len(str(num))


def get_first_and_ost_from_num(num):
    if num == 0 or num is None:
        return None, None
    first_digit = num % 10
    whole_num = num // 10
    return first_digit, whole_num if whole_num != 0 else None


def sum_list_numbers(list_numbers):
    remainder = 0
    result = ""
    for line in list_numbers:
        line_sum = sum(filter(lambda x: x is not None, line)) + remainder
        first, ost = get_first_and_ost_from_num(line_sum)
        remainder = ost if ost is not None else 0
        result += str(first) if first is not None else ''
    if remainder is not None:
        result += str(remainder)
    return result[::-1]


def calculate(numbers, times_of_change):
    list_numbers = []
    max_num = max(numbers)
    temp_line = copy.copy(numbers)

    for _ in range(get_raz(max_num)):
        line = []
        for i, num in enumerate(temp_line):
            first, whole = get_first_and_ost_from_num(num)
            line.append(first)
            temp_line[i] = whole
        list_numbers.append(line)

    count_changes = 0
    rev_list_numbers = list_numbers[::-1]

    for line in rev_list_numbers:
        for _ in line:
            min_dig = min(filter(lambda x: x is not None, line))
            if min_dig == 9:
                break
            min_dig_idx = line.index(min_dig)
            if count_changes < times_of_change:
                line[min_dig_idx] = 9
                count_changes += 1
            else:
                break

    list_numbers = rev_list_numbers[::-1]
    return int(sum_list_numbers(list_numbers)) - sum(numbers)


res = calculate(numbers, count_create_digits)
print(res)
