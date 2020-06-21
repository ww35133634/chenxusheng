s1={'张三','王二麻子','李四','大周','小明'}
s2={'李四','黄忠','刘精','王二麻子'}

# #交集
# print(s1.intersection(s2))
# print(s1&s2)

# #并集
# print(s1.union(s2))
# print(s1|s2)

# #差集
# print(s1.difference(s2))
# print(s1-s2)
# print(s2.difference(s1))
# print(s2-s1)

# #对称差集
# print(s1.symmetric_difference(s2))
# print(s2.symmetric_difference(s1))

s3={'张三1','李四'}
s4={'李四1','张三'}
# print(s3.issubset(s1))
# print(s1.issuperset(s3))
print(s3.isdisjoint(s4))