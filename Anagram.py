#Anagram

s1 = input()
s2 = input()

s1 = s1.replace(" ","").lower()
s2 = s2.replace(" ","").lower()
s1 = ' '.join(ch for ch in s1 if ch.isalpha())
s2 = ' '.join(ch for ch in s2 if ch.isalpha())
if len(s1)==0 or len(s2)==0:
    print("Not Tom Riddles Anagram")
elif len(s1)==1 or len(s2)==1:
    print("Not Tom Riddles Anagram")
elif (len(set(s1)) ==1 or  len(set(s2))==1):
    print("Not Tom Riddles Anagram")
elif len(s1)==len(s2):
    if sorted(s1)==sorted(s2):
        print("Anagram")
    else:
        print("Not Anagram")
else:
    pritn("Not Anagram")

