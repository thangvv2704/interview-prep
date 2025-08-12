#!/usr/bin/env python3
"""
Script để chạy test cho các giải pháp LeetCode
Cách dùng: python run_tests.py [tùy chọn]
"""

import argparse
import os
import subprocess
import sys
from pathlib import Path


def run_pytest(test_path=None, verbose=False, coverage=False, html_report=False):
    """
    Chạy pytest với các tùy chọn được chỉ định
    
    Tham số:
        test_path: File hoặc thư mục test cụ thể để chạy
        verbose: Có chạy ở chế độ verbose không
        coverage: Có tạo báo cáo coverage không
        html_report: Có tạo báo cáo HTML không
    """
    cmd = ["python", "-m", "pytest"]
    
    if test_path:
        cmd.append(test_path)
    else:
        cmd.append("tests/")
    
    if verbose:
        cmd.append("-v")
    
    if coverage:
        cmd.append("--cov=solutions")
        cmd.append("--cov-report=term-missing")
    
    if html_report:
        cmd.append("--cov=solutions")
        cmd.append("--cov-report=html")
        cmd.append("--html=test_report.html")
    
    print(f"Đang chạy lệnh: {' '.join(cmd)}")
    print("-" * 50)
    
    try:
        result = subprocess.run(cmd, check=True)
        print("\n✅ Tất cả test đều thành công!")
        return True
    except subprocess.CalledProcessError as e:
        print(f"\n❌ Test thất bại với mã thoát {e.returncode}")
        return False


def list_available_tests():
    """Liệt kê tất cả các file test có sẵn"""
    test_dir = Path("tests")
    if not test_dir.exists():
        print("Không tìm thấy thư mục tests!")
        return
    
    test_files = list(test_dir.glob("test_*.py"))
    
    if not test_files:
        print("Không tìm thấy file test nào!")
        return
    
    print("Các file test có sẵn:")
    print("-" * 30)
    
    for test_file in sorted(test_files):
        # Trích xuất tên bài toán từ tên file test
        problem_name = test_file.stem.replace("test_", "").replace("_", " ").title()
        print(f"📝 {test_file.name} - {problem_name}")
    
    print(f"\nTổng cộng: {len(test_files)} file test")


def run_specific_solution(solution_path):
    """
    Chạy một file giải pháp cụ thể
    
    Tham số:
        solution_path: Đường dẫn đến file giải pháp
    """
    if not os.path.exists(solution_path):
        print(f"❌ Không tìm thấy file giải pháp: {solution_path}")
        return False
    
    print(f"Đang chạy giải pháp: {solution_path}")
    print("-" * 50)
    
    try:
        result = subprocess.run([sys.executable, solution_path], check=True)
        print("\n✅ Giải pháp chạy thành công!")
        return True
    except subprocess.CalledProcessError as e:
        print(f"\n❌ Giải pháp thất bại với mã thoát {e.returncode}")
        return False


def main():
    """Hàm chính"""
    parser = argparse.ArgumentParser(description="Chạy test cho các giải pháp LeetCode")
    parser.add_argument("--test", help="File hoặc thư mục test cụ thể để chạy")
    parser.add_argument("--solution", help="Chạy một file giải pháp cụ thể")
    parser.add_argument("--verbose", "-v", action="store_true", help="Đầu ra chi tiết")
    parser.add_argument("--coverage", action="store_true", help="Tạo báo cáo coverage")
    parser.add_argument("--html", action="store_true", help="Tạo báo cáo test HTML")
    parser.add_argument("--list", action="store_true", help="Liệt kê các test có sẵn")
    
    args = parser.parse_args()
    
    if args.list:
        list_available_tests()
        return
    
    if args.solution:
        run_specific_solution(args.solution)
        return
    
    # Chạy test
    success = run_pytest(
        test_path=args.test,
        verbose=args.verbose,
        coverage=args.coverage,
        html_report=args.html
    )
    
    if not success:
        sys.exit(1)


if __name__ == "__main__":
    main() 