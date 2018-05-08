
users = [
        { "id": 0, "name": "Hero" },
        { "id": 1, "name": "Dunn" },
        { "id": 2, "name": "Sue" },
        { "id": 3, "name": "Chi" },
        { "id": 4, "name": "Thor" },
        { "id": 5, "name": "Clive" },
        { "id": 6, "name": "Hicks" },
        { "id": 7, "name": "Devin" },
        { "id": 8, "name": "Kate" },
        { "id": 9, "name": "Klein" }
]

friendships = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (3, 4),
               (4, 5), (5, 6), (5, 7), (6, 8), (7, 8), (8, 9)]

for user in users:
    user["friends"] = []

for i, j in friendships:
    users[i]["friends"].append(users[j]) # add i as a friend of j
    users[j]["friends"].append(users[i]) # add j as a friend of i

def number_of_friends(user):
    """How many friends does user have?"""
    return len(user["friends"])

total_connections = sum(number_of_friends(user)
                        for user in users)

num_users = len(users)

average_connections = total_connections / num_users

# sort from most friends to least friends
# create a list of user id and the number of friends
num_friends_by_id = [(user["id"], number_of_friends(user))
                     for user in users]

sorted(num_friends_by_id,
       key = lambda (user_id, num_friends): num_friends,
       reverse = True)

def friend_of_friends_ids_bad(user):
    return[foaf["id"],
           for user in users]

# word counter
word_counts = {}
for word in document:
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_count = 1

for word in document:
    try:
        word_counts[word] += 1
    except KeyError:
        word_counts[word] = 1

from collections import defaultdict

word_counts = defaultdict(int)

for word in document:
    word_counts[word] += 1

dd_list = defaultdict(list)
dd_list[2].append(1)

{2: [1]}
