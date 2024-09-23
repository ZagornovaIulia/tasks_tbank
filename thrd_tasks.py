def get_time_from_floors(flor_1, flor_2):
    return abs(flor_1 - flor_2) * time_for_one_floor


def calc(floors, time, num_floor):
    max_floor, min_floor = floors[-1], floors[0]
    employer_floor = floors[num_floor - 1]
    time_to_down = get_time_from_floors(employer_floor, max_floor)
    time_to_up = get_time_from_floors(employer_floor, min_floor)
    time_all_floors = get_time_from_floors(max_floor, min_floor)

    if time_to_up < time_to_down:
        if time_to_up < time:
            return time_all_floors
        else:
            return time_to_up * 2 + time_to_down
    else:
        if time_to_down < time:
            return time_all_floors
        else:
            return time_to_down * 2 + time_to_up


count, time = map(int, input().split())
floors = list(map(int, input().split()))
num_floor = int(input())
time_for_one_floor = 1

res = calc(floors, time, num_floor)
print(res)
