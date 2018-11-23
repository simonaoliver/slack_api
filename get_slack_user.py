import requests
import pandas as pd

url = "https://slack.com/api/users.list?token=<your token>"
channels = "https://slack.com/api/channels.list?token=<your token>"
channels = requests.get(channels, headers={'Authorization': '<your token>'})
response = requests.get(url, headers={'Authorization': '<your token>'})

for channel in channels.json()['channels']:
    channels_dict[channel['name']] = {"members": channel}

channels_df = pd.DataFrame(channels.json()['channels'])

channels_df.set_index("name", inplace=True)

user_email_list = []
for user in response.json()['members']:
    if 'email' in user['profile']:
        user_email_list.append(user['profile']['email'])
    else :
        user_email_list.append('null')
        
members_df = pd.DataFrame(response.json()['members'])

members_df.set_index("name", inplace=True)

channel_lists=[]
channels_df
for i in members_df['id']:
    channel_list = []
    for j in channels_df['members']:
        if i in j:
            for key in channels_df.members.keys():
                if channels_df.members[key] ==  j:
                    channel_list.append(key)

    channel_lists.append(channel_list)
    
    members_df['membership'] = channel_lists
    
    members_df['email'] = user_email_list
    
    members_df.to_csv('slack_membership.csv')
  
