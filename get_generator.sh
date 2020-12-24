#!/bin/bash
# Tomáš Batěk, 2020
#
# Shell script to download original C++ ASCII-art generator, compile it, take the
# executable and delete everything used.

rm -rf .generator

echo "=========== Cloning repository... ==========="

git clone https://github.com/tomas-bat/ASCII-art-generator .generator
RES=$?

if [ $RES -ne 0 ]
then
	echo "Error: Failed cloning repository."
	rm -rf .generator
	exit 1
fi

echo "=========== Repository cloned into .generator ==========="
echo "=========== Compiling C++... ==========="

cd .generator
make compile
RES=$?

if [ $RES -ne 0 ]
then
	echo "Error: Failed compiling C++."
	cd ..
	rm -rf .generator
	exit 1
fi

echo "=========== C++ compiled ==========="
echo "=========== Moving generator executable... ==========="

cp generator ../generator
RES=$?

if [ $RES -ne 0 ]
then
	echo "Error: Failed moving generator executable."
	cd ..
	rm -rf .generator
	exit 1
fi

cd ..
rm -rf .generator

echo "=========== Finished. ==========="
