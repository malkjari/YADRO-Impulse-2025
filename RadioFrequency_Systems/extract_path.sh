#!/bin/bash

if [ $# -ne 2 ]
then
	echo "Incorrect number of args; usage: $0 [path_to_file] [keyword]"
	exit 1
fi

result=$(grep $2 $1)

if [ -n result ]
then
	echo "$result"
else
	echo "There are no line with such keyword!"
fi
