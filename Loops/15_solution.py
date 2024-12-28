# # reverse a number
# num = "6789"
# rvr_num = ""
# for i in num:
#     rvr_num = i + rvr_num

# print(rvr_num)


num = 7899  
rvr_num = 0  


while num > 0:
    digit = num % 10  
    rvr_num = rvr_num * 10 + digit  
    num = num // 10 
    
print(rvr_num)


