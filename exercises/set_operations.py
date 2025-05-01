"""
练习: 集合操作

描述：
实现两个学生集合的并集、交集和差集操作。

请补全下面的函数，对两个学生集合进行各种操作。
"""

def student_set_operations(set1, set2, operation):
    """
    对两个学生集合进行操作
    
    参数:
    - set1: 第一个学生集合
    - set2: 第二个学生集合
    - operation: 操作类型 ("union", "intersection", "difference")
    
    返回:
    - 集合操作的结果
    """
    # 请在下方编写代码
    if operation == "union":
        set1 = set1.union(set2)
        set2 = set2.union(set1)
        result = set1.union(set2)
        return result
    elif operation == "intersection":
        #set1 = set1.intersection(set2)
        #set2 = set2.intersection(set1)
        #set1 = set1.difference(set2)
        #set2 = set2.difference(set1)
        result = set1&set2
        return result
    elif operation == "difference":
        #set1 = set1.difference(set2)
        #set2 = set2.difference(set1)
        #set1 = set1.symmetric_difference(set2)
        #set2 = set2.symmetric_difference(set1)
        result = set1-set2
        return result
    else:
        pass
    pass
