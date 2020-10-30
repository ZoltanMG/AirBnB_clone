# :notebook_with_decorative_cover: AirBnB clone - The console :sunrise:

<p align="center">
  <img src="https://user-images.githubusercontent.com/66263776/97637714-299b3f00-1a09-11eb-824d-23b81263f96c.png" width="500" height= "200">
</p>

**AirBnB** is a website that you can find option about places that you can travel. In this project we are going to deploy a simple copy of the [AirBnB website](https://www.airbnb.com.co/?_set_bev_on_new_domain=1603810323_whaprsZfQ18Pr9Cb).That Divided diferent step like:
* The Console
* Web Static
* MySQL storage
* Web Framework - templating
* RESTful API
* Web dynamic

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

## :gem: Description of the command interpreter :gem:

### Getting Started

#### Installing
You will need to clone the repository of the project from Github. This will contain the simple shell program and all of its dependencies.
>$ git clone https://github.com/CBarreiro96/AirBnB_clone

After you have cloned the repository, you are going to find a folder called AirBnB_clone. In this folder you find several file that these allow the program to work.
####  File description.
| File | Description |
| :---: | :---: |
| [AUTHORS]() | Contain of Authors of this project |
| [models/base_models.py]() | Class that defines all common attributes/methods for other classes. |
|[models/__ init __.py:]() | In this file you can find code about convert to integer to binary |
|[models/engine/file_storage.py]() | Class that serializes instances to a JSON file and deserializes JSON file to instances |
| [_putchar.c](https://github.com/CBarreiro96/printf/blob/master/_putchar.c "Printable Tools") | Contains the function to printf byte to byte (**write**) |
| [man_3_printf](https://github.com/CBarreiro96/printf/blob/master/man_3_printf "Description") | It contain to description about printf |

## Build with
```
Ubuntu , Emacs and python3 language
```
## AUTHORS
* Zoltan Mora [ZoltanMG](https://github.com/ZoltanMG "User Github")
* Camilo Barreiro [CBarreiro96](https://github.com/CBarreiro96 "User Github")
