# OA
# String comparison with many keys

def rich_comp(string_list):
    
    first_key = string_list[0]
    num = string_list[1]
    
    # Case when num isn't an int
    try:
        num = int(num)
    except:
        return []
    
    # ??sort list???
    def sort_twoKeys(l,first_key):
        if first_key == "latest": # Sort by time first
            l.sort(reverse=True, key = lambda x:(x[1], x[2], x[0]))
        elif first_key == "largest": # Sort by size first
            l.sort(reverse=True, key = lambda x:(x[2], x[1], x[0]))
    
    # Loop string,????string list???
    storage = []
    location_record = {}
    for i in range(2, len(string_list)):
        s = string_list[i].split(", ") # contains a space
        
        try:
            # negate so that they have the same sorting order as for names
            s[1] = -long(s[1]) # transform last modified time to long, 
            s[2] = -long(s[2]) # transform file size to long
        except ValueError:
            continue
        
        # Saves it if it's not seen
        if s[0] not in location_record:
            storage.append(s)
            location_record[s[0]] = len(storage)-1 # because s just got appended, location is len()-1
        # If seen, updates the existing one to more prioritized version
        else:
            loc = location_record[s[0]]
            to_be_compared = [storage[loc],s]
            sort_twoKeys(to_be_compared, first_key)
            storage[loc] = to_be_compared[0]
        
    # Finally sort the storage
    sort_twoKeys(storage, first_key)

    return storage

# Test case
# "Name Time Size"
first_key = "largest"
num_s = "10"
string_list = [first_key,num_s, \
               "I, 16, 10", "I, 15, 15", "I, 16, 11", \
               "You, 28, 16", "You, 29, 15", "You, 28, 17",\
              "He, a19, 0", "They, 10, b20","Her, 99, 0"]
print rich_comp(string_list)