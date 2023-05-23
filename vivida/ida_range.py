import bisect

class range_t:
    def __init__(self, start_ea, end_ea):
        """
        Initializes a range object with a start and end value.
        Throws a ValueError if the start value is greater than or equal to the end value.
        """
        if start_ea >= end_ea:
            raise ValueError("Start must be less than end")
        self.start_ea = start_ea
        self.end_ea = end_ea

    def size(self):
        """
        Returns the size of this range.
        """
        return self.end_ea - self.start_ea
    
    def __lt__(self, other):
        """
        Returns True if the start of this range is less than the start of another range.
        """
        return self.start_ea < other.start

    def __eq__(self, other):
        """
        Returns True if the start and end of this range equal the start and end of another range.
        """
        return self.start_ea == other.start and self.end_ea == other.end

    def contains(self, ea):
        """
        Checks if a value is contained within this range.
        Returns True if the value is greater than or equal to the start and less than the end of this range.
        """
        return self.start_ea <= ea < self.end_ea

    def intersects(self, other):
        """
        Checks if this range intersects with another range.
        Returns True if there is any overlap in the ranges, False otherwise.
        """
        return (self.start_ea < other.end and other.start < self.end_ea)

    def overlaps(self, other):
        return other.start_ea < self.end_ea and self.start_ea < other.end_ea



class ranges_t:
    def __init__(self):
        self.ranges = []

    def add_range(self, range_obj):
        if not isinstance(range_obj, range_t):
            raise TypeError("range_obj must be an instance of RangeObject or its subclass")

        idx = bisect.bisect_right(self.ranges, range_obj)

        if idx != 0:
            prev_range = self.ranges[idx - 1]
            if prev_range.end > range_obj.start:
                raise ValueError("Overlapping ranges are not allowed")

        if idx != len(self.ranges):
            next_range = self.ranges[idx]
            if next_range.start < range_obj.end:
                raise ValueError("Overlapping ranges are not allowed")

        bisect.insort(self.ranges, range_obj)

    def find_nearest_range(self, offset):
        new_range = range_t(offset, offset + 1)
        idx = bisect.bisect_right(self.ranges, new_range)

        if idx != 0:
            prev_range = self.ranges[idx - 1]
            if prev_range.start <= offset <= prev_range.end:
                return prev_range
            elif idx != len(self.ranges):
                next_range = self.ranges[idx]
                if offset - prev_range.end <= next_range.start - offset:
                    return prev_range

        if idx != len(self.ranges):
            return self.ranges[idx]

        return None

"""
class myrange_t(range_t):
    def __init__(self, start, end, data=None):
        super().__init__(start, end)
        self.data = data

rf = ranges_t()
rf.add_range(myrange_t(0, 10, "some data"))

t = rf.find_nearest_range(5)
t = rf.find_nearest_range(15)
print(t.data)
"""
