# print('Hello World')

# create database

people = {
          'Alice': {
                    'phone': '2341',
                    'addr': 'Foo drive 23'
                    },
          'Beth': {
                   'phone': '9102',
                   'addr': 'Bar street 42'
                   },
          'Cecil': {
                    'phone': '3158',
                    'addr': 'Baz avenue 90'
                    }
          }

# create labels
labels = {
          'phone': 'phone number',
          'addr': 'address'
          }

# enter name
name = raw_input('Name: ')

# choose function
request = raw_input('phone number(p) or address(a)?')

key = request # input either 'p' nor 'a'
if request == 'p': key = 'phone'
if request == 'a': key = 'addr'

# print the value
# if name in people: print "%s's %s is: \'%s\'." % (name, labels[key], people[name][key])

# using get() get default value
person = people.get(name, {})
label = labels.get(key, key)
result = person.get(key, 'not available')

print "%s's %s is: \'%s\'." % (name, label, result)

