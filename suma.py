def find_subarrays(big_array, small_array):
    subarrays = []
    small_length = len(small_array)
    
    for i in range(len(big_array) - small_length + 1):
        if big_array[i:i+small_length] == small_array:
            subarrays.append((i, i+small_length))
    
    return subarrays  

big_array = [5, 8, 3]
small_array = [3, 8, 5]

subarrays = find_subarrays(big_array, small_array)

if subarrays:
    print("Sub-arrays formed after matching:")
    for start, end in subarrays:
        print(f"From Index {start} to {end-1}: {big_array[start:end]}")
else:
    print("No sub-arrays found.")
