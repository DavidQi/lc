class Solution(object):
    def merge(self, intervals):
        if not intervals:
            return []
        intervals = sorted(intervals, key=lambda x: x[0])

        result = [intervals[0]]
        for interval in intervals:
            if interval[0] > result[-1][-1]:
                result.append(interval)
            elif result[-1][-1] < interval[-1]:
                result[-1][-1] = interval[-1]
        return result


if __name__ == '__main__':
    l1 = [[1, 3], [2, 6], [8, 10], [15, 18]]
    l2 = [[-25, -14], [-21, -16], [-20, -15], [-10, -7], [-8, -5], [-6, -3], [2, 4], [2, 3], [3, 6], [12, 15], [13, 18],
          [14, 17], [22, 27], [25, 30], [26, 29]]
    o = Solution()
    print(o.merge(l1))
    print(o.merge(l2))
