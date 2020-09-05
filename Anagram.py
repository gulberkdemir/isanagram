import sys
import os
import string
import time
import argparse
class Anagram:

    def __init__(self):
        pass

    @staticmethod
    def isAnagram(s1, s2):
        s1 = sorted(s1)
        s2 = sorted(s2)
        if s1 == s2:
            print("This is an anagram")
        else:
            print("This is not an anagram")





