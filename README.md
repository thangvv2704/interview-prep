# LeetCode Interview Prep

Repo này chứa các giải pháp cho các bài toán LeetCode được viết bằng Python, với cấu trúc gọn gàng và dễ sử dụng.

## Cấu trúc thư mục

```
leetcode-prep/
├── solutions/           # Thư mục chứa các giải pháp
│   ├── easy/           # Bài toán dễ
│   ├── medium/         # Bài toán trung bình
│   └── hard/           # Bài toán khó
├── templates/           # Template cho các loại bài toán
├── tests/              # Test cases với pytest
├── utils/              # Utility functions
├── requirements.txt     # Dependencies
└── run_tests.py        # Script chạy test
```

## Cài đặt

1. Clone repo này
2. Cài đặt dependencies:
```bash
pip install -r requirements.txt
```

## Cách sử dụng

### 1. Tạo bài giải mới

Sử dụng template có sẵn trong thư mục `templates/`:

```bash
python create_solution.py --problem "Two Sum" --difficulty easy
```

### 2. Chạy test

```bash
# Chạy tất cả test
pytest

# Chạy test cho một bài cụ thể
pytest tests/test_two_sum.py

# Chạy test với coverage
pytest --cov=solutions
```

### 3. Chạy bài giải

```bash
python solutions/easy/two_sum.py
```

## Template sẵn có

- `array_problem.py` - Template cho bài toán về mảng
- `string_problem.py` - Template cho bài toán về chuỗi
- `tree_problem.py` - Template cho bài toán về cây
- `graph_problem.py` - Template cho bài toán về đồ thị

## Ví dụ bài mẫu

- `two_sum.py` - Bài toán Two Sum (Easy)
- `add_two_numbers.py` - Bài toán Add Two Numbers (Medium)
- `longest_substring.py` - Bài toán Longest Substring Without Repeating Characters (Medium)

## Quy ước đặt tên

- Tên file: `snake_case.py` (ví dụ: `two_sum.py`)
- Tên class: `PascalCase` (ví dụ: `TwoSum`)
- Tên function: `snake_case` (ví dụ: `two_sum_solution`)

## Chạy nhanh

```bash
# Cài đặt dependencies
pip install -r requirements.txt

# Chạy test cho bài mẫu
pytest tests/test_two_sum.py -v

# Chạy bài giải
python solutions/easy/two_sum.py
```
