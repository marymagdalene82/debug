
# Task 2
"""
1. OBSERVATION:
The logic first skips a number at index 1.

Step-by-step:
Original list: [1, 3, 4, 6, 7, 9, 10]

- Iteration starts:
  record_id = 1 → removed
  List becomes: [3, 4, 6, 7, 9, 10]

- Next iteration moves forward:
  Now pointer goes to index 1
  BUT index 0 now contains 3 (shifted left)

So 3 is skipped and never checked.


2. WHY:
When you remove an element from a list while iterating forward:
- All elements shift one position to the left
- But the loop moves to the next index

This causes the loop to skip the element that shifted into the current position.
The pointer becomes "blind" to the next element.

"""

# TASK 3
# Modifying the original list:
def clean_database(record_ids):
    # Fix 2: Iterate backwards through the list
    # When iterating from end to start, removing elements doesn't affect indices of unprocessed elements
    for i in range(len(record_ids) - 1, -1, -1):
        if record_ids[i] % 2 != 0:
            record_ids.pop(i)
    return record_ids


cleaned = clean_database([1,3,4,6,7,9,10])
print(f"Final List: {cleaned}")

# Creating a new list:
def clean_database(record_ids):
    # Fix 1: Use list comprehension to create a new list with only even numbers
    # This avoids modifying the original list during iteration
    return [record_id for record_id in record_ids if record_id % 2 == 0]


cleaned = clean_database([1, 3, 4, 6, 7, 9, 10])
print(f"Final List: {cleaned}") 




   