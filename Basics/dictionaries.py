# Dictionaries
d = {}
d['a'] = 'alpha'
d['g'] = 'gamma'
d['o'] = 'omega'

print 'd          ', d 
print 'd.keys()   ', d.keys()
print 'd.values() ', d.values()

print '----------------------------'

print 'Loop through keys and print values'

for k in sorted(d.keys()):
  print 'key:', k, '->', d[k]

print '----------------------------'

print 'Loop through d.items()'
for tuples in d.items():
  print 'tuples: ', tuples
