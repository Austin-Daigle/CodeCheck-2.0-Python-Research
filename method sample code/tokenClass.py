class StringObject:
    def __init__(self, begin, end, string):
        self.begin = begin
        self.end = end
        self.string = string

    def __str__(self):
        return "["+str(self.begin)+","+str(self.end)+",\""+str(self.string)+"\"]"
        
class StringCollection:
    def __init__(self):
        self.objects = []
        
    def add_object(self, obj):
        objHasOverlap = False
        for existing_obj in self.objects:
            if obj.begin >= existing_obj.begin and obj.end <= existing_obj.end:
                objHasOverlap = True
                #raise ValueError("Object with overlapping indexes cannot be added")
        if not objHasOverlap:
            print(str(obj)+" has been added successfuly.")
            self.objects.append(obj)
        else:
            print("\t[!] "+str(obj)+" could not be added due to a overlap in the indexes.")




    def __str__(self):
        result = ""
        for x in range(0,len(self.objects)):
            result = result + "\n"+str(self.objects[x])
        return result
        


####################################

tokens = StringCollection()
tokens.add_object(StringObject(1, 5, "Hello"))
tokens.add_object(StringObject(10, 50, "dummy"))
tokens.add_object(StringObject(2,4, "error"))
print(tokens)
