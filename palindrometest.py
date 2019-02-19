word = input("Write a word:")
a = len(word)
error = 0
for i in range(a//2):
if word[i] != word[-1 - i]:
error = 1
break

if error == 1:
print("It's not a palindrome")
else:
print("It's a palindrome")
print()
