#!/bin/bash

folder="${1}/"

pref="${2}"
declare -i a

declare -i leng
leng=$(echo $pref | wc -c)
leng=$leng-1

# TODO
if (($leng<4)); then
	echo "pref length required"
	return 0
fi

all="$(ls $folder)"
declare -i coun
coun="$(echo $all | wc -w)"
a=0
while (($a < $coun)); do

	a=$a+1
	this="$(echo ${all} | cut -f $a -d " " -)"

	para="$(echo ${this} | cut -f 3 -d "_" -)"

	if [[ $para == "para" ]]; then

		numb=${this:$leng+1:4}

		# check if png exists
		png=$folder${pref}_${numb}0001.png
		kee1=$(ls $png 2> /dev/null)
		# check if blen exists
		blen=$folder${pref}_${numb}.blend
		kee2=$(ls $blen 2> /dev/null)

		if [[ $kee1 == "" && $kee2 == "" ]]; then
			mv $folder$this ~/Documents/trash/
			#echo "trashing $folder$this"
		else
			echo -n ""
		fi

	fi
	
done


