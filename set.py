s = set()
print(type(s))
s = set({1,2,3})
s.add(4)
s.add(3)
print(s)
s1 = ({1,2,3})
s.intersection(s1)
print(s.intersection(s1))
s2 = ({5})
s.isdisjoint(s2)
print(s.isdisjoint(s2))