# 41. 缺失的第一个正数

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