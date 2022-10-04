# Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn. Go to the editor
# Sample value of n is 5
# Expected Result : 615


n = int(input("Enter the number -> "))
print(n+int(str(n)*2)+int(str(n)*3))