

dct ={}
keys_list = []
values_list = []
with open('file1.txt') as input_file:
    content_list = input_file.readlines()
    for i in range(0,len(content_list),2):
        keys_list.append(content_list[i].strip()) 
        values_list.append(content_list[i+1].strip()) 

keys_list = [int(key) for key in keys_list]
print(keys_list)

for i in range(len(keys_list)):
    if keys_list[i] in dct.keys():
        dct[keys_list[i]] = f'{dct[keys_list[i]]}; {values_list[i]}' 
    else:
        dct[keys_list[i]] = values_list[i]

keys_list = list(dct.keys())
keys_list.sort()



with open('output_keys.txt', 'w') as output_file:
    for key in keys_list:
        output_file.write('{}: {}\n'.format(key,dct[key]))
    #keys_list.sort()
    #for i in range(1,len(keys_list)):
    #    if keys_list[i-1] == keys_list[i]:
    #        continue
    #    output_file.write(f'{keys_list[i-1]}: {dct[keys_list[i-1]]}\n')
    #output_file.write(f'{keys_list[-1]}: {dct[keys_list[-1]]}\n')

with open('output_titles.txt', 'w') as output_file:
    values_list.sort()
    for value in values_list:
        output_file.write(f'{value}\n')
    
print(keys_list)
print(values_list)
print(dct)