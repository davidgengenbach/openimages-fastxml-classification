rm splitter.{html,cpp,c,so,o}
cython --cplus splitter.pyx

/usr/bin/clang -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -Wall -pedantic -Wextra -I/Users/davidgengenbach/anaconda3/lib/python3.5/site-packages/numpy/core/include -I/Users/davidgengenbach/anaconda3/include/python3.5m -c splitter.cpp -o splitter.o -std=c++11

#/usr/bin/clang -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -Wall -pedantic -Wextra -I/Users/davidgengenbach/anaconda3/lib/python3.5/site-packages/numpy/core/include -I/Users/davidgengenbach/anaconda3/include/python3.5m -c splitter.cpp -o splitter.o -std=c++11
