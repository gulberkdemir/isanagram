*** Variables ***
${word1}    angel
${word2}    glean


*** Settings ***
Library  C:/Python37Projects/isanagram/Anagram.py


*** Test Cases ***
Is Anagram
    isAnagram    angel    glean