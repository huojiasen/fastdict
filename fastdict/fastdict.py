#!/usr/bin/env python

import fastdict

f_dict = fastdict.FastDict()
f_dict.set(123, 456, 'vec0')
print f_dict.size()

print f_dict.get(123)
print f_dict.get(123)[0]
print f_dict.get(123)[0].first
print f_dict.get(123)[0].second
 
f_dict.append(123, 678, 'vec1')
print f_dict.size()

print f_dict.get(123)
print f_dict.get(123)[0]
print f_dict.get(123)[0].first
print f_dict.get(123)[0].second
print f_dict.get(123)[1]
print f_dict.get(123)[1].first
print f_dict.get(123)[1].second

for ele in f_dict.get(123):
    print ele
    print ele.first
    print ele.second

f_dict.set(456, 789, 'vec2')

print f_dict.keys()

for key in f_dict.keys():
    print "key: " + str(key)


 
