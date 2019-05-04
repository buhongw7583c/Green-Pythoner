d = {'hong': 'beijing', 'yi': 'us', 'ping': 'shanghai', 'xin': ''}

print(d)

new_d = {key: value for value, key in d.items() if key != '' }
print(new_d)