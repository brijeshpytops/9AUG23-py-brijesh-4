"""
List - ordered, mutable, allow duplicate value
Syntax:
list_name = []
list_name = list()


l = [10, 20.3, "python", 3 + 8j]
# l = list()

# check type
# print(type(l))

# print(l)

# access element of list

# positive indexing
# print(l[3])

# negetive indexing
# print(l[-3])

# slicing 
# nums = [1,2,3,4,5,6,7,8,9,10]
# print(nums)
# nums[start:stop-1:step-1]
# print(nums[2:5])
# print(nums[::3])
# print(nums[-4:-7:-1])

# replica
veg = ['tomato', 'potato', 'onion']
# print(veg * 3)

products = ['pen', 'book']

items = veg * 3
items.sort()
final_items = items + products

# add
# print(final_items)
cereals = ['rice', 'wheat']
# final_items.append(cereals)
# final_items.extend(cereals)
# final_items.insert(2, cereals)

# update
# final_items[2] = cereals

# delete
# final_items.pop()
# final_items.remove('pen')
# del final_items[-2]

# reverse
# final_items.reverse()

# 
# final_items.clear()

# final_items_2 = final_items.copy()
# print(final_items_2)

# print(dir(final_items))

# length
# print(len(final_items))




Tuple - ordered, immutable, allow duplicate value
Syntax:
tuple_name = ()
tuple_name = tuple()


nums = [1,1,2,3,4,5,6,7,8,9,10]

# tokens = ()
# tokens = tuple()
tokens = tuple(nums)
# tokens = 1,
# print(type(tokens))

# print(len(tokens))

# indexing, slicing

# print(dir(tokens))

# methods
# print(tokens.count(1))
# print(tokens.index(7))
# print(tokens.index(1 + 1))

# tokens[1] = 111
# print(tokens)


Set - unordered, mutable, do not allow duplicate value
Syntax:
set_name = {}
set_name = set()

nums = [1,1,2,3,4,5,6,7,8,9,10]
tokens = tuple(nums)
final_tokens = set(tokens)

print(final_tokens)

print(set([1,2,1,1,1,1,2,2,2,3,3,34,5,4,]))


Dictionary -
Syntax:
dict_name = {
    'key':'value',
    'key':'value',

}
dict_name = dict()
"""

contacts = {
    'a':{
        'aman':{
            'mobile':['0900909090', '6565434387'],
            'email':['aman@gmail.com']
        },
        'ajay':{
            'mobile':['56566256652']
        }
    },
    'b':{
        'babbn':{
            'mobile':['9090909090']
        }
    }
}
# print(contacts)
# print(len(contacts))
# print(type(contacts))

# access dict
# print(contacts['a'])
# print(contacts['b'])

# print(contacts['a']['aman'])
# print(contacts['a']['aman']['mobile'][1])
# print(type(contacts['a']['aman']))

# 'update','clear', 'copy',  'get', 'items','values', 'keys', 'pop', 'popitem',  'fromkeys','setdefault', 
# print(dir(contacts))

new_dict = {
    'c':{
        'chaman':{
            'mobile':['0000909090']
        },
        'chintu':{
            'mobile':['243243428']
        }
    },
    'd':{
        'dhiren':{
            'mobile':['656565656565']
        }
    }
}

contacts.update(new_dict)

# print(contacts.get('d'))
# contacts.clear()

# print(contacts.keys())
# print(contacts.values())
# print(contacts.items())

# for k in contacts.keys():
#     print(k)
# for v in contacts.values():
#     print(v)
# for k, v in contacts.items():
#     print(k, v)

# contacts.popitem()
# contacts.pop('c')


# print(contacts)


# car = {
#     'model':'XYZ',
#     'price':'25l',
#     'color':'blue',
#     'is_EV':True
# }

# car.setdefault('color','red')
# car.setdefault('is_EV',False)
# print(car)

# products = dict()
# veg = ['tomato', 'potato', 'banana']
# price = 50

# print(products.fromkeys(veg, price))


# print(contacts)
# user = {
#     'name':input("Enter your name : ")
# }
# print(user)