#!/bin/bash

#cap_="${1}/"
folder="/home/christopher/Documents/prog/gene/face/face_out_/"

#pref="${2}"
pref="face"

declare -i leng
leng=$(echo $pref | wc -c)
leng=$leng-1

# TODO
if (($leng < 4)); then
	echo "pref length required"
	return 0
fi

declare -i cap_
cap_=299
declare -i len_
all="$(ls $folder)"
declare -i coun
coun="$(echo $all | wc -w)"
declare -i a
a=0
declare -i num_
while (($a < $coun)); do
	a=$a+1
	this="$(echo ${all} | cut -f $a -d " " -)"
	numb=${this:$leng+1:4}
	len_=$(echo $numb | wc -c)
	len_=$len_-1
	while [[ ${numb:0:1} == "0" ]] && (( $len_ > 1 )); do
		numb=${numb:1:$len_}
		len_=$(echo $numb | wc -c)
		len_=$len_-1
	done
	num_=$numb
	if (($num_ > $cap_)); then
		#echo here
		mv $folder$this ~/Documents/trash/
	fi
done

