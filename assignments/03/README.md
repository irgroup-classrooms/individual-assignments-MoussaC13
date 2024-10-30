# Version Control Software

## Getting started with branching and merging, making a first commit

1. Please visit [git visualization tool](https://git-school.github.io/visualizing-git/). Create at least 5 commits, branches and tags there and watch the graph grow. (Hint: Typing help will show you all the available commands.)
2. Make a screenshot of your work when you’re finished. Give the screenshot a reasonable filename, for example `git-graph.png`.
3. Clone your own (this) repository into your local file system. 
4. Save the screenshot on your machine to this working directory.
5. On the command line:
  * navigate to the repository 
  * check your git status.
  * add the new file to git
  * and commit the change.
  * Finally, push your changes to the remote repository.
6. Visit your repository on GitHub to verify that your new file is present. 

## Committing your progress step-by-step

1. Download the following file https://librarycarpentry.org/lc-shell/data/shell-lesson.zip For instance, with 

```
wget https://librarycarpentry.org/lc-shell/data/shell-lesson.zip
```

2. Unzip it 

```
unzip shell-lesson
```

(Of course, you can also do it with the GUI, but it won't hurt to try out the CLI)

Make sure not to commit these files to the repository. **Note:** You can also add a `.gitignore` file and add the folder and file paths there.

In the following, create a bash script and the commands to get the desired answers to the tasks below. After successfully completing a single task, i.e., writing the correct command, commit your changes and push them to the repository. Try to include branches and solve merge conflicts if they should occur. _tl;dr_ Do task, commit changes, do next task, commit changes, and so on ...

**Note:** The objective of this assignment is getting familiar with the use of Git and GitHub, and also to get more experience with the command line interface in general. Some topics and contents of last week's lecture will come in handy, when solving the tasks. 

1. How do you get the first three lines of the file `2014-01_JA.tsv`?
2. How do you get the total number of lines in each of the `*.tsv`files?
3. How do you get the file with the highest number of lines and how many does it have? Can you get the output with a single command line call? 

Once, you have solved the quiz and came up with a reasonable command line call. Add it to your bash script, stage the changes, write a reasonable commit message, and push the changes. Then go on with the next task and repeat.
