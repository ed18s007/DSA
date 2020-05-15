# MAP IS DICTIONARY

udacity = {}
udacity['u'] = 1
udacity['d'] = 2
udacity['a'] = 3
udacity['c'] = 4
udacity['i'] = 5
udacity['t'] = 6
udacity['y'] = 7

print(udacity)
print(udacity['u'], udacity['c'], udacity['t'])

dictionary = {}
dictionary['d'] = [1]
dictionary['i'] = [2]
dictionary['c'] = [3]
dictionary['t'] = [4]
dictionary['i'].append(5)
dictionary['o'] = [6]
dictionary['n'] = [7]
dictionary['a'] = [8]
dictionary['r'] = [9]
dictionary['y'] = [10]

print(dictionary)

locations = {'North America': {'USA': ['Mountain View']}}
locations['North America']['USA'].append('Atlanta')
locations['Asia'] = {'India': ['Bangalore'], 'China' : ['Shanghai']}
locations['Africa'] = {'Egypt':['Cairo']}

print(locations['North America']['USA'])
usa_loc = locations['North America']['USA']
usa_loc.sort()
print(usa_loc)

asia_loc = locations['Asia']
asia_loc_list = [element + '-' + str(*asia_loc['India']) for element in asia_loc]
asia_loc_list.sort()
print(asia_loc_list)