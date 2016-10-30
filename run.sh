gcc -fPIC -std=c99 -shared -o smallangle.so smallangle.c `pkg-config --cflags --libs gsl`
python Main.py
