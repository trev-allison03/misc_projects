import json

following = open('following.json')
followers = open('followers_1.json')

following_json = json.load(following)
followers_json = json.load(followers)

def parse_json_string(json_file, str_):
    curr_set = set()
    for curr in json_file[str_]:
        curr_set.add(curr['string_list_data'][0]['value'])
    return curr_set

def parse_json_no_string(json_file):
    users = set()
    for user in json_file:
        users.add(user['string_list_data'][0]['value'])
    return users

not_following = parse_json_string(following_json, 'relationships_following') - parse_json_no_string(followers_json)

for users_not_follwing in not_following:
    print(users_not_follwing)