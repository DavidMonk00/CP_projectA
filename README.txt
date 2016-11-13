---README---
***IF POSSIBLE, PLEASE RUN ON LINUX***
This project uses compiled C code for the algorithms which is then linked
to a Python wrapper through ctypes. I haven't been able to find a way for the
c files to correctly compile on windows and thus the Python code will not run.
The error is:
"WindowsError: [Error 193] %1 is not a valid Win32 application" when trying to
load a shared library.

-Operation-
Linux:
 - Modify Main.py and Plot.py to the show the desired plot
 - Run Main.py

OR

*Compile C from scratch*
 - Ensure gsl is installed by running 'sudo apt-get install gsl-bin'
 - Navigate to the correct folder
 - Modify Main.py and Plot.py to show desired plot
 - Run in the terminal with './compile_run.sh'

Windows:
 - Compile the both singlependulum.c and doublependulum.c
 - Modify the LoadLibrary arguments in Main.py to point to the compiled libraries
 - Modify Main.py and Plot.py to show desired plot
 - Run Main.py


-Selecting Variables-
Single or double:	In Main.py, main(), choose to run either singlePendulum or doublePendulum
Initial variables:	In Main.py, main(), Modify any of A,D,R,G,cycles,h
Output:			In Plot.py, plotMethod or plotDoubleMethod, uncomment the plot which you would like to output.
