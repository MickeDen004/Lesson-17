# Recursion
# Input
# Class Exception

# descendants
# def classtree(cls, indent = 0):
#     print('.'*indent, cls.__name__)
#     for subcls in cls.__subclasses__():
#         classtree(subcls, indent + 3)
#
# classtree(BaseException)
# print(type(BaseException))

def recursion_base_errors(cls):
    if repr(cls) == "<class 'object'>":
        return
    temp = cls.__base__
    print(temp)
    recursion_base_errors(temp)

print(recursion_base_errors(BaseException))

