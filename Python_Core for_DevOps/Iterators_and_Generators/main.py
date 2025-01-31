def time_range(time_start: tuple, time_end: tuple) -> tuple:
    def time_to_seconds(t: tuple[int, int, int]) -> int:
        hours, minutes, seconds = t
        return hours * 3600 + minutes * 60 + seconds

    def seconds_to_time(s: int) -> tuple[int, int, int]:
        hours = (s // 3600) % 24
        minutes = (s % 3600) // 60

        seconds = s % 60
        return hours, minutes, seconds

    start_seconds = time_to_seconds(time_start)
    end_seconds = time_to_seconds(time_end) 

    if end_seconds < start_seconds:
        end_seconds += 24 * 3600
    current_seconds = start_seconds
    while current_seconds <= end_seconds:
        yield seconds_to_time(current_seconds)
        current_seconds += 1


t_range = time_range(time_start=(10, 10, 6),
                     time_end=(10, 20, 9))
print(next(t_range))  # == (10, 0, 0)
# print(next(t_range))  # == (10, 0, 1)
# print(next(t_range))  # == (10, 0, 2)
# next(t_range)
# Error: StopIteration
# t_range = time_range(time_start=(23, 59, 59),
#                      time_end=(0, 0, 3))
# t_range_list = list(t_range)
# print(t_range_list)
#  == [
#   (23, 59, 59),
#   (0, 0, 0),
#   (0, 0, 1),
#   (0, 0, 2)
# ])
