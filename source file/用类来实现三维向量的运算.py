'''
设计一个三维向量类，并实现向量的加法、减法以及向量与标量的乘法和除法运算

'''

class Vector3:
    # 构造方法，初始化，定义向量坐标
    def __init__(self, x, y, z):
        self.__x = x
        self.__y = y
        self.__z = z

    # 与两一个向量相加，对应分量相加，返回新向量
    def __add__(self, anotherPoint):
        x = self.__x + anotherPoint.__x
        y = self.__y + anotherPoint.__y
        z = self.__z + anotherPoint.__z
        return Vector3(x, y, z)

    # 减去另一个向量，对应分量相减，返回新向量
    def __sub__(self, anotherPoint):
        x = self.__x - anotherPoint.__x
        y = self.__y - anotherPoint.__y
        z = self.__z - anotherPoint.__z
        return Vector3(x, y, z)

    # 向量与一个数字相乘，各分量乘以同一个数字，返回新向量
    def __mul__(self, n):
        x, y, z = self.__x*n, self.__y*n, self.__z*n
        return Vector3(x, y, z)

    # 向量除以一个数字，各分量除以同一个数字，返回新向量
    def __truediv__(self, n):
        x, y, z = self.__x/n, self.__y/n, self.__z/n
        return Vector3(x, y, z)

    # 查看向量长度，所有分量平方和的平方根,用属性来实现
    @property
    def length(self):
        return (self.__x**2 + self.__y**2 + self.__z**2)**0.5

    def __str__(self):
        return 'Vector3({},{},{})'.format(self.__x,
                                             self.__y,
                                             self.__z)
    __repr__=__str__
   
    
# 用法演示
v1 = Vector3(3, 4, 5)
v2 = Vector3(5, 6, 7)
print(v1+v2)
print(v1-v2)
print(v1*3)
print(v2/2)
print(v1.length)#将方法转换为属性后，可以直接通过方法名访问方法，不需要添加一对小括号()，让代码更简洁。
