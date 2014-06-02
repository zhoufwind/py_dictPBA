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
if request == 'p': key = 'phone'
if request == 'a': key = 'addr'

# print the value
if name in people: print "%s's %s is: \'%s\'." % (name, labels[key], people[name][key])

