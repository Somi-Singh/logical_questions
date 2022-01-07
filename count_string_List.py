#counte len(string in loop with list)#
List=["shireen","nazneen","shahnaaz"]
for i  in List:
    print(i, len(i))

def count_string_len(name_list):
    for i  in name_list:
        print(i,len(i))
count_string_len(["shireen","nazneen"])