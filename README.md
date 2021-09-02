# The Renamer

## Full documentation 


## What does The Renamer do?

The Renamer is used to rename entries in pandas dataframe. It first reads in a csv file that has codes, or already known names to support identification and renaming. It uses a dictionary, with zip and map to simplify the process.

## What does The Renamer do for me? 

It helps separate data from code to keep your code base small and makes it easier to work with renaming a lot entries since you can edit the ids.csv in a full featured editor like excel. It also makes renaming things more repeatable since you just put the csv containing the ids in your code base, import build_ids and renamer and go.

If you do exploratory data analysis a lot, then you probably already have a system. Keep it, and augment it with The Renamer, or better yet make a pull request, and I can integrate your system into The Renamer. 

## Special Notes

The file used to contain the codes and known names is a csv file. Excel generally does well with csv files; however, it has a nasty habit of converting 0230 to an integer then 230 when you open the file by double clicking it. To get around this, open Excel first and use Excel to open the file. By default it will give you an option to pick the deliminator and assign the text type to each column.
