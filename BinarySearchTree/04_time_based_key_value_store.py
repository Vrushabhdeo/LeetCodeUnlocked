from typing import Dict


# class TimeMap:
#
#     def __init__(self):
#         self.key_val_pair = Dict[str, Dict[int, str]]
#
#     def set(self, key: str, value: str, integer: int) -> None:
#         self.key_val_pair[key][integer] =  value
#         print("Set Complete")
#         print(self.key_val_pair)
#
#     def get(self, key: str, integer: int) -> str:
#         val = self.key_val_pair[key].get(integer, -1)
#         if val != -1:
#             return val
#         else:
#             for _ in range(1,integer, -1):
#                 print(_)


# class TimeMap:
#
#     def __init__(self):
#         self.key_val_pair: Dict[str, Dict[int, str]] = {}
#
#     def set(self, key: str, value: str, integer: int) -> None:
#         if key not in self.key_val_pair:
#             self.key_val_pair[key] =  {}
#         self.key_val_pair[key][integer] = value
#         print("Set Complete")
#         print(self.key_val_pair)
#
#     def get(self, key: str, integer: int) -> str:
#         if key not in self.key_val_pair:
#             return ""
#         if integer in self.key_val_pair[key]:
#             return self.key_val_pair[key][integer]
#
#         max_time = -1
#         for int_time in self.key_val_pair[key]:
#             if int_time <= integer and int_time >= max_time:
#                 max_time = int_time
#         return self.key_val_pair[key].get(max_time, "")

from collections import defaultdict
import bisect

class TimeMap:
    def __init__(self):
        self.store = defaultdict(list)  # key -> [(timestamp, value)]

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((timestamp, value))  # list remains sorted by insertion

    def get(self, key: str, timestamp: int) -> str:
        values = self.store.get(key, [])
        i = bisect.bisect_right(values, (timestamp, chr(127)))
        return values[i-1][1] if i > 0 else ""

# Your TimeMap object will be instantiated and called as such:
timemap = TimeMap()
timemap.set("foo", "bar", 1)
timemap.set("foo", "bar2", 3)
print(timemap.get("foo", 3))