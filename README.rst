qcodes++
===================================

QCoDeS is a Python-based data acquisition framework developed by the
Copenhagen / Delft / Sydney / Microsoft quantum computing consortium.
It contains a huge range of drivers for communicating with instruments,
and a very flexible database-based method for collecting data.
See https://qcodes.github.io/ for more info.

This package, qcodes++ (aka qcodes-plusplus or qcpp), is designed to 
make using qcodes as user friendly as possible. Qcodes++ rests on the
text-based data set and easy definition of loops once used in qcodes.
It also has truly live plotting and introduces new features to streamline
data acquisition. All features of qcodes are preserved in a qcodes++ environment,
since qcodes++ wraps around qcodes and requires the latest version of qcodes
to function; 

QCoDeS and qcodes++ are compatible with Python 3.5+. It is primarily intended for use
from Jupyter notebooks and jupyter lab, but can also be used from Spyder, traditional terminal-based
shells and in stand-alone scripts.

Docs
====
Check out the wiki https://github.com/djcarrad/qcodes-plusplus/wiki for an introduction. The 
accompanying jupyter notebooks are under 'tutorials'. As of yet, there is no separate, comprehensive
documentation; this is high on the to-do list. However, all the code is quite well self-documented and 
everything is open source. If you need to know which arguments a function takes, or which capabilities 
an instrument driver has, just open up the file! Or ask a friend

Install
=======

- Install anaconda from anaconda website: if you want to be able to call python from the command line, you should add the anaconda PATH to environment variables during install. Anaconda is a suite of software can be used to manage a python installation. 

- Install git: https://git-scm.com/download/win

Git is versioning software that allows multiple developers to contribute to pieces of software. It's used when software is likely to be changing quickly and flexibility and collaboration is key.

- Open the newly installed git bash, navigate to the desired folder (usually C:/git. You may have to create this folder), and clone the repository

	cd C:/git

	git clone https://github.com/djcarrad/qcodes-plusplus.git qcodes-plusplus

'cloning' the repository effectively downloads the latest version of the software, and tells git to keep track of changes you might make to it. If you prefer to use the git gui, use Source Location: https://github.com/djcarrad/qcodes-elab.git and Target Directory: C:/git/qcodes-elab (or the directory of your choice)

- Now open the Anaconda prompt and type:

	conda create –n qcodes python
	
	activate qcodes
	
	pip install –e *path to repository* qcodes

	(for example: pip install -e C:/git/qcodes-plusplus qcodes-plusplus)

This does a couple of things; it creates an 'environment' that is effectively a separate python installation. qcodes requires that some packages are not updated to the latest version. Running qcodes in its own environment means your 'base' python installation can remain completely up-to-date, and that qcodes can run smoothly. Calling 'activate qcodes' puts you in the qcodes environment. You can 'deactivate qcodes' if you want to return to the base environment. The *path to repository* is usually just 'C:/git/qcodes-elab'

- Optionally install useful packages from the anaconda prompt:

	pip install scipy zhinst

You can now run qcodes in jupyter notebook or jupyter lab by opening the anaconda prompt, and typing

	activate qcodes
	
	jupyter notebook

or

	jupyter lab
	
Additionally...
---------------

- If you are going to use VISA instruments (e.g. ones that communicate via GPIB, USB, RS232) you should install the NI VISA and GPIB(488.2) backends from the National Instruments website

https://www.ni.com/en/support/downloads/drivers/download.ni-visa.html

https://www.ni.com/en/support/downloads/drivers/download.ni-488-2.html

- If the qcodes install fails, you may need to install Visual Studio C++ build tools. https://visualstudio.microsoft.com/downloads/ --> Tools for Visual Studio --> Build Tools for Visual Studio.
	
	
Updating
--------
Open git bash, navigate to the install folder (usually cd C:/git/qcodes-plusplus), and use 

	git pull

Sometimes, git complains that you cannot pull due to non-committed changes. This can happen even though you have not changed anything, since some files in qcodes automatically backup/change but in totally unimportant ways. You can

	git fetch --all

	git reset --hard origin/master

This _should_ now be fixed. If you encounter this error, please let me know.

Status
======
As of 24/6/2024, latest versions of all packages required by qcodes are working, except:
The current version of ipykernel closes all plot windows when the kernel is restarted. Will be difficult to fix given the lack of documentation for ipykernel.

On the to-do list is improving analysis functions, such as tighter integration with InspectraGadget
and incorporation of fitting tools.

If there is a feature that you desire, feel free to contact me, damonc@dtu.dk. We can try to make it happen together!

License
=======

See `License <https://github.com/QCoDeS/Qcodes/tree/master/LICENSE.rst>`__.
