# ***************************************************************************************************** #
#                                                                                                       #
#                                                                  :::::       :::::        :::         #
#    main.py                                                      +:+:+:+     +:+:+:+     :+:+:+        #
#                                                                +:+  :+:    +:+   :+:   +:+ +:+        #
#    By: rdidier- <didier.rda@gmail.com>                        #+#  +:+    #+#   +:+   +#+  +:+        #
#                                                              #+# #+#     #+#   #+#   +#+#+#+#+        #
#    Created: 2019/11/19 16:28:50 by rdidier-                 #+#   #+#   #+#   #+#   #+#    #+#        #
#    Updated: 2019/11/20 00:10:28 by rdidier-                ###   ###   ########    ###     ###.br     #
#                                                                                                       #
# ***************************************************************************************************** #

#list behave as a C pointer 
lista = ['a','c','b','x']
new_list = lista
lista[0] = 'z'
print(new_list)

#list unpacking
a,b, *other, c = [1,2,3,4,5,6,7,8]

print(a)
print(b)
print(other)
print(c)

#dictionary declarations
user = {
    'basket':[1,2],
    'greet': '',
    'age':20
}

user2 = dict(name ='Jones')

#set
my_set = {1,2,3}

print(1 in my_set)

a = [1,2,3]
b = a

print(a is b)
print(a == b)

#for loop in dict
#for item in user:
 #   print(item)

for item in user.items():
   key, value = item
   print(key, value)

#In a more simple-way


for key, value in user.items():
    print(key, value)

for i, char in enumerate("Helloo"):
    print(i, char)

#While with else aplication

while i < 50:
    print(i)
    i += 1
    break
else:
    print('Done with all the work')

#break, continue and pass

for i, char in enumerate("Helloo"):
    continue
    print(i, char)
    

for i, char in enumerate("Helloo"):
    # THINKING ABOUT IT
    pass

#Default Parameters
def say_hello(name = 'Darth Vader', emoji = '😈'):
    print(f'hello {name}{emoji}')   
say_hello()

#Positional arguments
say_hello('😍','Didier')
say_hello('Didier', '😍')

#Keyword arguments
say_hello(emoji ='😍', name = 'Rodrigo')
say_hello('Timmy')




