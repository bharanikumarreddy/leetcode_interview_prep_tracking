list1 = [1,0,1,1,0,1]
# left = 0
# most_consecutive_ones_count = 0
# current_count = 0
# for num in list1:
#     if num == 1:
#         current_count += 1
#         most_consecutive_ones_count = max(most_consecutive_ones_count, current_count)
#     else:
#         current_count = 0

# print(most_consecutive_ones_count)



left=0
zeroes_count=0
max_lenght=0
k=2

for right in range(len(list1)):
    if list1[right] == 0:
        zeroes_count +=1
    
    while zeroes_count < k:
        if list1[left] == 0:
            zeroes_count -=1
        left +=1
    max_lenght = max(max_lenght,left-right+1)
print(max_lenght)
        