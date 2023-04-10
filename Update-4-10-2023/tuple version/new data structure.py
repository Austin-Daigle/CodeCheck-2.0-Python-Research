class ObjectData:
    def __init__(self, pairs_list, pairs_list_2, obj_str):
        self.pairs_list = pairs_list
        self.pairs_list_2 = pairs_list_2
        self.obj_str = obj_str

class ObjectsStore:
    def __init__(self):
        self.store = {}

    def add_object(self,obj_str, pairs_list, pairs_list_2):
        if obj_str in self.store:
            existing_obj = self.store[obj_str]
            existing_obj.pairs_list.extend(pairs_list)
            existing_obj.pairs_list_2.extend(pairs_list_2)
        else:
            new_obj = ObjectData(pairs_list, pairs_list_2, obj_str)
            self.store[obj_str] = new_obj

    def remove_redundant_pairs(self):
        for obj_data in self.store.values():
            unique_pairs = []
            for pair in obj_data.pairs_list:
                if pair not in unique_pairs:
                    unique_pairs.append(pair)
            obj_data.pairs_list = unique_pairs
            unique_pairs_2 = []
            for pair in obj_data.pairs_list_2:
                if pair not in unique_pairs_2:
                    unique_pairs_2.append(pair)
            obj_data.pairs_list_2 = unique_pairs_2
        print("redundant pairs removed")

    def remove_underlaps(self):
        for obj_data in self.store.values():
            pairs_list = obj_data.pairs_list
            pairs_list_2 = obj_data.pairs_list_2
            new_pairs_list = []
            for pair in pairs_list:
                remove_pair = False
                for other_obj_data in self.store.values():
                    if other_obj_data is not obj_data:
                        for other_pair in other_obj_data.pairs_list:
                            if other_pair[0] >= pair[0] and other_pair[1] <= pair[1]:
                                remove_pair = True
                                break
                    if remove_pair:
                        break
                if not remove_pair:
                    new_pairs_list.append(pair)
            obj_data.pairs_list = new_pairs_list

            new_pairs_list_2 = []
            for pair in pairs_list_2:
                remove_pair = False
                for other_obj_data in self.store.values():
                    if other_obj_data is not obj_data:
                        for other_pair in other_obj_data.pairs_list_2:
                            if other_pair[0] >= pair[0] and other_pair[1] <= pair[1]:
                                remove_pair = True
                                break
                    if remove_pair:
                        break
                if not remove_pair:
                    new_pairs_list_2.append(pair)
            obj_data.pairs_list_2 = new_pairs_list_2
        print("underlaps removed")

    def __str__(self):
        output = ''
        for obj_str, obj_data in self.store.items():
            pairs_str = ', '.join([str(pair) for pair in obj_data.pairs_list])
            pairs_str_2 = ', '.join([str(pair) for pair in obj_data.pairs_list_2])
            output += f'"{obj_str}" |\tA = [{pairs_str}]\n\tB = [{pairs_str_2}]\n'
        return output 

###########################################################################

store = ObjectsStore()

store.add_object("T",[[0,1]],[[0,1]])
store.add_object("Th",[[0,2]],[[0,2]])
store.add_object("Thi",[[0,3]],[[0,3]])
store.add_object("This",[[0,4]],[[0,4]])
store.add_object("h",[[1,2],[8,9]],[[1,2]])
store.add_object("hi",[[1,3]],[[1,3]])
store.add_object("his",[[1,4]],[[1,4]])
store.add_object("i",[[2,3],[5,6]],[[2,3]])
store.add_object("is",[[2,4],[5,7]],[[2,4]])
store.add_object("s",[[3,4],[6,7]],[[3,4]])
store.add_object("i",[[2,3],[5,6]],[[2,3]])
store.add_object("is",[[2,4],[5,7]],[[2,3]])
store.add_object("s",[[3,4],[6,7]],[[3,4]])
store.add_object("h",[[1,2],[8,9]],[[1,2]])

print(store)
store.remove_redundant_pairs()
print(store)
store.remove_underlaps()
print(store)