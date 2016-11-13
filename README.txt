---README---
***IF POSSIBLE, PLEASE RUN ON LINUX***
This project uses compiled C code for the algorithms which is then linked
to a Python wrapper through ctypes. I haven't been able to find a way for the
c files to correctly compile on windows and thus the Python code will not run.

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
 - Modify Main.py and Plot.py to show desired plot
 - Run Main.py


-Selecting Variables-
Single or double:	In Main.py, main(), choose to run either singlePendulum or doublePendulum
Initial variables:	In Main.py, main(), Modify any of A,D,R,G,cycles,h
Output:			In Plot.py, plotMethod or plotDoubleMethod, uncomment the plot which you would like to output.

