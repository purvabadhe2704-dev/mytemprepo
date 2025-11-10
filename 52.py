# 1.List
# Function in list - len(), min(), max(), type(), tuple()

colours = ['red','pink','yellow','green','orange','black'] # List
nums = [20,30,98,76,56,95] #List

print(len(colours))
print(len(nums))

print(min(colours)) #black
print(min(nums))    #20

print(max(colours)) #yellow
print(max(nums))    #98

print(type(colours))  # class<'list'>
print(type(nums))     # class<'list'>

t1 = tuple(colours) # convert a list into tuple
print (t1)
print(type(t1))   #class<'tuple'>

