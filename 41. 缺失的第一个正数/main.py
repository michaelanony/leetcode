"""
给你一个未排序的整数数组，请你找出其中没有出现的最小的正整数。

示例 1:

输入: [1,2,0]
输出: 3

提示：

你的算法的时间复杂度应为O(n)，并且只能使用常数级别的额外空间。
"""
class Solution:
    def firstMissingPositive(self, nums) -> int:
        tmp = []
        [tmp.append(i) for i in nums if i >0 and i not in tmp]
        tmp.sort()
        if tmp:
            count = tmp[0]
            if count != 1:
                return 1
            for num in tmp:
                if num == count:
                    count += 1 
                    continue
                break
            return count
        else:
            return 1
if __name__ == "__main__":
    s = Solution()
    case1 = [-1]
    ret1 = s.firstMissingPositive(case1)
    assert ret1 == 1
    case2=[0,2,2,1,1]
    ret2 = s.firstMissingPositive(case2)
    assert ret2 == 3
    case3 = [7,8,9,11,12]
    ret3 = s.firstMissingPositive(case3)
    assert ret3 == 1