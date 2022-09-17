import json

data = '''
    {
        "name" : "Aditya",
        "phone" :
            {
                "type" : "intl",
                "number" : "+91-9106245105"
            },
        "email" : 
        {
            "hide" : "yes"
        }
    }
'''

info = json.loads(data)
print('Name : ', info["name"])
print('Hide : ', info["email"]["hide"])


data2 = '''
    [
        {
            "name" : "A",
            "id"  : "4",
            "designation" : "Engineer"
        },
        {
            "name" : "B",
            "id"  : "5",
            "designation" : "Sr. Engineer"
        }
    ]
'''

info2 = json.loads(data2)
print('-------------------------------------------------------------------------------------')
for i in info2:
    print('Name :',i['name'])
    print('id :',i['id'])
    print('designation : ',i['designation'])
    print('-------------------------------------------------------------------------------------')