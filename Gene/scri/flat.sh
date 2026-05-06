#!/bin/bash
# find the first file and change its number to 0000, then next to 0001, etc
# TODO: probably better to use kept in normal folder
#folder="kept/flora/trun/"
#folder="/home/christopher/Documents/prog/blen/blen/flor/mush/"
#folder="/home/christopher/Documents/prog/blen/blen/flor/need/"
#folder="/home/christopher/Documents/prog/make/flor/stic/kept/00/"
folder="${1}/"
# TODO: automate this
# files per object
declare -i fpob
fpob=3

##################

all="$(ls $folder)"
declare -i coun
coun="$(echo $all | wc -w)"
coun=$coun/$fpob
declare -i leng
declare -i a
a=0
declare -i end
declare -i field
declare -i b
while (( $a < $coun )); do
	b=$a*$fpob
	end=$b+$fpob
	while (( $b < $end )); do
		field=$b+1
		# this file
		# TODO: why does this work without escape characters
		this="$(echo ${all} | cut -f $field -d " " -)"
		leng="$(echo $this | wc -c)"
		numb=""
		if (( $a < 1000 )); then
			numb=${numb}0
		fi
		if (( $a < 100 )); then
			numb=${numb}0
		fi
		if (( $a < 10 )); then
			numb=${numb}0
		fi
		numb=${numb}$a
		newn=${this:0:5}$numb${this:9:$leng}
		if [[ "$folder$this" != "$folder$newn" ]]; then
			#echo "renaming $folder$this to $folder$newn"
			mv $folder$this $folder$newn
		fi
		b=$b+1
	done
	a=$a+1
done

