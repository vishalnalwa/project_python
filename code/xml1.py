#This program teaches how to parse xml with python
import xml.etree.ElementTree as ET

data = '''
<person>
<name>Chuck</name>
<phone type="intl">
+1 734 303 4456
</phone>
<email hide="yes" />
</person>'''

tree = ET.fromstring(data)
print(type(tree))
print('Name', tree.find('name').text)
print('Atrrb:',tree.find('email').get('hide'))
