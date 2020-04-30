'''
String Methods:
1)islower(): This method returns True if the character is a lowercase letter otherwise it will return False.

2)isupper(): This method returns True if the character is an uppercase letter otherwise it will return False.

3) upper(): This method converts an alphabet from lowercase letter to uppercase letter.

4)lower(): This method converts an alphabet from uppercase letter to lowercase letter.

5)isalpha(): This method returns True if a character is an alphabet otherwise it will return False.

6)isspace(): This method returns True if a character is a space otherwise it will return False.

7) isdigit(): This method returns True if a character is a digit(0 to 9) otherwise it will return False.

8)strip(): This method removes whitespaces at begining and ending of a given string (leading and trailing whitespaces).

9) lstrip():
This method will remove spaces at the begining (leading) of a given string.

10) rstrip():
This method will remove spaces at the ending(trailing) of a given string.

11) replace():
*This method is used to repace a particular substring in a given string.
*takes 2 arguments
General syntax:
replace(old_sub_str , new_sub_str)


12) startswith():
*This method returns True if the string starts with a particular substring otherwise it will return False.
*takes 3 arguments
*General syntax:
startswith(substr, start point , end point)
Note:
* 2nd and 3rd argument is optional

13) endswith():
* This method returns True if the string ends with a particular substing otherwise it will return False.
*takes 3 arguments
*General syntax:
endswith(substr, start point , end point)
Note:
* 2nd and 3rd argument is optional

14)isalnum():--->isalphanumeric():
*This method returns True
case1:if the string contains both alphabets and numbers
case2:if the string contains only alphabets
case3:if the string contains only numbers

*Otherswise it will return False
case1:if the string contains space
case2:if the string contains special characters - @#$&
15) join():
This method is used to join elements of an iterable with a certain character separating the each elements of an iterable.
*iterables--->string, list ,tuple, set, dictionary
# input: "abc for tech tech for abc"
#output:"aabbcccceeffhhoorrtt"

16) find():
This method will find a character or substirng in a string and it returns lowest index value of a character or a substring.
* it finds character or substirng in string from left to right.
*if character or substirng is not present it will return -1.

17) rfind():
This method will find a character or substirng in a string and it returns highest index value of a character or a substring.
* it finds character or substirng in string from right to left.
*if character or substirng is not present it will return -1.

18) index():
This method will return lowest index value of a character or a substring.
* it finds character or substirng in string from left to right.
*if character or substirng is not present in the string it will raise a ValueError.

19)rindex():
This method will return highest index value of a character or a substring.
* it finds character or substirng in string from right to left.
*if character or substirng is not present in the string it will raise a ValueError.

20) count():
This method will return number of occurrences of a character or a substring in a string.
*if a character or a substring is not present in a string, it will return 0

21) capitalize():
This method will convert the first character a string to uppercase
ex--> Abc ---> Abc
------>abc --->Aba
------->python ---Python

22) istitle():
This method will return True if the string begins with Uppercase letter otherwise it will return False.

23) casefold():
This method will convert from irrespective of lowercase or uppercase to lowercase format.

24)zfill():
This method will adds zeros in a given string at the beginning based on the width size.

25) swapcase():
This method will convert a character from lowercase to uppercase and viceversa
A-->a
b-->B

26) split():
This method will split() the given string based on the delimiter.
* By default it will consider space as the delimiter
*anything such as ,  @ 3 ,gn,sdsu
*By default it will store splitted characters in list

27) splitlines():
This method will make a split wherever it counters a escape sequences such as \n \r etc
* pass True as an arg for this method then it will return raw string & split ch at escape sequences

Functions over a string:

1) sorted() -->it is a inbuilt function where it will sort a sring in ascending order & it will return a list
2)len() -->return length of a string
3)max()-->return maximum character in a string
4)min()-->return minmum character in a string
5)ord()-->return ascii code of a character---a -->97
6)chr()-->return character of an ascii code -->65-->A

String operations:

------------------------------------------------------------
    Operations  Operator
------------------------------------------------------------

1) concatenation        -------------> +
2) repeatation             -------------> *
3)Access                    -------------->[]
4)slincing                   -------------->[:]
5)Membership operation ----------> in / not in
---------------------------------------------------------------

Collections in python:
--------------------------
* Collections is a module in python.

*Different types of collections
1)deque ---> double ended queue
2)namedtuple()
3)counter
4)OrderedDict
5)defaultdict
6)chainMap


1) deque:
------------
* deque is an object / class which is defined in collections module.
*deque is a list optimized for adding and removing items from both ends.

creating deque:
* we make use deque()--> constructor to create a double ended queue(deque).

Methods on deque:
-----------------------
1)append(x)---> It adds x to the right side of the deque.
2)appendleft(x) ---> It adds x to the left side of the deque.
3)extend(iterable)---> extend the right side of the deque by appending from an iterable.
4)extendleft(interable)---> extend the left side of the deque by appending from an iterable.
5)insert(i,x)---> it inserts x into the deque at the specified position i.
6)pop()---> it removes and return an element from right side of the deque.
7)popleft()--->it removes and return an element from left side of the deque.
8)remove(x)---> it removes the first occurrence of x and it raises a ValueError if element is not present.
9) copy() ---> it will create a shallow copy of a deque.
10)clear() --->removes all the elements of a deque.
11)count(x) ---> number of occurrences of x.
12)reverse()---> it revserses the deque in-place and returns None.
13)rotate(n=1)---> rotates deque n steps to the right side if n is positive ,if n is negative then it rotates deque n steps to the left side.

2)namedtuple():

why namedtuple():

*tuples is collection of arbitrary objects
 & tuples are immutable-->can't be modified once they are created
*tuple ele are accessed through integer indexes

problem with tuple
1)tup elements can only be accessed through integer indexes , we can't
give names to individual ele of tuple-->minimizes code readability

2) what if two tuples have the same number of elements and
 the same properties stored on them-->mixing up ele order(index) when accessing
 --> create bugs in your code
#example1

* The above problems can be fixed by using namedtuple()


what is namedtuple()
*namedtuple is a factory function.
* namedtuples are immutable similar to  regular tuples. Once we create them we can’t modify it.

*Each object stored in namedtuple can be accessed through a unique identifier-->this will help us not to remember integer indexes.

*Namedtuples can be a great alternative to defining a class manually and they have some other interesting features that
I want to introduce you

*namedtuples are extension of built-in tuples


#how to create namedtuple in python
#example:2

Accessing and Modifying
*dot notation with fields name
*index--we can integer indexes like how we used to fetch tuple elements
[]
*getattr(ref,'field_name')

Methods on namedtupe:

1) _fields:
This method returns a tuple of strings listing the field names.
Useful for introspection and for creating new named tuple types from existing named tuples

2)_replace():
This method returns a new object of the namedtuple replacing specified fields with new values

3)_make():
This method creates a new object from an existing iterable such as list, tuple, set

4)_asdict():
This method returns a new dict which maps field names to their corresponding values:

5)_field_defaults:
Dictionary mapping field names to default values.


==================================================================================
3)Counter:
A Counter is a dict subclass for counting hashable objects.
It is a collection where elements are stored as dictionary keys and their counts are stored as dictionary values.

--->Counter(iterable)

Methods:
1)elements()
*This method returns list over elements repeating each as many times as its count.
*Elements are returned in the order first encountered. If an element’s count is less than one, elements() will ignore it.

2)most_common(n)
*This method returns a list of the n most common elements and their counts from the most common to the least.
*Elements with equal counts are ordered in the order first encountered

3)subtract()
*Elements are subtracted from an iterable or from another mapping (or counter).
similar to dict.update() but subtracts counts instead of replacing them.
*Both inputs and outputs may be zero or negative.

dictionary methods on Counter

1) update():
it adds all the elements of a Counter to another Counter.
2) items():
It lists out the Counter's key and it's count as value.
3)keys():
It lists out the Counter's keys.
4)values():
It lists out the Counter's keys.
5)clear()"
It removes all the elements of a Counter.

operation:
+---> adds two Counters.
- --->subtracts two Counters.
union:
returns maximum count of two counters
intersection:
returns minimum count of two counters

4) OrderedDict:

###why OrderedDict when we have regular dictinary###

*The regular dict was designed to be very good at mapping operations.
Tracking insertion order was secondary.

*The OrderedDict was designed to be good at reordering operations.
Space efficiency, iteration speed, and the performance of update operations were secondary.

*Algorithmically, OrderedDict can handle frequent reordering operations better than dict.
This makes it suitable for tracking recent accesses (for example in an LRU cache).

*The equality operation for OrderedDict checks for matching order.

*The popitem() method of OrderedDict has a different signature.
 It accepts an optional argument to specify which item is popped.

*OrderedDict has a move_to_end() method to efficiently reposition an element to an endpoint.

###What is OrderedDict ?###
* It is a subclass of dict
* Ordered dictionaries are just like regular dictionaries but have some extra capabilities relating to ordering operations.

###creating OrderdDict###
example:1

 ##accessing items in OrderedDict

### OrderedDict methods ###
1) move_to_end(key,last=bool)
2) popitem(last=bool)

1) move_to_end(key,last=bool):
* we can reorder orderedDict using this method
*Move an existing key to either end of an ordered dictionary.
*The item is moved to the right end if last is true (the default) or to the beginning if last is false.
*Raises KeyError if the key does not exist:
example: 2

2)  popitem(last=bool):
The popitem() method for ordered dictionaries returns and removes a (key, value) pair.
The pairs are returned in LIFO order if last is true or FIFO order if false.
When we don’t pass an argument, last is assumed to be true.

5) defaultdict:
*Defaultdict is a container like dictionaries present in the module collections.
*Defaultdict is a sub-class of the dict class that returns a dictionary-like object.
*The functionality of both dictionaries and defualtdict are almost same except for the fact that defaultdict raises a KeyError if None or
 provides a default value for the key that does not exists if we pass default factory function(None,lambda,int,list).

##creating defaultdict##

defaultdict(default_factory):

* default_factory ---> A function returning the default value for the dictionary defined.
If this argument is absent then the dictionary raises a KeyError.

##how exactly defaultdict works##

* Defaultdict support the instance variable--->default_factory.
* Also it support a method ---> __missing__()


Method:
1)__missing__(): It uses the factory function.

*This method is called by the __getitem__() method of the dict class when the requested key is not found;
 whatever it returns or raises is then returned or raised by __getitem__().

* using int and list as a default_factory function


ChainMap object:

* It is an object of collections module.
* it is used to link multiple dictionaries as a single unit

*A ChainMap groups multiple dicts or other mappings together to create a single, updateable view.
If no maps are specified, a single empty dictionary is provided so that a new chain always has at least one mapping.

*Lookups search the underlying mappings successively until a key is found.
In contrast, writes, updates, and deletions only operate on the first mapping.

A ChainMap incorporates the underlying mappings by reference.
So, if one of the underlying mappings gets updated, those changes will be reflected in ChainMap.

How to construct ChainMap:
---> ChainMap(*maps) ---> ChainMap(dict1,dict2,.....dictn)

##accessing and updating ChainMap##

ChainMap attribute: maps
*A user updateable list of mappings. The list is ordered from first-searched to last-searched.
*It is the only stored state and can be modified to change which mappings are searched.
*The list should always contain at least one mapping.
ChainMap method: new_child()
*Returns a new ChainMap containing a new map followed by all of the maps in the current instance.
*This method is used for creating subcontexts that can be updated without altering values in any of the parent mappings.

ChainMap property: parents
*Property returning a new ChainMap containing all of the maps in the current instance except the first one.

'''
