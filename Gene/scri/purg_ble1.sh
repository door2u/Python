#!/bin/bash

folder="${1}/"

all="$(ls $folder)"
declare -i coun
coun="$(echo $all | wc -w)"
declare -i a
a=0
while (($a < $coun)); do
	a=$a+1
	this="$(echo ${all} | cut -f $a -d " " -)"
	blend1="$(echo ${this} | cut -f 2 -d "." -)"
	if [[ $blend1 == "blend1" ]]; then
		mv $folder$this ~/Documents/trash/
	fi
done

