# AirBnB_clone 
![Flowchart](https://imgur.com/xuoucfD.png)
 Built in python3, this project emulates the functioning of the AirBnB website.
 This version is called The Holberton B&B, and it is a project for [Holberton School Medellín](https://www.holbertonschool.com/co/campus_life/medellin).
 
## Flowchart
We will develop the backend as well as the frontend part of the website. Here is a diagram of the project and a hint of the technologies we used.
 
 ![Flowchart](https://imgur.com/3rCP5Fx.png)
 
 ## The Console
 There is a built-in command line interpreter (console) that provides a way to interact with the Storage-engine.
 
 Thru the console is possible to: 
* Create a new object (ex: a new User or a new Place)
* Retrieve an object from a file, a database etc…
* Do operations on objects (count, compute stats, etc…)
* Update attributes of an object
* Destroy an object

#### Usage

To launch the console application in interactive mode simply run:

```console.py ```

or to use the non-interactive mode run:

```echo "your-command-goes-here" | ./console.py ```

#### Commands

Commands | Description | Usage
-------- | ----------- |-------- |
**help** or **?**| Displays the documented commands. | **help**
**quit**     | Exits the program. | **quit**
**EOF**      | Ends the program. Used when files are passed into the program. | N/A
**create**  | Creates a new instance of the \<class_name\>. Creates a Json file with the object representation. and prints the id of created object. | **create** \<class_name\>
**show**    | Prints the string representation of an instance based on the class name and id. | **show** \<class_name class_id\>
**destroy** | Deletes and instance base on the class name and id. | **destroy** \<class_name class_id\>
**all** | Prints all string representation of all instances based or not on the class name | **all** or **all** \<class_name class_id\>
**update** | Updates an instance based on the class name and id by adding or updating attribute | **update** \<class_name class_id key value\>

## Tests

If you wish to run at the test for this application all of the test are located
under the **test/** folder and can execute all of them by simply running:

```python3 -m unittest discover tests ```

from the root directory.