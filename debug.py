# Task 1
# - Index 0: value=1 (odd) -> REMOVE -> list becomes [3, 4, 6, 7, 9, 10]
# - Index 1: value=4 (even) -> SKIP (but we skipped 3)
# - Index 2: value=6 (even) -> SKIP
# - Index 3: value=7 (odd) -> REMOVE -> list becomes [3, 4, 6, 9, 10]
# - Index 4: value=9 (odd) -> REMOVE -> list becomes [3, 4, 6, 10]
# - Index 5: OUT OF BOUNDS -> loop ends
# RESULT: [3, 4, 6, 9, 10] (This is wrong because some odd numbers remain)

# Task 2
# 1. Set breakpoint at the for loop
# 2. Step through each iteration using "Step Over" (F10)
# 3. Watch the record_ids variable after each remove() call
# 4. Observe that indices shift, causing the iterator to skip elements
# 5. Noticed that element at index 1 (value=3, which is odd) was never checked
#    because after removing index 0, the list shifted and index 1 now contained 4
# 6. Confirmed: the loop counter advances but the list is being modified underneath

# TASK 3
# Modifying the original list:
def clean_database(record_ids):
    # Fix 2: Iterate backwards through the list
    # When iterating from end to start, removing elements doesn't affect indices of unprocessed elements
    for i in range(len(record_ids) - 1, -1, -1):
        if record_ids[i] % 2 != 0:
            record_ids.pop(i)
    return record_ids

# Test: [1, 3, 4, 6, 7, 9, 10] → [4, 6, 10] 

# Creating a new list:
def clean_database(record_ids):
    # Fix 1: Use list comprehension to create a new list with only even numbers
    # This avoids modifying the original list during iteration
    return [record_id for record_id in record_ids if record_id % 2 == 0]

# Test: [1, 3, 4, 6, 7, 9, 10] → [4, 6, 10] 




    print(f"Empty list: {test1}")  # Expected: []
    
    