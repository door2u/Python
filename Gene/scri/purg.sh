#!/bin/bash

folder="${1}/"

pref="${2}"
declare -i a
#a=2
#while (( 1 == 1 )); do
#	fold="$(echo $folder | cut -f $a -d '/' -)"
#	#echo $bark
#	if [[ $fold != "" ]]; then
#		#if [[ $fold == "bark" ]]; then
#		#	bark="1"
#		#	break
#		#fi
#		pref=$fold
#	else
#		break
#	fi
#	#if [[ $bark == "" ]]; then
#	#	bark="0"
#	#	break
#	#fi
#	a=$a+1
#done

bark="0"
if [[ $pref == "bark" ]]; then
	bark="1"
fi
#echo $bark

#echo $pref
declare -i leng
leng=$(echo $pref | wc -c)
leng=$leng-1

#echo $leng

# TODO
if (($leng<4)); then
	echo "pref length required"
	return 0
fi

#return 0

all="$(ls $folder)"
declare -i coun
coun="$(echo $all | wc -w)"
a=0
while (($a < $coun)); do
	a=$a+1
	this="$(echo ${all} | cut -f $a -d " " -)"
	#numb=${this:5:4}
	numb=${this:$leng+1:4}
	#echo $numb
	#return 0
	#pref=${this:0:4}
	if [[ $bark == "1" ]]; then
		# TODO
		#pref="trun"
		pref="wrap"
	fi

	

	# check if png exists
	path=$folder${pref}_${numb}0001.png
	kee=$(ls $path 2> /dev/null)
	if [[ $kee == "" ]]; then
		mv $folder$this ~/Documents/trash/
		#echo "trashing $folder$this"
		#out=$(ls $folder$this)
		#echo $folder$this
	else
		echo -n ""
		#ls $folder$this
	fi
	blend1="$(echo ${this} | cut -f 2 -d "." -)"
	if [[ $blend1 == "blend1" ]]; then
		mv $folder$this ~/Documents/trash/
		
	fi
done


