# Basic Concepts

The goal of this guide is to explain in a high-level but useful way the core concepts of modern computing. This guide is aimed at those who have never interacted with software as more than an end-user of graphical applications, but who for whatever reason have a desire for more flexible and precise control over their computer and its software.

## Understanding the Filesystem

The most important thing to remember when doing any sort of programming is that every command is run in the context of some **location**. Your Desktop is a location. Your Documents folder is a location. Everything on your computer has a location, and locations are all relative. The whole thing is called a **filesystem**. Here is an illustration of the typical Mac OSX filesystem (Windows filesystems are fairly similar). Indentation implies nesting:

```
/
    Applications/
        Chess.app
        Rstudio.app
        iTunes.app
        ...
    System/
        Library/
    Users/
        Guest/
        Shared/
        <username>/
            Desktop/
                file.txt
            Documents/
            Downloads/
        ...
    bin/
        pwd
        ls
        chmod
        ...
    var/
        log/
        tmp/
        ...
    etc/
    ...

```

The key takeaway here is that every file in your computer has a location, and this location can be described by the full, or "absolute" path. For example, the text file on the desktop can be described in the following way:

```
/Users/<username>/Desktop/file.txt
```

No matter where you are in your computer, this path will always reference the same file. However, it would be tedius to have to type this verbose path every time you needed to reference a file. Most of the time, we refer to files via their "relative paths". But relative to what?

## Understanding the Command Line

Really, watch [the video](https://www.youtube.com/watch?v=tc4ROCJYbm0).

To understand the command line, it's valuable to first understand the various "layers" that make up a computer.

At the very bottom, there's the **hardware**: chips, memory, and electricity. These are the fruits of electrical engineering and can do simple things very, very quickly. Programming these these directly is very tedious. As a result, we wrap the hardware around a very core piece of software, known as a **kernel**. The kernel is software that controls the hardware and the basic resources (CPU power, memory) of the computer. To get the computer to do things, we talk to the kernel. Note how the problem is computing got a little bit simpler.

For many people, interactions with a computer takes place via a graphical user interface, otherwise known as a "GUI". Icons on your desktop, double-clicks, drag-and-drop -- all of these are GUI operations. The GUI is a program, like any other, which puts things on the screen and interprets keystrokes and trackpad activity. The GUI talks to the kernel and turns your clicks and keystrokes into actions.

A GUI is a very sophisticated program, and GUI-based computers have been around only for the last twenty or so years. Before graphical interfaces were popular (or even possible), computing took place via a much simpler interface. That interface was known as the **command line**, otherwise known as the **shell**.

Why shell? Because the shell was a program that *wrapped around* (get it?) the kernel and provided a convenient way to run commands. A shell is also a program, much simpler than a GUI, which provides a text-based user interface.

Why would someone use a shell over a more user-friendly GUI? Principally, for control. The primary drawback of a GUI is that it can only do what it was programmed to do. It is very hard to program a GUI, and the interfaces popular on modern computers are virtually impossible to modify. A shell, on the other hand, is a simple program that can do almost anything. If a GUI is intuitive but inflexible, a command line is less intuitive (at first), but extremeley powerful and flexible. For programmers, data scientists, and others for whom work involves the organization and manipulation of information, this power and flexibility is crucial. This is why people use the command line.

## Working with the shell

A shell is just a program. There are many of them. On Mac OSX, the default is the "[bash shell](https://en.wikipedia.org/wiki/Bash_(Unix_shell))". On Windows, there is [PowerShell](https://en.wikipedia.org/wiki/Windows_PowerShell). On OSX, you can open a bash shell by opening the "Terminal" application. On Windows, there is a PowerShell application.

Firing up the shell will bring you to a boring-looking screen which looks something like this:

```
Hi! Welcome to the shell!

$
```

Not much to look at. You type some things and hit enter. Something happens. Rinse and repeat until your computer crashes or you're a billionare. Things get more interesting when you realize that every command you type into the shell looks like the following:

```
Hi! Welcome to the shell!

$ <program> <arguments>
```

There is always one program, and an arbitrary number of arguments. This is how every command works. Your computer comes with several dozen built-in programs, which do very simple but useful things. We will review them shortly. First, however, we must discuss the concept of a "working directory".

Recall that any file can be fully described by it's absolute path. When interacting with files (a common activity), you could in theory specify the full path of every file. This would be extremely tedious, especially given that, for any given task, related files are generally close together. In OSX and Windows, there are the Finder and Explorer programs for browsing through folders. These programs are GUIs accomplishing the same goal.

The **working directory** is your shell's current "location" inside the filesystem. You can "navigate" the filesystem by running commands which cause the shell to move up or down directory hierarchies. This is analagous to double-clicking on a folder on your desktop.

When you are in a directory, every file argument is evaluated as though the current working directory were prepended to the argument. Let's see an example:

```
/$ python dir1/file1.py
'Hello world'

/$ cd dir1
/dir1$ python file1.py
'Hello world'

/dir1$ cd ..
/$ python file1.py
usr/bin/python: can't open file 'file1.py': [Errno 2] No such file or directory
```

Here, we saw two programs run on three arguments.

1. First, we ran the `python` program on argument `dir/file1.py`, a python file.
2. Then, we ran the `cd` (change directory) program on argument `dir1`, also a file (in Unix, [everything is a file](https://en.wikipedia.org/wiki/Everything_is_a_file), even a directory.) Note how the command prompt changes to reflect the fact that we moved through the filesystem.
3. We ran the `python` program on argument `file1.py`, the same python file.
4. We ran the `cd` program on `..`, representing the current *parent directory*.
5. We ran the `python` program on argument `file1.py`, but received an error, because there is no such file in our current location.

Hopefully this example will illustrate the nature of using a shell to navigate and executing commands in a filesystem.

## Command Reference
### for Linux-style command line interfaces

Note that in this program reference, filenames and directories can be given as either absolute or relative paths.

`pwd` -- print working directory

`ls` -- list files in current directory

`touch <filename>` -- makes a new file

`rm <filename>` -- delete a file

`cd <directory>` -- change current directory to `<directory>`

`python <filename>.py` -- run a Python file

`mkdir <directory>` -- create a new directory

`rmdir <directory>` -- delete a directory

`mv <filename1> <filename2>` -- move `<filename1>` to `<filename2>`

`cp <filename1> <filename2>` -- copy `<filename1>` to `<filename2>`

`cat <filename>` -- print the entire file to the screen

`head <filename>` -- print the first few lines of a file to the screen

`tail <filename>` -- print the last few lines of a file to the screen

`man <program>` -- show additional information about the program

`echo <string>` -- print `<string>` to the screen (as in, a string of letters)

`ps` -- print information about currently-running processes (instances of programs)

Note that programs often accept additional optional arguments. Consider:

`tail -n 20 <filename>` -- print the last 20 lines of a file to the screen

`ls -lah` -- list files in current directory in a super easy-to-read format

`ps -aux` -- print a lot of information about currently-running processes

`kill <integer>` -- kill the process with process id `<integer>`

## Standard Input, Standard Output, Processes

By default, every program takes input from one place, Standard Input (`stdin`), and sends output to one place, Standard Output (`stdout`). In general, `stdin` is the keyboard/trackbad. `Stdout` is the screen. A surprisingly large amount of programming boils down to routing the output of one program into the input of another.

When you execute a command in the shell, the program "takes control" of the terminal while it is running. When it finishes, it returns control of the shell. While the programming is running, it may request input from standard in (such as asking for a password). It may also send output to standard out (for example, informing you about the program's progress).

A **process** is an instance of a running program. To think of it another way, a program is just a bunch of zeroes and ones inside of memory. A process is that program being executed in a million steps on the computer's CPU. The same program can be run as many processes. They fundamental rule about computers is that processes aren't allowed to mess with each other's memory. The kernel makes sure of this (remember the kernel?).

It is possible to "background" a process, which simply means that you don't let that process take control of your shell. This lets you type in more commands while the process is running. At times this behavior may be desirable. On Unix-like systems (Linux, OSX), you can background a process using the ampersand, like this:

```
/$ <program> <arg1> <arg2> &
```

## Debugging Error Messages

Debugging is a large topic. Here we will discuss the most important principal for debugging anything. That principal is: **simplify and isolate the problem.**

Software systems are complex, with many moving parts. Managing this complexity is a big part of software engineering. When trying to fix something, the best way to do it is to isolate the problem.

Imagine you are building an app that streams data from the internet, parses it, and loads it into a custom GUI. The app is currently broken. At this point in time, the problem could be with the internet, the parser, or the GUI. Your first job is to figure out where the problem is. This means isolation. Some things to consider:

1. Replacing streaming data with static dummy data
2. Feeding the GUI static dummy data
3. Testing the parser on dummy data

By testing each of these pieces in a controlled environment, it becomes possible to find and fix problems. There are many tools to help in this process (debuggers being a major one). If these tools are not available to you, then a sure-fire approach is to cut away and simplify your program as much as possible until it works, and then carefully rebuild from there.

Please read your error messages. They are in words and they mean things. If you read them they will usually tell you what the problem is so you can fix it. This is true a surprising amount of the time.

Reading error messages is intimidating at first, but will become easier over time as you develop a better sense of *what* kinds of things tend to go wrong, as well as what information error messages are able to convey.

If you see an error message that you don't understand, do the following:

1. Copy the error
2. Paste it into a Google searchbar
3. Look over the top couple of answers

This will work extremely frequently. [StackOverflow](http://stackoverflow.com/) deserves much thanks for this.

## A Kitchen Metaphor

As a former student of the controversial linguist [George Lakoff](https://en.wikipedia.org/wiki/George_Lakoff), it would be bad form not to include at least one grand metaphor to attempt to place these ideas in comfortable order.

Think of your computer as a professional kitchen. Imagine shelves of recipe books, each containing many instructions for how to make certain dishes. Imagine teams of chefs and sous-chefs, working away at various dishes. Raw ingredients are transformed into delicious meals. The resources consumed -- gas for the oven, water for the sink, are accessed via oven ranges and sink spouts.

The recipes are programs -- they sit idle until some chefs are asked to prepare them. The actual cooking of a dish is a process -- in which the kitchen's resources are organized and devoted to preparing a dish. Ingredients and dishes are files -- the objects on which we operate. The ovens and sinks are the kernel -- the interface abstracting away the underlying resources, making them easier to work with.

You can have a million recipes, but only cook two dishes. You can have five recipes, but make each one a thousand times. You can cook one dish at a time, and leave most of your resources unused, or turn on every single oven.

The owner of the restaraunt is [Sudo](https://en.wikipedia.org/wiki/Sudo) -- able to overrule even the head chef, and set whatever rules she wants.

## Git and GitHub

The last topic in this guide is Git. Git not related to the command line per se, but rather is an important tool for the development of software. In many fields, but most of all in software, version matters. Software products are in constant states of change. Software projects almost always require the collaboration of multiple people. Managing all of this activity can be challenging. Enter Git.

Git is a tool for recording change over time, making it easier for people working on software to make sure they both have the correct and up-to-date version of their code, but also to be able to go back and see where and why changes were made. Known as source control, this bookkeeping is now fundamental in modern software development.

The core unit of Git is the **repository**. A repository can be thought of as unit being remembered. Work on repositories are saved in chunks known as **commits**. A commit can be thought of as a unit of memory. Developing software is then a process of committing changes to a repository representing the software project.

Some benefits of using Git:

1. Easy to restore files if they have been lost or damaged
2. Easy to get changes to files or folders without having to re-download the entire file or folder

There are more, but these two are so useful that rather than enumerate them it may be best to pause and reflect on these instead. Git, like many things, is a program.

GitHub, on the other hand, is a website which makes it easy to collaborate with others via the internet. GitHub uses Git as a foundation, and builds on it. This distinction is subtle but worth knowing.

Using Git involves understanding a handful of commands. Here are most of them:

`git clone <url to repo>` -- clone a repository from GitHub to your computer
`git add .` -- prepare files for the next commit
`git commit -am "<commit message>"` -- make a commit, with the message `<commit message>`
`git push` -- "push" new changes up to GitHub
`git pull` -- "pull" new changes from GitHub

To get started:

1. [Make a GitHub Account](https://github.com/). Everyone who writes programs for anything has one. It's like having an email address. If you don't have one people will think you're weird and won't hire you.
2. [Install Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git). You can install just the command-line program or the fancy GUI.

For this class, it is strongly advised that you also:

3. "Fork" the course repository. What this basically means is that you're going to copy the course repository to your own account.
4. Clone the forked repository to your computer.
5. Point RStudio's "Default Working Directory" to the course repository.
6. Avoid approximately half of your classmate's problems.
