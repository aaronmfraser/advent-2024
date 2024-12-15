
# Pull in the already split list1, sort them
with  open("list_1_raw", "r") as f1:
    list1 = f1.read().split()    
    list1.sort()

# Pull in the already split list 2, sort them
with open("list_2_raw", "r") as f2:
    list2 = f2.read().split()  
    list2.sort()


similarity = []


# Loop through first list, use enumerate to capture the index and value
for x in list1:
    match_count = sum(1 for y in list2 if y == x)
    
    # using abs() to find distances between each pair
    
    if match_count > 0:
        print(f"l1 num: {x} - matches: {match_count}")
        new_num = int(x) * match_count
        
        similarity.append(new_num)


# Check that list is correct length
# Print the sum of all distances
print(f"similarity Score: {sum(similarity)}")