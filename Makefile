CFLAGS = -g -O3 -DNDEBUG -DDONT_USE_TEST_MAIN
CPPFLAGS = -g -O3 -fpermissive -DNDEBUG -DDONT_USE_TEST_MAIN

default: binpot 


HERE=$(realpath ./)

	
binpot: 
	git clone https://github.com/cmla/PotreeConverter.git src/potreeconverter
	cd src/potreeconverter && make PotreeConverter
	## patch for colab
	cp $(HERE)/src/potree.colab.js  src/potreeconverter/PotreeConverter/resources/page_template/libs/potree/
	## copy to bin
	mkdir -p $(HERE)/bin/
	cp $(HERE)/src/potreeconverter/build/PotreeConverter/PotreeConverter $(HERE)/bin/
	cp -r $(HERE)/src/potreeconverter/PotreeConverter/resources $(HERE)/bin/


clean:
	-rm -f -r bin
	cd src/potreeconverter && make clean 
