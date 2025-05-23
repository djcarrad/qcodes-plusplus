qcodes++
===================================

QCoDeS is a Python-based data acquisition framework developed by the
Copenhagen / Delft / Sydney / Microsoft quantum computing consortium.
It contains a huge range of drivers for communicating with instruments,
and a flexible - but complex - database-based method for collecting data
and running measurement loops.
See https://qcodes.github.io/ for more info.

This package, qcodes++ (aka qcodesplusplus or qcpp), provides user-friendly
frontend to the solid backend of qcodes. If you have always wanted to run 
your measurements using python but found qcodes too daunting, qcodes++ is 
the package for you. Qcodes++ features

- text-based data (i.e. readable by e.g. notepad, excel, origin pro, etc)

- a simple yet powerful method for taking data and running measurement loops

- superior live plotting

- powerful offline plotting

- Improvements to core qcodes functions (such as the Station) to streamline data acquisition, protect (meta)data integtrity and minimise user error

- Improved drivers for certain instruments

- and other user-friendliness improvements outlined in the documentation.

All features of qcodes are preserved in a qcodes++ installation. Even those
features that qcodes++ does not rely on can be used seamlessly within the same
notebook/environment. This means you lose nothing by installing qcodes++ ontop of qcodes.

QCoDeS and qcodes++ are compatible with Python 3.5+. It is primarily intended for use
from Jupyter notebooks and jupyter lab, but can also be used from Spyder, traditional terminal-based
shells and in stand-alone scripts.

Docs
====
Check out the wiki https://github.com/djcarrad/qcodesplusplus/wiki for an introduction. The 
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

	git clone https://github.com/djcarrad/qcodesplusplus.git

'cloning' the repository effectively downloads the latest version of the software, and tells git to keep track of changes you might make to it. If you prefer to use the git gui, use Source Location: https://github.com/djcarrad/qcodesplusplus.git and Target Directory: C:/git/qcodesplusplus (or the directory of your choice)

- Now open the Anaconda prompt and type:

	conda create –n qcodes python
	
	activate qcodes
	
	pip install –e *path to repository* qcodes

	(for example: pip install -e C:/git/qcodesplusplus)

This does a couple of things; it creates an 'environment' that is effectively a separate python installation. qcodes requires that some packages are not updated to the latest version. Running qcodes in its own environment means your 'base' python installation can remain completely up-to-date, and that qcodes can run smoothly. Calling 'activate qcodes' puts you in the qcodes environment. You can 'deactivate qcodes' if you want to return to the base environment. The *path to repository* is usually just 'C:/git/qcodesplusplus'

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
Open git bash, navigate to the install folder (usually cd C:/git/qcodesplusplus), and use 

	git pull


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

Differences from qcodes-elab
==================================================

Data_type cannot be declared to parameter on init. 
It has to be declared after by parameter.data_type=float or parameter.data_type=str


