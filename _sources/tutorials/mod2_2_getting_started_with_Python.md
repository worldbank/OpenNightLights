# Getting started with Python (10 min)
## Intro to Python

<div class="alert alert-success">
<a href="https://www.python.org/" class="alert-link">Python</a> is a popular programming language for data science.
</div>

This tutorial uses Python and assumes that you have at least some familiarity with it.

Python is one of the most popular programming languages for a number of reasons:
- It’s open-source
- It has a large standard library and a massive (and growing!) ecosystem of packages (collections of code), including those used for scientific computing
- It’s user-friendly
- It has a large and active online community for knowledge-sharing and trouble-shooting when you get stuck
- It’s a general-purpose language...this is helpful for data science work, which often covers a wide range of tasks

<div class="alert alert-success">
If you are completely new to programming, you’ll first want to get started with <a href="https://wiki.python.org/moin/BeginnersGuide/NonProgrammers" class="alert-link"> this Beginner's Guide for Non-Programmers.</a>
</div>

<div class="alert alert-success">
If you are a programmer who is new to Python, <a href="https://wiki.python.org/moin/BeginnersGuide/Programmers" class="alert-link">this Beginner's Guide for Programmers</a> may help.
</div>

<div class="alert alert-success">
<a href="https://github.com/openlists/PythonResources" class="alert-link">Here’s another large list of resources for Python</a> assembled by that community we talked about.
</div>


## Installing Python

There are many ways to install and manage Python, in fact most Linux and UNIX-based computers already have it as a system install.

This tutorial requires Python 3.7+. So if you do not already have that you will want to install it on your computer. Even if you already have Python 3.7, it is recommended that you set up a virtual environment for this tutorial (as with any project). See below for how to do that.

## Package management
We mentioned that large and growing ecosystem of Python packages, which really makes this a powerful language. Thanks to these open-source packages, many tasks we’ll conduct in this tutorial will use code already written for the task, so you don’t have to write out the source code from scratch.

However, these packages often depend on each other in various ways and are updated frequently. If you didn’t have a way to manage packages and dependencies, things might break and it becomes a frustrating experience. Fortunately,there are package managers available for this.

If you’ve used Python, you’re familiar with pip.

<div class="alert alert-success">
    <b>pip</b> is a utility for installing Python packages contained in the Python Package Index (PyPI), a repository containing packages people have written in Python.
</div>

There is also conda, a popular package management platform among data scientists.

<div class="alert alert-success">
<a href="https://conda.io/en/latest/">Conda (distributed by Anaconda)</a> is an open source package management system and environment management system that runs on Windows, macOS and Linux.
</div>

The Anaconda website provides <a href="https://www.anaconda.com/blog/understanding-conda-and-pip">a helpful description of conda and its comparison to pip</a>. 

In summary: using conda can make things more streamlined, but there are some constraints, particularly if the Python package you need is not in the conda repository or if you are building your own packages in Python...but if that's the case you are not reading a "how to install Python" tutorial..so you can skip this section. Conda also manages virtual environments, which simplifies things for us.

We will use conda in this tutorial; however, you are free to manage dependencies any way you wish of course. If you use pip, just adjust accordingly where you see the instructions say `conda install`.


### Installing conda

Conda can be installed for Windows, macOS, or Linux:
- <a href="https://docs.anaconda.com/anaconda/install/windows/">Installing conda for Windows</a>
- <a href="https://docs.anaconda.com/anaconda/install/mac-os/">Installing conda for macOS</a>
- <a href="https://docs.anaconda.com/anaconda/install/linux/">Installing conda for Linux</a>

Follow the instructions relevant to your operating system and install conda on your computer.

### Managing environments

<div class="alert alert-success">
<a href="https://docs.anaconda.com/anaconda/user-guide/getting-started/">Getting started with conda</a> provides helpful documentation for getting things set up. We will touch on the highlights here, but this resource has more details.</div>

After you have successfully installed conda you can set up your environment and install packages. There are instructions how to use the GUI navigation tool, but for simplicity sake here, we are just going to use the command line. Open a command line or terminal window on your computer. The `$` will indicate a command line interface (CLI) prompt.

Confirm that you have conda install correctly, a version will be printed:
`$ conda --version`

Create an environment for this project. We'll call it "onl" but you can name it whatever you wish. We are going to create this environment and install Python 3.9 with it.

`$ conda create --name onl python=3.9`

When this environment is created, you should see instructions about how to activate and deacative it.

To activate:
`$ conda activate onl`

You should now see your environment name in parenthesis next to the prompt to let you know you are working within this environment.

To deactivate:
`$ conda deactivate`

**Make sure you are always working in this environment any time you are using this tutorial to make sure you can access all your packages as needed!**

If you want to see a list of all your environments (and their locations):
`$ conda info --envs`

### Managing environments

The main reason to use virtual environments is to install and manage packages with ease for your project (in this case, this tutorial). We will install a few packages as we go, but right now, let's install the `jupyter` package so that you can open notebooks.

To install jupyter, make sure your environment is activated! And:
`$ conda install jupyter`

This will install the jupyter Python package as well as any dependences it has.

To see a list of packages installed in your environment, from within your active environment:
`$ conda list`

You should only need to install a package once in your environment.

## Development environments

There are many ways to write, edit and execute Python scripts. Programmers will often use an Integrated Development Environment (IDE), such as PyCharm, which is a popular IDE for Python. There are a lot of advantages to using IDEs, especially if you’re building more complicated software applications; however, for this tutorial, we’ll be executing fairly simple routines and can do this from Jupyter notebooks. In fact, this tutorial is contained in Jupyter notebooks!


```python

```
