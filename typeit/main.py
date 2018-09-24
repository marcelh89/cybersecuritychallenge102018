import hashlib

from typeit.utils import readFileIntoList

"""
fixPassword = "\x93\x39\x02\x94\x83\x02\x82\xf3\x23\xf8\xd3\x13"
fixPasswordAsText = ''.join('%02x' % ord(c) for c in fixPassword) #only for tests - not used in calculation!!
print("fixPassword", fixPassword)
print("fixPasswordAsText", fixPasswordAsText)
"""

possiblePasswords = readFileIntoList("possiblepasswords")



print()


