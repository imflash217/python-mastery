class Set:
    def __init__(self):
        self._elements = []  # IMP! always kept in SORTED order

    def __len__(self):
        return len(self._elements)

    def __contains__(self, value):
        """Takes O(log_n) time due to Binary Search in self._get_position() method"""
        idx = self._get_position(value)
        return idx < len(self) and self._elements[idx] == value

    def __eq__(self, other) -> bool:
        assert type(self) == type(other)
        if len(self) != len(other):
            return False
        # return self.is_subset_of(other) # Takes O(n*log_n) time
        for x, y in zip(self._elements, other._elements):
            if x != y:
                return False
        return True

    def _get_position(self, value):
        """Uses Binary Search to find the position of an element. Takes O(log_n) time"""
        low = 0
        high = len(self._elements) - 1
        while low <= high:
            mid = (low + high) // 2
            if value == self._elements[mid]:
                return mid
            elif value < self._elements[mid]:
                high = mid - 1
            else:
                low = mid + 1
        return low

    def add(self, value):
        if value not in self:
            # self._elements.append(value) # TODO!: takes O(n) time; so not used
            idx = self._get_position(value)  # this step is faster. Takes O(log_n) time
            self._elements.insert(idx, value)

    def remove(self, value):
        assert value in self._elements
        idx = self._get_position(value)
        self._elements.pop(idx)

    def is_subset_of(self, other):
        """Takes O(n*log_n) time"""
        for item in self._elements:  # O(n) time
            if item not in other:  # O(log_n) time
                return False
        return True


if __name__ == "__main__":
    print("hariom")
