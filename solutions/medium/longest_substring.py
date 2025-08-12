"""
Bài toán: Longest Substring Without Repeating Characters (Chuỗi con dài nhất không có ký tự lặp lại)
Độ khó: Trung bình
URL: https://leetcode.com/problems/longest-substring-without-repeating-characters/

Mô tả:
Cho một chuỗi s, hãy tìm độ dài của chuỗi con dài nhất không có ký tự lặp lại.

Ví dụ:
Đầu vào: s = "abcabcbb"
Đầu ra: 3
Giải thích: Đáp án là "abc", có độ dài 3.

Ràng buộc:
- 0 <= s.length <= 5 * 10^4
- s chỉ chứa chữ cái tiếng Anh, chữ số, ký hiệu và khoảng trắng.
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from typing import Dict
from utils.leetcode_utils import timing_decorator


class Solution:
    """
    Lớp giải pháp cho bài toán Longest Substring Without Repeating Characters
    """
    
    @timing_decorator
    def length_of_longest_substring_brute_force(self, s: str) -> int:
        """
        Giải pháp vét cạn - Độ phức tạp thời gian O(n³)
        
        Tham số:
            s: Chuỗi đầu vào
            
        Trả về:
            Độ dài của chuỗi con dài nhất không có ký tự lặp lại
        """
        def has_repeating_chars(substring: str) -> bool:
            """Kiểm tra xem chuỗi con có ký tự lặp lại không"""
            char_set = set()
            for char in substring:
                if char in char_set:
                    return True
                char_set.add(char)
            return False
        
        max_length = 0
        n = len(s)
        
        for i in range(n):
            for j in range(i + 1, n + 1):
                substring = s[i:j]
                if not has_repeating_chars(substring):
                    max_length = max(max_length, len(substring))
        
        return max_length
    
    @timing_decorator
    def length_of_longest_substring_sliding_window(self, s: str) -> int:
        """
        Giải pháp sliding window - Độ phức tạp thời gian O(n)
        
        Tham số:
            s: Chuỗi đầu vào
            
        Trả về:
            Độ dài của chuỗi con dài nhất không có ký tự lặp lại
        """
        char_map: Dict[str, int] = {}
        max_length = 0
        start = 0
        
        for end, char in enumerate(s):
            if char in char_map and char_map[char] >= start:
                start = char_map[char] + 1
            char_map[char] = end
            max_length = max(max_length, end - start + 1)
        
        return max_length
    
    def solve(self, s: str) -> int:
        """
        Phương thức giải chính - sử dụng phương pháp sliding window tối ưu
        
        Tham số:
            s: Chuỗi đầu vào
            
        Trả về:
            Độ dài của chuỗi con dài nhất không có ký tự lặp lại
        """
        return self.length_of_longest_substring_sliding_window(s)


def main():
    """Hàm chính để chạy các ví dụ"""
    solution = Solution()
    
    # Các trường hợp test
    test_cases = [
        ("abcabcbb", 3),
        ("bbbbb", 1),
        ("pwwkew", 3),
        ("", 0),
        ("a", 1),
        ("ab", 2),
        ("abc", 3),
        ("dvdf", 3),
        ("anviaj", 5)
    ]
    
    print("Kiểm tra giải pháp Longest Substring Without Repeating Characters:")
    print("=" * 70)
    
    for i, (s, expected) in enumerate(test_cases, 1):
        print(f"Trường hợp test {i}:")
        print(f"Đầu vào: s = \"{s}\"")
        print(f"Kết quả mong đợi: {expected}")
        
        result = solution.solve(s)
        print(f"Kết quả: {result}")
        print(f"Đúng: {result == expected}")
        print("-" * 40)
    
    print("\nSo sánh hiệu suất:")
    print("=" * 50)
    
    # Test hiệu suất với chuỗi dài
    long_string = "abcdefghijklmnopqrstuvwxyz" * 1000
    
    print("Kiểm tra với chuỗi dài (26,000 ký tự):")
    result1 = solution.length_of_longest_substring_brute_force(long_string)
    result2 = solution.length_of_longest_substring_sliding_window(long_string)
    
    print(f"Kết quả vét cạn: {result1}")
    print(f"Kết quả sliding window: {result2}")


if __name__ == "__main__":
    main() 