# # to check for palindromes
# txt ="radar"
# rvr_txt=""

# for i in txt:
#     rvr_txt=i + rvr_txt

# if txt == rvr_txt:
#         print("palindrome")
# else:
#         print("not a palindrome")

    
txt = "radar"
length = len(txt)
palindrome = True
for i in range(length//2):
    if txt[i] !=txt[length-i-1]:
        palindrome = False
        break
print(palindrome)



    