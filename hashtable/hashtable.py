class Node:
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        pass

    def insert_at_head(self, node):
        node.next = self.head
        self.head = node

    def find(self, value):
        cur = self.head
        while cur is not None:
            if cur.key == value:
                return cur
            
            cur = cur.next

        return None

    def delete(self, value):
        cur = self.head
        # case if value is in head
        if cur.key == value:
            self.head = self.head.next
            return cur
        
        # general case
        prev = cur
        cur = cur.next

        while cur is not None:


            if cur.key == value:
                prev.next = cur.next
                return cur
            else:
                prev = prev.next
                cur = cur.next
        
        return None

# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity):
        self.capacity = capacity
        self.hash_list = [LinkedList()] * capacity
        self.count = 0


    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """

        return self.capacity #len(self.hash_list)


    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        return self.count / self.capacity


    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """

        # Your code here


    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        hash = 5381

        for char in key:
            hash = ((hash << 5) + hash) + ord(char)
        return hash & 0xFFFFFFFF


    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        #return self.fnv1(key) % self.capacity
        return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        slot = self.hash_index(key)
        ll = self.hash_list[slot]
        new_node = Node(key, value)
        ll.insert_at_head(new_node)
        self.count += 1

        
        if self.get_load_factor() > 7.0:
            print('hi')
            self.resize(self.capacity * 2)

    def put2(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        slot = self.hash_index(key)
        ll = self.hash_list[slot]
        new_node = Node(key, value)
        ll.insert_at_head(new_node)
        self.count += 1

        




    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        
        ll = self.hash_list[self.hash_index(key)]
        self.count -= 1
        return ll.delete(key)

        


    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        
        ll = self.hash_list[self.hash_index(key)]
        node = ll.find(key)
        if node is not None:
            return node.value
        else:
            return None
        


            
        
        

    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        
        self.capacity = new_capacity
        temp_list = self.hash_list
        
        self.hash_list = [LinkedList()] * self.capacity
        for ll in temp_list:
            cur = ll.head
            if ll.head is None:
                pass

            while cur is not None:

                self.put2(cur.key, cur.value)
                cur = cur.next






if __name__ == "__main__":
    ht = HashTable(8)
    

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")
    ht.put("line_13", "And stood awhile in thought.")
    ht.put("line_14", "And stood awhile in thought.")
    ht.put("line_15", "And stood awhile in thought.")
    ht.put("line_16", "And stood awhile in thought.")
    ht.put("line_17", "And stood awhile in thought.")
    ht.put("line_18", "And stood awhile in thought.")
    ht.put("line_19", "And stood awhile in thought.")
    ht.put("line_20", "And stood awhile in thought.")
    ht.put("line_21", "And stood awhile in thought.")
    ht.put("line_22", "And stood awhile in thought.")
    ht.put("line_23", "And stood awhile in thought.")
    ht.put("line_24", "And stood awhile in thought.")
    ht.put("line_25", "And stood awhile in thought.")
    ht.put("line_26", "And stood awhile in thought.")
    ht.put("line_27", "And stood awhile in thought.")
    ht.put("line_28", "And stood awhile in thought.")
    ht.put("line_29", "And stood awhile in thought.")
    ht.put("line_30", "And stood awhile in thought.")
    ht.put("line_31", "And stood awhile in thought.")
    ht.put("line_32", "And stood awhile in thought.")
    ht.put("line_33", "And stood awhile in thought.")
    ht.put("line_34", "And stood awhile in thought.")

    print("")
    
    # Test storing beyond capacity
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    # Test resizing
    old_capacity = ht.get_num_slots()
    print(ht.get_load_factor())
    ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()
    print(ht.get_load_factor())

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    print("")
    print(ht.get_load_factor())
