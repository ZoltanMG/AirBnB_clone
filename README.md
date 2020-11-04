# :notebook_with_decorative_cover: AirBnB clone - The console :sunrise:

<p align="center">
  <img src="https://user-images.githubusercontent.com/66263776/97637714-299b3f00-1a09-11eb-824d-23b81263f96c.png" width="500" height= "200">
</p>

**AirBnB** is a website that you can find option about places that you can travel. In this project we are going to deploy a simple copy of the [AirBnB website](https://www.airbnb.com.co/?_set_bev_on_new_domain=1603810323_whaprsZfQ18Pr9Cb "Website").That Divided diferent step like:
* The Console
* Web Static
* MySQL storage
* Web Framework - templating
* RESTful API
* Web dynamic

<p align="center">
  <img src="https://user-images.githubusercontent.com/66263776/98057530-81261a00-1e10-11eb-9197-a5eb38a64be5.png" width="400" height= "200">
</p>

However in this repository we are going to show the first part of this project  that is **The console**

## :gem: Description of the project :gem: 
### The console
<p align="center">
  <img src="https://user-images.githubusercontent.com/66263776/97640151-28204580-1a0e-11eb-9e21-888830a67f3e.png" width="400" height= "200">
</p>

This first part **the console** about **AirBnB** is a command interpreter similar to a Linux shell but limited to a specific use-case; 

This part can be work  in two diferent mode:

#### Interactive mode
In this **Interactive** mode the console will display a prompt (hbnb), what it indicate is that user can write and execute a command. You need to run the the file ***./console.py***. and if you like exit of this place you need to write ***quit*** in the prompt.
```
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$
```
#### Non-Interactive mode
In this **Non-Interactive** mode the console will desplay a prompt (hbnb) but you need to be run with a command input piped into its execution so that the command is run as soon as the console starts. In this mode no prompt will appear, and no further input will be expected from the user.
```
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
```
### :man_technologist: Arquitecture of the project :man_technologist:
This proyect was realized  by instruction set:
1) The first step 
2)
4) **Test** : It was realized to ensure that the program function, all files, classes, functions was tested with [unit_tests](https://docs.python.org/3.4/library/unittest.html#module-unittest "Unitest")

### :eight_spoked_asterisk: Command :eight_spoked_asterisk:
| Command | Usage |Description |
| :---: | :---: |:---: |
| quit *or* EOF |  | Exits the program |
| Help | help **<command\>** | Provides a text describing how to use a command. |
| Created | **<class name\>** |  create an object of the class declared by user; |
| Show | show **<class name\> <id\>** |  create an object of the class declared by user; |
| Updated | <class name\> <id\> <attribute name\> <attribute value\> |  create an object of the class declared by user; |

## :gem: Description of the command interpreter :gem:

### Getting Started

#### Installing
You will need to clone the repository of the project from Github. This will contain the simple shell program and all of its dependencies.
>user@ubuntu$ git clone https://github.com/CBarreiro96/AirBnB_clone

After you have cloned the repository, you are going to find a folder called AirBnB_clone. In this folder you find several file that these allow the program to work.

The first step that you need to do is:
>user@ubuntu$ **cd AirBnB/**
>
>user@ubuntu:~/AirBnB$ **ls**

In this file you find these files:

####  File description.
| File | Description |
| :---: | :---: |
| [AUTHORS](https://github.com/CBarreiro96/AirBnB_clone/blob/main/AUTHORS "Authors of Project") | Contain of Authors of this project |
| [models/base_models.py](https://github.com/CBarreiro96/AirBnB_clone/blob/main/models/base_model.py "base_models") | Class that defines all common attributes/methods for other classes. |
|[models/__ init __.py:](https://github.com/CBarreiro96/AirBnB_clone/blob/main/models/__init__.py "Init") | In this file you can find code about convert to integer to binary |
|[models/engine/file_storage.py](https://github.com/CBarreiro96/AirBnB_clone/blob/main/models/engine/file_storage.py "File_storage") | Class that serializes instances to a JSON file and deserializes JSON file to instances |
| [models/amenity.py](https://github.com/CBarreiro96/AirBnB_clone/blob/main/models/amenity.py "File amenity") | Amenity class inheriting from BaseModel |
| [models/city](https://github.com/CBarreiro96/AirBnB_clone/blob/main/models/city.py "File city") | City class inheriting from BaseModel |
| [models/place.py](https://github.com/CBarreiro96/AirBnB_clone/blob/main/models/place.py "File place") | Place class inheriting from BaseModel |
| [models/review.py](https://github.com/CBarreiro96/AirBnB_clone/blob/main/models/review.py "File review") | Review class inheriting from BaseModel |
| [models/user.py](https://github.com/CBarreiro96/AirBnB_clone/blob/main/models/user.py "File user") | User inheriting from BaseModel |
| [tests](https://github.com/CBarreiro96/AirBnB_clone/blob/main/models/user.py "File user") | This is a directory that you can find all tests did in this proyect |
### Uses of Console
In this section, you are going to learn How can you do this proyect?, so you can use this project of two way: Interactive mode or Non interactive mode, If you would like use interactive mode you have to write ```./console.py```, but if you would like to use Non interactive you have to write ```echo "<command>" | ./console.py``` 
The first time you don't have anything store in the console, if you put the command all after you start console, It doesn't print anything.
```
user@ubuntu::~/AirBnB$ ./console.py
(hbn)all
[]
(hbn)
```
Now, we are going to create 

## Build with
```
Ubuntu , Emacs and python3 language
```
## AUTHORS
* Zoltan Mora [ZoltanMG](https://github.com/ZoltanMG "User Github")
* Camilo Barreiro [CBarreiro96](https://github.com/CBarreiro96 "User Github")
