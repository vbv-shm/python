print(type.__class__)
object
class UselessCLass():
    def __init__(self) -> None:
        self.name='vaibhav'
    def __str__(self) -> str:
        return "UselessClass"
class AnotherUselessClass(UselessCLass):
    pass

x=UselessCLass()
print(x.__str__())

y=AnotherUselessClass()
print(y.__class__.__bases__)

# print(object.__new__(int))
print(dir(object))
print(dir(type))