# Udacity Nano degrees
## Full Stack Web Developer

**Assignment:** 1 - Fresh Tomatoes Movie Trailers

**Autor:** Marco Olimpio - marco.olimpio [at] gmail

**Description:** This simple application bring a selected list of my 
favorites movies. There is also the possibility to play the trailers 
of the selected movies, just click over one of the posters displayed 
and have fun! 

This application is one of the assignments of Udacity's Full Stack Web 
Developer Nanodegree.

#### The structure 

---

We basically have only two folders:

- ***src*** - with the application code
- ***tests*** - the unit tests

In src folder there are three main files:
- **media.py:** Where we define the Movie class 
- **entertainment_center.py** Where we instantiate our list of movies 
and call the generate HTML method from the fresh_tomatoes.py
- **fresh_tomatoes.py:** Responsible to process a list of given movies 
(python array) and create a display HTML file.

 
#### How to execute

---

Simply execute the command

```python
$python3  enterteinment_center.py
``` 

it should generate the fresh_tomatoes.html and open your default browser. 
If a browser does not appear you should open a browser by yourself and open 
the file  ***fresh_tomatoes.html***. 


### Pylint and PEP-8

---
We executed the pylint and a interesting fact is that the original 
```fresh_tomatoes.py``` had some minor issues as shown next
![Pylint of the original fresh_tomatoes.py](/imgs/fresh_tomatoes_pylint_before.png "Pylint of the original fresh_tomatoes.py")

After some adjustments of the orginal code we could make 10/10 in all code
![Pylint of all modules](/imgs/pylint_all.png "Pylint of all modules")

We utilized PEP-8 online tool (http://pep8online.com/) to validade all modules as we can see next:
PEP-8 Media.py
![Ok for PEP-8 Media.py](/imgs/pep8_movie.png "Ok for PEP-8 Media.py")

PEP-8 entertainment_center.py
![Ok for PEP-8 entertainment_center.py](/imgs/pep8_entertainment.png "Ok for PEP-8 entertainment_center.py")

Unfortunatelly the ```fresh_tomatoes.py```was the only one to not meet the PEP-8 
PEP-8 fresh_tomatoes.py
![Not Ok for PEP-8 fresh_tomatoes.py](/imgs/pep8_fresh.png "Not Ok for PEP-8 fresh_tomatoes.py")

If you are interested in installing pylint it's necessary to install it using 
````pip install pylint````
command. After that, you should execute the linter like
```
$pylint my_file.py
```


## Unit testing


We also provided an unit test of the Movie model. We utilized **Pytest**. This is a white box test and we expceted
a exception to be raised for not valid URL for the poster URL as well as for trailers URLs.

If you want to be able to execute the tests as well, please install pytest with 
```
$pip install pytest
```
and, within the project folder, execute the tests as follows:
```
$pytest
```

As we can see we passed all the tests:
![All tests ok](/imgs/tests.png "All movie tests passed")
