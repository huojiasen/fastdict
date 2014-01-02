#!/usr/bin/env python

import fastdict
import sys
import struct

f_dict = fastdict.FastCompressIntDict(8)
f_dict.set(123, 6794572984750169060, 0)
print f_dict.size()

print f_dict.get(123)
print f_dict.get(123)[0]
print f_dict.get(123)[0].first
print f_dict.get(123)[0].second
 
f_dict.append(123, 678, 1)
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

f_dict.set(456, 789, 2)

print f_dict.keys()

for key in f_dict.keys():
    print "key: " + str(key)

f_dict.set_keydimensions([1, 2, 3])

fastdict.save_compress_int("test.dict", f_dict)

f_dict = fastdict.FastCompressIntDict(8)

print f_dict.size()

fastdict.load_compress_int("test.dict", f_dict)

print f_dict.size()
 
f_dict_merge_source = fastdict.FastCompressIntDict(8)

f_dict_merge_source.set(789, 123, 3)

print f_dict_merge_source.size()
 
for key in f_dict_merge_source.keys():
    print "key: " + str(key)

f_dict.merge(f_dict_merge_source)

print "merged: "
print f_dict.size()

f_dict_merge_source.clear()

print f_dict_merge_source.size()
 
for ele in f_dict.get(789):
    print ele
    print ele.first
    print ele.second
 
for ele in f_dict.get(123):
    print ele
    print ele.first
    print ele.second

key_dimensions = []

print f_dict.get_keydimensions(key_dimensions)

print key_dimensions

print f_dict.exist(123)
print f_dict.exist(12345)

for ele in f_dict.get(12345):
    print ele
    print ele.first
    print ele.second

f_dict.go_index()

cols = f_dict.get_cols(123)
col_count = 0
for column in cols.first:
    print "col: " + str(col_count)
    for bit_count in column:
        print bit_count
    col_count += 1

for image_id in cols.second:
    print image_id


print f_dict.size()
 
fastdict.save_compress_int("test.dict", f_dict)

f_dict = fastdict.FastCompressIntDict(8)
print f_dict.size()

cols = f_dict.get_cols(123)
col_count = 0
for column in cols.first:
    print "col: " + str(col_count)
    for bit_count in column:
        print bit_count
    col_count += 1

for image_id in cols.second:
    print image_id

fastdict.load_compress_int("test.dict", f_dict)

cols = f_dict.get_cols(123)
col_count = 0
for column in cols.first:
    print "col: " + str(col_count)
    for bit_count in column:
        print bit_count
    col_count += 1

for image_id in cols.second:
    print image_id

# get_binary_codes should be called before runtime dict initialization
binary_codes = f_dict.get_binary_codes(123)
for code in binary_codes.first:
    print "code: " + str(code)

# initialze runtime dict
print "init runtime dict..."
f_dict.init_runtime_dict()
print "done."

print "buffer:"
cols_buffer = f_dict.get_cols_as_buffer(123)
print len(cols_buffer)
print cols_buffer
index = 0
for buffers in cols_buffer:
    print index
    for i in range(0, len(buffers) / 8):
        data = ''
        for j in range(i * 8, i * 8 + 8):
            data = data + buffers[j]
        print data
        print struct.unpack('Q', data)
    index += 1

 