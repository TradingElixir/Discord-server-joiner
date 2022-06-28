import requests

link = input('rfmYs6RaEB')
if len(link) > 6:
    link = link[19:]
apilink = "https://discord.gg/" + str(link)

print (link)

with open('tokens.txt','r') as handle:
        tokens = handle.readlines()
        for x in tokens:
            token = x.rstrip()
            headers={
                'Authorization': token
                }
            requests.post(apilink, headers=headers)
        print ("All valid tokens have joined!")
