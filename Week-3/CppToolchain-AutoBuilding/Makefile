run: display1.o display2.o display3.o mesh.o
	g++ display1.o mesh.o -o display1  -L/usr/X11R6/lib -lGL -lglut -lGLU
	g++ display2.o mesh.o -o display2  -L/usr/X11R6/lib -lGL -lglut -lGLU
	g++ display3.o mesh.o -o display3  -L/usr/X11R6/lib -lGL -lglut -lGLU
mesh.o: mesh.cpp
	g++ -c -I include/ mesh.cpp -o mesh.o
display3.o: display.cpp
	g++ -w -c -D TEST3 -I include/ display.cpp -o display3.o
display2.o: display.cpp
	g++ -w -c -D TEST2 -I include/ display.cpp -o display2.o
display1.o: display.cpp
	g++ -w -c -D TEST1 -I include/ display.cpp -o display1.o
clean:
	rm *.o
	rm display1
	rm display2
	rm display3