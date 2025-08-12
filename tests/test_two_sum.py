"""
Các trường hợp test cho bài toán Two Sum
"""
import pytest
import sys
import os

# Thêm thư mục cha vào đường dẫn để có thể import giải pháp
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from solutions.easy.two_sum import Solution


class TestTwoSum:
    """Lớp test cho bài toán Two Sum"""
    
    def setup_method(self):
        """Phương thức setup được gọi trước mỗi test"""
        self.solution = Solution()
    
    def test_two_sum_basic(self):
        """Test trường hợp cơ bản"""
        nums = [2, 7, 11, 15]
        target = 9
        expected = [0, 1]
        result = self.solution.solve(nums, target)
        assert result == expected
    
    def test_two_sum_duplicate_numbers(self):
        """Test trường hợp có số trùng lặp"""
        nums = [3, 3]
        target = 6
        expected = [0, 1]
        result = self.solution.solve(nums, target)
        assert result == expected
    
    def test_two_sum_negative_numbers(self):
        """Test trường hợp có số âm"""
        nums = [-1, -2, -3, -4, -5]
        target = -8
        expected = [2, 4]
        result = self.solution.solve(nums, target)
        assert result == expected
    
    def test_two_sum_large_numbers(self):
        """Test trường hợp có số lớn"""
        nums = [1000000, 2000000, 3000000, 4000000]
        target = 5000000
        expected = [1, 3]
        result = self.solution.solve(nums, target)
        assert result == expected
    
    def test_two_sum_brute_force(self):
        """Test giải pháp vét cạn"""
        nums = [2, 7, 11, 15]
        target = 9
        expected = [0, 1]
        result = self.solution.two_sum_brute_force(nums, target)
        assert result == expected
    
    def test_two_sum_hashmap(self):
        """Test giải pháp hash map"""
        nums = [2, 7, 11, 15]
        target = 9
        expected = [0, 1]
        result = self.solution.two_sum_hashmap(nums, target)
        assert result == expected
    
    def test_two_sum_edge_cases(self):
        """Test các trường hợp biên"""
        # Test với mảng có độ dài tối thiểu
        nums = [1, 2]
        target = 3
        expected = [0, 1]
        result = self.solution.solve(nums, target)
        assert result == expected
        
        # Test với số 0
        nums = [0, 4, 3, 0]
        target = 0
        expected = [0, 3]
        result = self.solution.solve(nums, target)
        assert result == expected
    
    def test_two_sum_performance(self):
        """Test hiệu suất với mảng lớn"""
        # Tạo mảng lớn
        nums = list(range(1000))
        target = 1998  # Tổng của chỉ số 999 và 999
        
        # Cả hai giải pháp phải trả về cùng kết quả
        result1 = self.solution.two_sum_brute_force(nums, target)
        result2 = self.solution.two_sum_hashmap(nums, target)
        
        assert result1 == result2
        assert len(result1) == 2
        assert nums[result1[0]] + nums[result1[1]] == target


if __name__ == "__main__":
    # Chạy test với pytest
    pytest.main([__file__, "-v"]) 