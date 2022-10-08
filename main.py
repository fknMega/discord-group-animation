import requests
import time

#group id
id = ''

#token
token = ''

#name to animate
name = 'test'

#delay in seconds
delay = 1



#create a new method
def animate(name):
    #loop through the name characters and add them to a string

    new_name = ''
    for i in name:
        #add the character to the string
        new_name += i

        #skip if the character is a space
        if i == ' ':
            continue



        #change the name
        change_name(new_name)
        #sleep for x seconds
        time.sleep(delay)



def change_name(name):
    #send a request to discord to change the name of the group


    #add auth token
    headers = { 'Authorization': token , 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36' , 'content-type': 'application/json' }

    #send a patch req
    r = requests.patch('https://discord.com/api/v9/channels/' + id, headers=headers, json={  'name': name})
    print(r.status_code)


animate(name)

