.. toctree::
   :maxdepth: 2
   :caption: Contents:

Welcome!
=======================================

This project is ongoing. If you have a problem, please open an issue on the github page. If you would like to add functionality, then open an issue and we can discuss it. 

`Github Page <https://github.com/Rowlando13/the_renamer>`_ 

About The Renamer
=================
What does The Renamer do?

The Renamer is used to rename entries in pandas dataframe. It first reads in a csv file that has codes, or already known names to support identification and renaming. It uses a dictionary, with zip and map to simplify the process.

What does The Renamer do for me? 

It helps separate data from code to keep your code base small and makes it easier to work with renaming a lot entries since you can edit the ids.csv in a full featured editor like excel. It also makes renaming things more repeatable since you just put the csv containing the ids in your code base, import build_ids and renamer and go.

If you do exploratory data analysis a lot, then you probably already have a system. Keep it, and augment it with The Renamer, or better yet make a pull request, and I can integrate your system. 

Notes
=====
To see a nice implementation, go to my `Medium Article <url>`_ .

Excel Usage 

The file used to contain the codes and known names is a csv file. Excel generally does well with csv files; however, it has a nasty habit of converting 0230 to an integer then 230 when you open the file by double clicking it. To get around this, open Excel first and use Excel to open the file. By default it will give you an option to pick the deliminator and assign the text type to each column. 

Test Coverage 

There is pretty good test coverage, but I use some 2 mb files to test it, so the tests are in the 'test-master' branch.  If you are having an issue, the first thing, I will ask you to do is clone the most recent 'test-master' branch, run the tests, and then send me a screen shot.

`Github Test-Master Branch <https://github.com/Rowlando13/the_renamer/tree/test-master>`_

Best Way to Use 
===============
Currentely, the best way to use The Renamer is by cloning the master branch and placing the_renamer.py and ids.csv in your working directory. The code is well thought out, but I did not want to clutter PyPI since it is only ~200 lines. If there is enough desire, then I am happy to. 

`Github Master Branch <https://github.com/Rowlando13/the_renamer/tree/master>`_

Functions
=========
.. autofunction:: the_renamer.build_ids

.. autofunction:: the_renamer.renamer 

IDs.csv
=======
This just a normal csv file with a few rules: 
   #. In the second row of each column you must have 'destination', 'one', or 'many'. 
   #. You can only have one 'destination' column. You can have arbitrarily many 'one' or 'many' columns. The columns can be arbitrarily long. 
   #. The entries in the 'destination' or 'one' column can be any type, but the 'many' columns entries must be str type.


