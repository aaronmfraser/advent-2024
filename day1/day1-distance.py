
# Pull in the already split list1, sort them
with  open("list_1_raw", "r") as f1:
    list1 = f1.read().split()    
    list1.sort()

# Pull in the already split list 2, sort them
with open("list_2_raw", "r") as f2:
    list2 = f2.read().split()  
    list2.sort()


distances = []

# First make sure the two lists are equal length, proceed only if they are same
if len(list1) == len(list2):
    
    # Loop through first list, use enumerate to capture the index and value
    for idx, x in enumerate(list1):
        
        # convert lines in list to int
        l1=int(x)
        
        # Using index from list1, pull the equivalent number and convert to int
        l2=int(list2[idx])
        
        # using abs() to find distances between each pair
        d1=abs(l1-l2)
        
        # Add this distance to list
        distances.append(d1)

# Check that list is correct length
if len(distances) == 1000:
    # Print the sum of all distances
    print(f"Total Distance: {sum(distances)}")