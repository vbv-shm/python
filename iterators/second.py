# sequence_iter.py

class SequenceIterator:
    def __init__(self, sequence):
        self._sequence = sequence
        self._index = 0

    # def __iter__(self):
    #     return self

    def __next__(self):
        if self._index < len(self._sequence):
            item = self._sequence[self._index]
            self._index += 1
            return item
        else:
            raise StopIteration
        

sequence = SequenceIterator([1, 2, 3, 4])

# Get an iterator over the data
print(sequence)
# iterator = sequence.__iter__()
# print(iterator)
while True:
    try:
        # Retrieve the next item
        item = sequence.__next__()
    except StopIteration:
        break
    else:
        # The loop's code block goes here...
        print(item)