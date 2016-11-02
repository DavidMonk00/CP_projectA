echo 'Starting compilation...'
gcc -fPIC -std=c99 -shared -o smallangle.so smallangle.c `pkg-config --cflags --libs gsl`
echo 'Compiled succesfully. Starting plot.'
python Main.py
