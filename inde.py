import os
# type() yu isinstance()区别    type()不会认为子类是一种父类类型。 isinstance()会认为子类是一种父类类型。


print  (__name__ )

def  demohanshu():
    print("测试函数成功")   

def test(parameter_list):
    """
    docstring
    """
    print(parameter_list)

if __name__ == "__main__":
    demohanshu()
    test("小李")