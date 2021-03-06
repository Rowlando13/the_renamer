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
To see a nice implementation, go to my `Medium Article <https://rowlando13.medium.com/the-renamer-e7592d4baf2a>`_ .

Excel Usage 

The file used to contain the codes and known names is a csv file. Excel generally does well with csv files; however, it has a nasty habit of converting 0230 to an integer then 230 when you open the file by double clicking it. To get around this, open Excel first and use Excel to open the file. By default it will give you an option to pick the deliminator and assign the text type to each column. 

Best Way to Use 
===============
Currently, the best way to use The Renamer is by cloning the master branch and placing the_renamer.py and ids.csv in your working directory. The code is well thought out, but I did not want to clutter PyPI since it is only ~200 lines. If there is enough desire, then I am happy to. 

`Github Master Branch <https://github.com/Rowlando13/the_renamer/tree/master>`_

Functions
=========
.. autofunction:: the_renamer.build_ids

.. autofunction:: the_renamer.renamer 

IDs.csv
=======
This just a normal csv file with a few rules: 
   #. Row 1, enter the names of the columns. The names are for your own book keeping. They don't appear anywhere else. They must be unique within row 1.
   #. Row 2, enter you must have 'destination', 'one', or 'many' based on the type of column. 

      * 'Destination' type columns contain the desired name. 
      * 'One' type columns contains only single entries.
      * 'Many' type columns contain multiple entries separated by a comma.

   #. You can only have one 'destination' column. You can have arbitrarily many 'one' or 'many' columns. The columns can be arbitrarily long. 
   #. The entries in the 'destination' or 'one' column can be any type, but the 'many' columns entries must be str type. 
   #. No entries can be blank. If no value is desired, use '<NONE>'. If the value of '<NONE>' is desired you change this by updating the 'none_value' variable at the top of the_renamer.py.

US States Example ids.csv

(displayed as if editing in Excel or Google sheets)

=============  ===========  ====================================================
desired        most_common  all      
=============  ===========  ====================================================
destination    single       many
AL             Alabama      alabama, ALABAMA, Alabama, BAMA
AK             <NONE>       Arkansas, arkansas, ARKANSAS, The Other Kansas
AZ             Arizona      Arizona, arizona, ARIZONA
...            ...          ...
=============  ===========  ====================================================

Test Coverage 
==============
There is pretty good test coverage. If you are having an issue, the first thing I will ask you to do is clone the most recent 'master' branch, run the tests, and then send me a screen shot.

`Github Master Branch <https://github.com/Rowlando13/the_renamer/tree/master>`_

.. autoclass:: test_the_renamer.TestRenamer
   :members:


