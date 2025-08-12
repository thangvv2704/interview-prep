"""
Các hàm tiện ích cho các bài toán LeetCode
"""
from typing import List, Optional, Union
import time
import functools


def timing_decorator(func):
    """Decorator để đo thời gian thực thi của một hàm"""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Hàm {func.__name__} mất {end_time - start_time:.6f} giây")
        return result
    return wrapper


def create_linked_list(values: List[int]) -> Optional['ListNode']:
    """Tạo một linked list từ danh sách các giá trị"""
    if not values:
        return None
    
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    
    return head


def linked_list_to_list(head: Optional['ListNode']) -> List[int]:
    """Chuyển đổi linked list thành danh sách các giá trị"""
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result


def create_binary_tree(values: List[Optional[int]], index: int = 0) -> Optional['TreeNode']:
    """Tạo một cây nhị phân từ danh sách các giá trị (theo thứ tự level-order)"""
    if index >= len(values) or values[index] is None:
        return None
    
    root = TreeNode(values[index])
    root.left = create_binary_tree(values, 2 * index + 1)
    root.right = create_binary_tree(values, 2 * index + 2)
    
    return root


def binary_tree_to_list(root: Optional['TreeNode']) -> List[Optional[int]]:
    """Chuyển đổi cây nhị phân thành danh sách các giá trị (theo thứ tự level-order)"""
    if not root:
        return []
    
    result = []
    queue = [root]
    
    while queue:
        node = queue.pop(0)
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    
    # Loại bỏ các giá trị None ở cuối
    while result and result[-1] is None:
        result.pop()
    
    return result


def print_matrix(matrix: List[List[Union[int, str]]]) -> None:
    """In đẹp một ma trận 2D"""
    for row in matrix:
        print(f"[{', '.join(map(str, row))}]")


def print_tree(root: Optional['TreeNode'], level: int = 0) -> None:
    """In đẹp một cây nhị phân"""
    if root is None:
        return
    
    print_tree(root.right, level + 1)
    print("  " * level + str(root.val))
    print_tree(root.left, level + 1)


# Các cấu trúc dữ liệu thường dùng trong bài toán LeetCode
class ListNode:
    """Lớp đại diện cho một node trong linked list"""
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    def __repr__(self):
        return f"ListNode({self.val})"


class TreeNode:
    """Lớp đại diện cho một node trong cây nhị phân"""
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
    def __repr__(self):
        return f"TreeNode({self.val})"


class Node:
    """Lớp đại diện cho một node trong đồ thị"""
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
    
    def __repr__(self):
        return f"Node({self.val})" 