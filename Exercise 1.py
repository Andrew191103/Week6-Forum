inventory = {
 'gold' : 500,
 'pouch' : ['flint', 'twine', 'gemstone'],
 'backpack' : ['xylophone','dagger', 'bedroll','bread loaf']
}

inventory['pocket'] = ['seashell', 'strange berry', 'lint']
backpacks = inventory['backpack']
backpacks.sort()
backpacks.remove('dagger')
inventory['backpack'] = backpacks
inventory['gold'] += 50
print(inventory)
