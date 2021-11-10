# Strings and bytes: str, bytes, bytearray
import sys

print(sys.getdefaultencoding())

print(ord('a'))
print(chr(97))

s = "Hello"
print(s.encode('ascii'))
print(s.encode('utf8'))
print(s.encode('utf16'))
