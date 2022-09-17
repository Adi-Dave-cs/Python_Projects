import xml.etree.ElementTree as ET

data = '''
<person> 
    <name> Aditya </name>
    <phone type = 'intl'>
        +91 9106245105
    </phone>
    <email hide = 'yes'/>
</person>
'''

tree = ET.fromstring(data)
print('Name : ', tree.find('name').text)
print('Attr : ', tree.find('email').get('hide'))


data2 = '''
<stuff>
    <persons>
        <person> 
            <name> Aditya </name>
            <phone type = 'intl'>
                +91 9106245105
            </phone>
            <email hide = 'yes'/>
        </person>
        <person> 
            <name> Aditya </name>
            <phone type = 'intl'>
                +91 9106245105
            </phone>
            <email hide = 'yes'/>
        </person>
    </persons>
</stuff>
'''

tree2 = ET.fromstring(data2)
list_p = tree2.findall('persons/person')
print("Person count",len(list_p))
for i in list_p :
    print('Name : ', i.find('name').text)
    print('Attr : ', i.find('email').get('hide'))