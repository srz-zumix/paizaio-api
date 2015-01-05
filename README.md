paiza.IO Python API
===========
  
[paiza.IO](http://melpon.org/wandbox/) is a social compilation service.  
This project is a Pythonic binding to the paiza.IO API.

Installation
--------------------------------------------------

	git clone https://github.com/srz-zumix/paizaio-api.git
	cd paizaio-api
	python setup.py install


Getting Started
--------------------------------------------------

	from paizaio import PaizaIO
	
	paiza = PaizaIO()
	paiza.code('#include <iostream>\nint main() { int x = 0; std::cout << "hoge" << std::endl; }')
	print paiza.run()
