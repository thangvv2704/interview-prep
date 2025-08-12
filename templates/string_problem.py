"""
Template cho bài toán về chuỗi
Tên bài: [PROBLEM_NAME]
Độ khó: [EASY/MEDIUM/HARD]
URL: [LEETCODE_URL]

Mô tả:
[PROBLEM_DESCRIPTION]

Ví dụ:
[EXAMPLE_INPUT_OUTPUT]

Ràng buộc:
[CONSTRAINTS]
"""

from typing import List, Optional
from utils.leetcode_utils import timing_decorator


class Solution:
    """
    Lớp giải pháp cho bài toán [PROBLEM_NAME]
    """
    
    @timing_decorator
    def solve(self, s: str) -> str:
        """
        Phương thức giải chính
        
        Tham số:
            s: Chuỗi đầu vào
            
        Trả về:
            Kết quả giải pháp
        """
        # TODO: Viết giải pháp của bạn ở đây
        pass
    
    def solve_optimized(self, s: str) -> str:
        """
        Phương thức giải tối ưu
        
        Tham số:
            s: Chuỗi đầu vào
            
        Trả về:
            Kết quả giải pháp
        """
        # TODO: Viết giải pháp tối ưu ở đây
        pass


def main():
    """Hàm chính để chạy các ví dụ"""
    solution = Solution()
    
    # Các trường hợp test
    test_cases = [
        # Thêm các trường hợp test của bạn ở đây
        # Ví dụ: ("hello", "olleh"),
    ]
    
    print("Kiểm tra giải pháp [PROBLEM_NAME]:")
    print("=" * 50)
    
    for i, (s, expected) in enumerate(test_cases, 1):
        print(f"Trường hợp test {i}:")
        print(f"Đầu vào: s = \"{s}\"")
        print(f"Kết quả mong đợi: \"{expected}\"")
        
        result = solution.solve(s)
        print(f"Kết quả: \"{result}\"")
        print(f"Đúng: {result == expected}")
        print("-" * 30)


if __name__ == "__main__":
    main() 