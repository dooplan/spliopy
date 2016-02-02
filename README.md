# spliopy
Python wrapper around Splio-EmailForge REST API 1.0

## Installation
``` pip install spliopy``` 

## Usage 
```python
from spliopy.spliopy import SplioConnection
connection = SplioConnection(API_KEY, UNIVERSE)
```
  - Get universe database fields
```python
    connection.get_fields() 
```
  - Get universe avaiable lists
```python 
    connection.get_lists() 
```
  - Get all known attributes for a contact identified by email.
```python 
    connection.get_contact('example@example.com') 
```
  - Create a new contact. It is mandatory to provide the email address within the fields.
```python 
    connection.add_contact({'email':'example@example.com', 'firstname'='example'....}) 
```
  - Update an existing contact identified by email.
```python 
    connection.update_contact('example@example.com', {'firstname':'example_updated'...}) 
```
  - Check if email is blacklisted in the universe.
```python 
    connection.is_blacklisted('example@example.com') 
```
  - Blacklist email in the universe.
```python 
    connection.blacklist('example@example.com') 
```
