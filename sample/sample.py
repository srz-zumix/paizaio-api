#!/usr/bin/env python

from paizaio import PaizaIO
	
if __name__ == '__main__':
	paiza = PaizaIO()
	paiza.longpoll(True)
	paiza.code('#include <iostream>\nint main() { int x = 0; std::cout << "hoge" << std::endl; }')
	print paiza.run()

