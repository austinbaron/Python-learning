
### Python Classes and objects

To understand the need for creating a class and object in Python let’s consider an example, let’s say you wanted to track the number of dogs that may have different attributes like breed and age. If a list is used, the first element could be the dog’s breed while the second element could represent its age. Let’s suppose there are 100 different dogs, then how would you know which element is supposed to be which? What if you wanted to add other properties to these dogs? This lacks organization and it’s the exact need for classes.

Class Definition
```python

class ClassName:
    # Statement

```
Object Definition
```python
obj = ClassName()
print(obj.atrr)

```

#### Some points on Python class:

* Classes are created by keyword class.
* Attributes are the variables that belong to a class.
* Attributes are always public and can be accessed using the dot (.) operator. Eg.: My class.Myattribute

#### Object of Python Class

An Object is an instance of a Class. A class is like a blueprint while an instance is a copy of the class with actual values. It’s not an idea anymore, it’s an actual dog, like a dog of breed pug who’s seven years old. You can have many dogs to create many different instances, but without the class as a guide, you would be lost, not knowing what information is required.

An object consists of:

* State: It is represented by the attributes of an object. It also reflects the properties of an object.
* Behavior: It is represented by the methods of an object. It also reflects the response of an object to other objects.
* Identity: It gives a unique name to an object and enables one object to interact with other objects.