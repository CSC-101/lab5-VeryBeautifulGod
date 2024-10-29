import data
from data import Time
# Write your functions for each part in the space below.

# Part 1
   # The function for Part 1 should be within the class in data.py.


# Part 2
   # The function for Part 2 should be within the class in data.py.


# Part 3
def time_add(time1: Time, time2: Time) -> Time:
    new_hour = time1.hour + time2.hour
    new_minute = time1.minute + time2.minute
    new_second = time1.second + time2.second

    if new_second >= 60:
        new_minute = new_minute + new_second // 60
        new_second = new_second % 60

    if new_minute >= 60:
        new_hour = new_hour + new_minute // 60
        new_minute = new_minute % 60

    return Time(new_hour, new_minute, new_second)


# Part 4
def is_descending(lst: list[float]) -> bool:
    for i in range(len(lst) - 1):
        if lst[i] <= lst[i + 1]:
            return False
    return True


# Part 5
def largest_between(numbers, lower, upper):
    if lower > upper:
        return None

    adjusted_lower = max(0, lower)
    adjusted_upper = min(len(numbers) - 1, upper)

    if adjusted_lower > adjusted_upper:
        return None

    largest_index = adjusted_lower
    for i in range(adjusted_lower, adjusted_upper + 1):
        if numbers[i] > numbers[largest_index]:
            largest_index = i

    return largest_index

# Part 6
def furthest_from_origin(points):
    if not points:
        return None

    furthest_index = 0
    max_distance_squared = points[0].x**2 + points[0].y**2

    for i in range(1, len(points)):
        distance_squared = points[i].x**2 + points[i].y**2
        if distance_squared > max_distance_squared:
            max_distance_squared = distance_squared
            furthest_index = i

    return furthest_index
