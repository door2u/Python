#!/bin/bash

# TODO: removed all three-digit blend and image files
# TODO: moved folders

all="$(ls out)"

declare -i coun
coun="$(echo $all | wc -w)"

#echo $coun

declare -i typ

declare -i i
declare -a list
i=0
while (($i < $coun)); do

	i=$i+1
	list="$(echo ${all} | cut -f $i -d " " -)"

	#echo ""
	pref="$(echo $list | cut -f 1 -d "." -)"
	#echo $pref
	midd="$(echo $list | cut -f 2 -d "." -)"
	#echo $midd
	suff="$(echo $list | cut -f 3 -d "." -)"
	#echo $suff

	typ=2

	# text file without a period
	if [[ $pref == $midd ]] && [[ $midd == $suff ]]; then
		fil="$pref.png"
		typ=0
	fi
	# ie 500.blend
	if [[ $midd == "blend" ]]; then
		fil="$pref.png"
		typ=1
	fi
	# ie 4.743974
	if [[ $pref != $midd ]] && [[ $suff == "" ]]; then
		fil="$pref.$midd.png"
		typ=0
	fi
	# ie 4.743974.blend
	if [[ $suff == "blend" ]]; then
		fil="$pref.$midd.png"
		typ=1
	fi

	chec="$(ls out/$fil 2> /dev/null)"
	resu="$(echo $chec | cut -f 1 -d " " -)"
	if [[ $resu == "" ]]; then
		mv out/$list out/t/
		#echo "trashing $list"
		#echo -n ""
	else
		if (( $typ == 0 )); then
			mv out/$list out/f/
			#echo "keeping text $list"
			#echo -n ""
		elif (( $typ == 1 )); then
			mv out/$list out/b/
			#echo "keeping blen $list"
			#echo -n ""
		else
			mv out/$list out/i/
			#echo "keeping imag $list"
			#echo -n ""
		fi
	fi

	#if (($i % 100 == 0)); then
	#	echo $i
	#fi

done


