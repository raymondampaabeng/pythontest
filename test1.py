current_users= ['raymond', 'boniface', 'kwaku', 'yaw', 'kwasi']
new_users= ['king', 'akosua', 'John', 'agyei', 'kwadwo']
used_elements = set[current_users]

for new_user in new_users:
    if new_user in used_elements:
        print('You will have to enter a new username')
    else:
        print('The username is available')

used_elements= set(map(str.lower,current_users))
for new_user in new_users:
    if str.lower(new_user)in used_elements:
        print(f'new_user (or its lowercase equivalent)has already been used')