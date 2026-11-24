size = int(input("Enter the hash table size: "))
hash_table = [None] * size

n = int(input("Enter the number of elements: "))

if n > size:
    print("The number of elements cannot exceed the size of hash table")

else:
    for i in range(n):
        key = int(input("Enter a key: "))

        index = key % size

        if hash_table[index] is None:
            hash_table[index] = key

        elif hash_table[index] % size != index:

            old_key = hash_table[index]
            hash_table[index] = key

            new_index = (index + 1) % size
            
            while hash_table[new_index] is not None:
                new_index = (new_index + 1) % size

            hash_table[new_index] = old_key

        else:
            new_index = (index + 1) % size

            while hash_table[new_index] is not None:
                new_index = (new_index + 1)% size

            hash_table[new_index] = key

print("\nHash table: ")
for i in range(size):
    print(i,":",hash_table[i])
    