"""Task: You are given a list of strings. Some of those strings may contain integers, 
for example Digital Car33r Institute. Implement a method digit_filter that takes 
a list of strings as an argument and only returns those strings that don't contain a number. """
import re

# l33t = ['Digital Car33r Institute', 'DCI', 'Digital', 'Career', 'Inst1tut3']

# new = []
# for i in l33t:
#     if not re.search(r'\d', i ):

#         new.append(i)

# print(new)

# def digit_filter(list):
#     new = []
#     for i in list:
#         if not re.search(r'\d', i):
            
#             new.append(i)
            
#     print(new)
    

# l33t = ['Digital Car33r Institute', 'DCI', 'Digital', 'Career', 'Inst1tut3']

# digit_filter(l33t)

#------------------------------------------------------------

# def digit_filter(list):
    
#     container = []
    
#     for element in list:
        
#         if not any(i.isdigit() for i in element):
        
#             container.append(element)
            
#     return container
    
    
    
# l33t = ['Digital Car33r Institute', 'DCI', 'Digital', 'Career', 'Inst1tut3']


# print(digit_filter(l33t))


#------------------------------------------------------------

# def digit_filter(list):
    
#     container = []
    
#     for element in list:
        
#         for i in element:
            
#             if i.isdigit():
                
#                 container.append(element)
#                 break
    
#     for e in container:
        
#         list.remove(e)
    
#     return list





# l33t = ['Digital Car33r Institute', 'DCI', 'Digital', 'Career', 'Inst1tut3']

# print(digit_filter(l33t))


