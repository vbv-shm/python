print("hello".__iter__().__next__())
print(dir("hello".__iter__()))
print("hello".__iter__())

print(['a','b','c'].__getitem__(2))
print(['a','b','c'].__iter__().__next__())
