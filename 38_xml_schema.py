# XML SCHEMA - describes the format XML documents exchanged between two systems must follow, like a "contract"
# Written in XML

# The XML document and the XML schema contract are submitted to a Validator software and it checks the document's compliance

# There are many XML Schema Languages


# XSD - XML Schema from the W3C

"""
Example of XML and Schema

<person>
    <lastname>Severance</lastname>
    <age>17</age>
    <dateborn>2001-04-17</dateborn>
</person>

<xs:complexType name="person">
    <xs:sequence>
        <xs:element name="lastname" type="xs:string"/>
        <xs:element name="age" type="xs:integer"/>
        <xs:element name="dateborn" type="xs:date"/>
    </xs:sequence>
</xs:complexType>
"""


# XML CONSTRAINTS
"""
    Example of XML constraints

    <xs:element name="full_name" type="xs:string" minOccurs="1" maxOccurs="1"/>
    <xs:element name="bar" maxOccurs="unbounded"/>
"""


# XML DATA TYPES - string, date, dateTime, decimal, integer...
"""
    <xs:element name="customer" type="xs:string"/>
    <xs:element name="start" type="xs:date"/>
    <xs:element name="startdate" type="xs:dateTime"/>
    <xs:element name="prize" type="xs:decimal"/>
    <xs:element name="weeks" type="xs:integer"/>
    <xs:element name="foo" type="xs:positiveInteger"/>
"""


# ISO 8601 DATE/TIME FORMAT
# YYYY-MM-DDTHH:MM:SSZ
# 2022-05-30T09:30:10Z
# The last letter is the timezone, in this case Z stands for Zulu time or UTC / GMT


# WORKING WITH XML IN PYTHON
import xml.etree.ElementTree as ET

data = """<person>
    <name>Chuck</name>
    <phone type="intl">
        +1 734 303 4456
    </phone>
    <email hide="yes"/>
<person>"""

tree = ET.fromstring(data)  # this line can result in error if there are errors in the XML
# Query the resulting object to access data
print(tree.find('name').text)  # -> Chuck
print(tree.find('email').get('hide'))  # -> yes