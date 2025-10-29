# 在此文件中实现 isOdd 函数

def isOdd(value):
    """
    判断输入是否为奇整数    
    参数:
    value - 任意类型的输入值    
    返回:
    bool - 如果是整数且为奇数返回 True，否则返回 False
    """
    # 学生实现代码区域
    # 提示：首先检查类型是否为整数，然后检查奇偶性
    if type(value) is not int:
            return False
        
    # 检查是否为奇数（使用位运算，效率高且正确处理负数）
    return value % 2 != 0
