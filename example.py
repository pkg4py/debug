from debug import Debug

debug1 = Debug('example:debug1')
debug2 = Debug('example:debug2')
debug3 = Debug('example:debug3')

i = 0

while i < 10:
  debug1('1 - %d - name: %s, age: %d', i, 'haoxin', 18)
  debug2('2 - %d - name: %s, age: %d', i, 'haoxin', 18)
  debug3('3 - %d - name: %s, age: %d', i, 'haoxin', 18)
  i += 1
