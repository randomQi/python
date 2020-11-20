import os
# type() yu isinstance()区别    type()不会认为子类是一种父类类型。 isinstance()会认为子类是一种父类类型。


print  (__name__ )

def  demohanshu():
    print("测试函数成功")   
# 函数的使用
def test(parameter_list):
    """
    docstring
    """
    print(parameter_list)
# lambda表达式的使用
sum = lambda a,b: a + b



#python中l类的定义以及使用
class Student():
    name = ""
    age = 0
    def funcname(self, name,age):
        """
        docstring
        """
        return age

if __name__ == "__main__":
    # 实例化Student
    student = Student()
    s= student.funcname("测试",56)
    print(s)