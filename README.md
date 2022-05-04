#  The Renamer

## Documentation 
[Documentation](https://the-renamer.readthedocs.io/en/latest/) hosted on Read the Docs 

[Nice Implementation](https://rowlando13.medium.com/the-renamer-e7592d4baf2a) written on Medium

## What does The Renamer do?

The Renamer is used to rename entries in pandas dataframe. It first reads in a csv file that has codes, or already known names to support identification and renaming. It uses a dictionary, with zip and map to simplify the process.

## What does The Renamer do for me? 

It helps separate data from code to keep your code base small and makes it easier to work with renaming a lot entries since you can edit the ids.csv in a full featured editor like excel. It also makes renaming things more repeatable since you just put the csv containing the ids in your code base, import build_ids and renamer and go.

If you do exploratory data analysis a lot, then you probably already have a system. Keep it, and augment it with The Renamer, or better yet make a pull request, and I can integrate your system into The Renamer. 
