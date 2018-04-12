primerorden.png:valores.txt
	python ej19.py

valores.txt:
	c++ ej19.cpp
	./a.out>valores.txt
