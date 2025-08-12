"""
Bài toán: Two Sum (Tổng hai số)
Độ khó: Dễ
URL: https://leetcode.com/problems/two-sum/

Mô tả:
Cho một mảng số nguyên nums và một số nguyên target, hãy trả về chỉ số của hai số 
sao cho tổng của chúng bằng target. Bạn có thể giả định rằng mỗi đầu vào sẽ có 
đúng một giải pháp và bạn không thể sử dụng cùng một phần tử hai lần.

Ví dụ:
Đầu vào: nums = [2, 7, 11, 15], target = 9
Đầu ra: [0, 1]
Giải thích: Vì nums[0] + nums[1] == 9, chúng ta trả về [0, 1].

Ràng buộc:
- 2 <= nums.length <= 10^4
- -10^9 <= nums[i] <= 10^9
- -10^9 <= target <= 10^9
- Chỉ có một giải pháp hợp lệ tồn tại.
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from typing import List
from utils.leetcode_utils import timing_decorator


class Solution:
    """
    Lớp giải pháp cho bài toán Two Sum
    """
    
    @timing_decorator
    def two_sum_brute_force(self, nums: List[int], target: int) -> List[int]:
        """
        Giải pháp vét cạn - Độ phức tạp thời gian O(n²)
        
        Tham số:
            nums: Mảng đầu vào
            target: Tổng mục tiêu
            
        Trả về:
            Danh sách hai chỉ số có tổng bằng target
        """
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []
    
    @timing_decorator
    def two_sum_hashmap(self, nums: List[int], target: int) -> List[int]:
        """
        Giải pháp sử dụng hash map - Độ phức tạp thời gian O(n)
        
        Tham số:
            nums: Mảng đầu vào
            target: Tổng mục tiêu
            
        Trả về:
            Danh sách hai chỉ số có tổng bằng target
        """
        num_map = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_map:
                return [num_map[complement], i]
            num_map[num] = i
        return []
    
    def solve(self, nums: List[int], target: int) -> List[int]:
        """
        Phương thức giải chính - sử dụng phương pháp hash map tối ưu
        
        Tham số:
            nums: Mảng đầu vào
            target: Tổng mục tiêu
            
        Trả về:
            Danh sách hai chỉ số có tổng bằng target
        """
        return self.two_sum_hashmap(nums, target)


def main():
    """Hàm chính để chạy các ví dụ"""
    solution = Solution()
    
    # Các trường hợp test
    test_cases = [
        ([2, 7, 11, 15], 9, [0, 1]),
        ([3, 2, 4], 6, [1, 2]),
        ([3, 3], 6, [0, 1]),
        ([1, 5, 8, 10, 13], 18, [2, 3]),  # Sửa từ [2, 4] thành [2, 3]
        ([0, 4, 3, 0], 0, [0, 3])
    ]
    
    print("Kiểm tra giải pháp Two Sum:")
    print("=" * 50)
    
    for i, (nums, target, expected) in enumerate(test_cases, 1):
        print(f"Trường hợp test {i}:")
        print(f"Đầu vào: nums = {nums}, target = {target}")
        print(f"Kết quả mong đợi: {expected}")
        
        result = solution.solve(nums, target)
        print(f"Kết quả: {result}")
        print(f"Đúng: {result == expected}")
        print("-" * 30)
    
    print("\nSo sánh hiệu suất:")
    print("=" * 50)
    
    # Test hiệu suất với mảng lớn
    large_nums = list(range(10000))
    large_target = 19998
    
    print("Kiểm tra với mảng lớn (10,000 phần tử):")
    result1 = solution.two_sum_brute_force(large_nums, large_target)
    result2 = solution.two_sum_hashmap(large_nums, large_target)
    
    print(f"Kết quả vét cạn: {result1}")
    print(f"Kết quả hash map: {result2}")


if __name__ == "__main__":
    main() 