#!/usr/bin/env python3
"""
Script để tạo file giải pháp LeetCode mới từ template
Cách dùng: python create_solution.py --problem "Tên Bài Toán" --difficulty easy
"""

import argparse
import os
import re
from datetime import datetime
from pathlib import Path


def create_solution_file(problem_name: str, difficulty: str, template_type: str = "array"):
    """
    Tạo file giải pháp mới từ template
    
    Tham số:
        problem_name: Tên bài toán
        difficulty: Mức độ khó (easy, medium, hard)
        template_type: Loại template để sử dụng
    """
    # Chuyển đổi tên bài toán thành snake_case cho tên file
    filename = re.sub(r'[^a-zA-Z0-9\s]', '', problem_name.lower())
    filename = re.sub(r'\s+', '_', filename)
    filename = f"{filename}.py"
    
    # Xác định đường dẫn template
    template_path = f"templates/{template_type}_problem.py"
    
    if not os.path.exists(template_path):
        print(f"Không tìm thấy template {template_path}. Sử dụng template array.")
        template_path = "templates/array_problem.py"
    
    # Đọc template
    with open(template_path, 'r', encoding='utf-8') as f:
        template_content = f.read()
    
    # Thay thế các placeholder
    content = template_content.replace("[PROBLEM_NAME]", problem_name)
    content = content.replace("[EASY/MEDIUM/HARD]", difficulty.upper())
    content = content.replace("[LEETCODE_URL]", f"https://leetcode.com/problems/{filename.replace('.py', '')}/")
    content = content.replace("[PROBLEM_DESCRIPTION]", f"Mô tả cho {problem_name}")
    content = content.replace("[EXAMPLE_INPUT_OUTPUT]", "Thêm ví dụ đầu vào/đầu ra ở đây")
    content = content.replace("[CONSTRAINTS]", "Thêm ràng buộc ở đây")
    
    # Tạo thư mục giải pháp nếu chưa tồn tại
    solution_dir = f"solutions/{difficulty.lower()}"
    os.makedirs(solution_dir, exist_ok=True)
    
    # Ghi file giải pháp
    solution_path = os.path.join(solution_dir, filename)
    with open(solution_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"Đã tạo file giải pháp: {solution_path}")
    
    # Tạo file test
    create_test_file(problem_name, difficulty, filename)
    
    # Cập nhật README
    update_readme(problem_name, difficulty, filename)


def create_test_file(problem_name: str, difficulty: str, filename: str):
    """Tạo file test cho giải pháp"""
    test_filename = f"test_{filename}"
    test_path = os.path.join("tests", test_filename)
    
    # Template test cơ bản
    test_content = f'''"""
Các trường hợp test cho {problem_name}
"""
import pytest
import sys
import os

# Thêm thư mục cha vào đường dẫn để có thể import giải pháp
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from solutions.{difficulty.lower()}.{filename.replace('.py', '')} import Solution


class Test{problem_name.replace(' ', '')}:
    """Lớp test cho {problem_name}"""
    
    def setup_method(self):
        """Phương thức setup được gọi trước mỗi test"""
        self.solution = Solution()
    
    def test_basic_case(self):
        """Test trường hợp cơ bản"""
        # TODO: Thêm các trường hợp test của bạn ở đây
        pass
    
    def test_edge_cases(self):
        """Test các trường hợp biên"""
        # TODO: Thêm các test trường hợp biên ở đây
        pass


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
'''
    
    with open(test_path, 'w', encoding='utf-8') as f:
        f.write(test_content)
    
    print(f"Đã tạo file test: {test_path}")


def update_readme(problem_name: str, difficulty: str, filename: str):
    """Cập nhật README với bài toán mới"""
    readme_path = "README.md"
    
    if not os.path.exists(readme_path):
        return
    
    with open(readme_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Tìm phần để thêm bài toán mới
    if "## Ví dụ bài mẫu" in content:
        # Thêm bài toán mới vào danh sách
        new_entry = f"- `{filename}` - Bài toán {problem_name} ({difficulty.capitalize()})"
        
        # Tìm cuối phần ví dụ
        examples_start = content.find("## Ví dụ bài mẫu")
        examples_end = content.find("##", examples_start + 1)
        
        if examples_end == -1:
            examples_end = len(content)
        
        examples_section = content[examples_start:examples_end]
        
        # Thêm entry mới trước cuối phần
        if "## Quy ước đặt tên" in examples_section:
            # Chèn trước phần tiếp theo
            insert_pos = examples_section.find("## Quy ước đặt tên")
            new_section = examples_section[:insert_pos] + new_entry + "\n\n" + examples_section[insert_pos:]
        else:
            # Thêm vào cuối phần ví dụ
            new_section = examples_section.rstrip() + "\n" + new_entry + "\n"
        
        # Thay thế phần
        content = content[:examples_start] + new_section + content[examples_end:]
        
        with open(readme_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"Đã cập nhật README.md với bài toán mới")


def main():
    """Hàm chính"""
    parser = argparse.ArgumentParser(description="Tạo file giải pháp LeetCode mới")
    parser.add_argument("--problem", required=True, help="Tên bài toán")
    parser.add_argument("--difficulty", required=True, choices=["easy", "medium", "hard"], 
                       help="Mức độ khó")
    parser.add_argument("--template", default="array", 
                       choices=["array", "string", "tree", "graph"],
                       help="Loại template để sử dụng")
    
    args = parser.parse_args()
    
    print(f"Đang tạo giải pháp cho: {args.problem}")
    print(f"Mức độ khó: {args.difficulty}")
    print(f"Template: {args.template}")
    print("-" * 50)
    
    create_solution_file(args.problem, args.difficulty, args.template)
    
    print("\nCác bước tiếp theo:")
    print(f"1. Chỉnh sửa file giải pháp: solutions/{args.difficulty.lower()}/{args.problem.lower().replace(' ', '_')}.py")
    print(f"2. Chỉnh sửa file test: tests/test_{args.problem.lower().replace(' ', '_')}.py")
    print("3. Chạy test: pytest tests/")
    print("4. Chạy giải pháp: python solutions/[difficulty]/[filename].py")


if __name__ == "__main__":
    main() 