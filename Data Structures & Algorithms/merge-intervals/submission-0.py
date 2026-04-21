class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda i: i[0])
        output = [intervals[0]]

        for interval in intervals[1:]:
            last_end = output[-1][1]

            if interval[0] <= last_end:
                output[-1][1] = max(last_end, interval[1])
            else:
                output.append(interval)
        return output        