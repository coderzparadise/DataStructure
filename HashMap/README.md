# Data Structure: HashMap()

Background: A HashMap provides storing and accessing data in (key, value) pairs. Each key is associated with a value, and you can access the value by using the corresponding key. By creating custom hashmap, we can even add weight to key pairs.

### Functions
get_hash_func() - Calculates the hash value for a given item.

add() - Adds a new item to the hash map, resizing if the load factor exceeds 1 (overloaded).\
insert() - Adds a new item to the hash map, resizing if the load factor exceeds 1 (overloaded).

insert_full() - Creates a new hash map with double the size (plus one) and inserts all existing items and the new item into it.

display() - Prints the contents of the hash map (the list of buckets).
