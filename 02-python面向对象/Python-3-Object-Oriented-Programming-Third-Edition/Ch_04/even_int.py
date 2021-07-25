class EventOnly(list):
    def append(self, integer):
        if not isinstance(integer, int):
            raise TypeError('Only integer can be add')
        if integer % 2 == 0:
            raise ValueError('Only even numbers can be added')
        super().append(integer)


a = EventOnly()
a.append(3)
# a.append("3")
a.append(2)
