"""
Các trường hợp test cho bài toán Longest Substring Without Repeating Characters
"""
import pytest
import sys
import os

# Thêm thư mục cha vào đường dẫn để có thể import giải pháp
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from solutions.medium.longest_substring import Solution


class TestLongestSubstring:
    """Lớp test cho bài toán Longest Substring Without Repeating Characters"""
    
    def setup_method(self):
        """Phương thức setup được gọi trước mỗi test"""
        self.solution = Solution()
    
    def test_basic_case(self):
        """Test trường hợp cơ bản"""
        s = "abcabcbb"
        expected = 3
        result = self.solution.solve(s)
        assert result == expected
    
    def test_all_same_characters(self):
        """Test trường hợp tất cả ký tự giống nhau"""
        s = "bbbbb"
        expected = 1
        result = self.solution.solve(s)
        assert result == expected
    
    def test_no_repeating_characters(self):
        """Test trường hợp không có ký tự lặp lại"""
        s = "abc"
        expected = 3
        result = self.solution.solve(s)
        assert result == expected
    
    def test_empty_string(self):
        """Test trường hợp chuỗi rỗng"""
        s = ""
        expected = 0
        result = self.solution.solve(s)
        assert result == expected
    
    def test_single_character(self):
        """Test trường hợp một ký tự"""
        s = "a"
        expected = 1
        result = self.solution.solve(s)
        assert result == expected
    
    def test_two_characters(self):
        """Test trường hợp hai ký tự"""
        s = "ab"
        expected = 2
        result = self.solution.solve(s)
        assert result == expected
    
    def test_complex_case(self):
        """Test trường hợp phức tạp"""
        s = "dvdf"
        expected = 3
        result = self.solution.solve(s)
        assert result == expected
    
    def test_another_complex_case(self):
        """Test trường hợp phức tạp khác"""
        s = "anviaj"
        expected = 5
        result = self.solution.solve(s)
        assert result == expected
    
    def test_brute_force_solution(self):
        """Test giải pháp vét cạn"""
        s = "abcabcbb"
        expected = 3
        result = self.solution.length_of_longest_substring_brute_force(s)
        assert result == expected
    
    def test_sliding_window_solution(self):
        """Test giải pháp sliding window"""
        s = "abcabcbb"
        expected = 3
        result = self.solution.length_of_longest_substring_sliding_window(s)
        assert result == expected
    
    def test_performance_comparison(self):
        """Test so sánh hiệu suất giữa hai phương pháp"""
        # Tạo chuỗi dài để test hiệu suất
        s = "abcdefghijklmnopqrstuvwxyz" * 100
        
        # Cả hai giải pháp phải trả về cùng kết quả
        result1 = self.solution.length_of_longest_substring_brute_force(s)
        result2 = self.solution.length_of_longest_substring_sliding_window(s)
        
        assert result1 == result2
        assert result1 == 26  # Độ dài bảng chữ cái tiếng Anh


if __name__ == "__main__":
    # Chạy test với pytest
    pytest.main([__file__, "-v"]) 