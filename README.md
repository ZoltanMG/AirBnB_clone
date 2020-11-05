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

This first part **the console** about **AirBnB** is a command interpreter similar to a Linux shell but this console his functions are:
1) **Create** neww object(ex: new city, new user erc..)
2) **Show** an object
3) **Update** atributes of an object
4) **Deestroy** an object  

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
**Test** : It was realized to ensure that the program function, all files, classes, functions was tested with [unit_tests](https://docs.python.org/3.4/library/unittest.html#module-unittest "Unitest")

### :eight_spoked_asterisk: Command :eight_spoked_asterisk:
| Command | Usage |Description |
| :---: | :---: |:---: |
| quit *or* EOF |  | Exits the program |
| Help | help **<command\>** | Provides a text describing how to use a command. |
| Created | create **<class name\>** |  create an object of the class declared by user; |
| Show | show **<class name\> <id\>** | Prints the string representation of an instance based on the class name and id  |
| Updated | update<class name\> <id\> <attribute name\> <attribute value\> |  Updates an instance based on the class name and id by adding or updating attribute (saves the changes into a JSON file). |
| all | all <class name\> |  Prints all string representation of all instances based on the class name. |
| Destroy | destroy <class name\> <id\>  | Deletes an instance based on the class name and id . |

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

#### Interactive mode

```
user@ubuntu::~/AirBnB$ ./console.py
(hbn) all
[]
(hbn)
```
Now, we are going to start with the command  ***create***   In this command you created diferent classes that this project have in the files like these:

* BaseModel ------- (```Class```)
* City ----------------- (```Inherited class from base models```)
* Place ----------------- (```Inherited class from base models```)
* Amenity ----------------- (```Inherited class from base models```)
* State ----------------- (```Inherited class from base models```)
* Review ----------------- (```Inherited class from base models```)


--- ```Public instance atributes``` ---
  * id
  * created
  * updated

 
```
(hbn) created BaseModel
8ab395d2-ad4e-4fad-b9b1-82bb4ae274be
(hbn) all
["[BaseModel] (8ab395d2-ad4e-4fad-b9b1-82bb4ae274be) {'id': '8ab395d2-ad4e-4fad-b9b1-82bb4ae274be', 'created_at': datetime.datetime(2020, 11, 4, 19, 0, 4, 478376), 'updated_at': datetime.datetime(2020, 11, 4, 19, 0, 4, 478419)}"]
(hbn)
(hbn) create City
2c14dea2-8c1d-4349-b969-81f05a0d9faa
(hbn) all
["[BaseModel] (1345c546-ad7c-42d7-a019-86b0ddc42b48){'id':'1345c546-ad7c-42d7-a019-86b0ddc42b48', 'created_at': datetime.datetime(2020, 11, 4, 22, 12, 36, 875690), 'updated_at': datetime.datetime(2020, 11,4, 22, 12, 36, 875730)}","[City](2c14dea2-8c1d-4349-b969-81f05a0d9faa){'id':'2c14dea2-8c1d-4349-b969-81f05a0d9faa', 'created_at': datetime.datetime(2020, 11, 4, 22, 12, 58, 815023), 'updated_at': datetime.datetime(2020, 11, 4, 22, 12, 58, 815072)}"]
```
As you can see, when we write *create BaseModel* you are going to create objects type of class that It store in the file file.jason, so you can create all class of this proyect and It store in this file. 
On the other hand you can modify this Public atribute of this object typle class with the command **update**, in the next example you can find how you can use this.
In this example we are going to change  the id of BaseModel
```
(hbnb) all BaseModel
["[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'id': '49faff9a-6318-451f-87b6-910505c55907', 'updated_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903300)}"]
(hbnb) update BaseModel 49faff9a-6318-451f-87b6-910505c55907 first_name "Betty"
(hbnb) show BaseModel 49faff9a-6318-451f-87b6-910505c55907
[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'first_name': 'Betty', 'id': '49faff9a-6318-451f-87b6-910505c55907', 'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'updated_at': datetime.datetime(2017, 10, 2, 3, 11, 3, 49401)}
```

### Non interactive mode
```
user@ubuntu:~/AirBnB$ echo "create BaseModel" | ./console.py
(hbnb)
49faff9a-6318-451f-87b6-910505c55907
(hbnb) 
user@ubuntu:~/AirBnB$

user@ubuntu:~/AirBnB$ echo "all BaseModel" | ./console.py
(hbnb)
["[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'id': '49faff9a-6318-451f-87b6-910505c55907', 'updated_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903300)}"]
(hbnb) 
user@ubuntu:~/AirBnB$

user@ubuntu:~/AirBnB$ echo "show BaseModel 49faff9a-6318-451f-87b6-910505c55907" | ./console.py
(hbnb)
[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'id': '49faff9a-6318-451f-87b6-910505c55907', 'updated_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903300)}(hbnb) 
user@ubuntu:~/AirBnB$

user@ubuntu:~/AirBnB$ echo "update BaseModel 49faff9a-6318-451f-87b6-910505c55907 first_name "Betty"" | ./console.py
(hbnb)
(hbnb) 
user@ubuntu:~/AirBnB$
```

## Build with
```
Ubuntu , Emacs and python3 language
```
## AUTHORS
* Zoltan Mora [ZoltanMG](https://github.com/ZoltanMG "User Github")
* Camilo Barreiro [CBarreiro96](https://github.com/CBarreiro96 "User Github")
