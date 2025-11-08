#!/bin/bash
# copy one folder to another, avoid overwriting, and number all files sequentially
# TODO: probably better to use kept in normal folder
# from fol1 to fol2

#fol1="flora/trun/kept/02_extr/"
#fol2="kept/flora/trun_extr/"

#fol1="flora/bran/kept/00/"
#fol2="kept/flora/bran/"

#fol1="rock/kept/picked/13/"
#fol2="kept/rock/"

#fol1="flora/bark/kept/18/"
#fol2="kept/flora/bark/"

#fol1="flora/trun/kept/09/"
#fol2="kept/flora/trun/"

#fol1="/home/christopher/Documents/prog/make/flor/need/kept/01/"
#fol2="/home/christopher/Documents/prog/blen/blen/flor/need/"

fol1="${1}/"
fol2="${2}/"
pref="${3}"

# TODO
# files per object
declare -i fpob
fpob=3

###################

declare -i pref_leng
pref_leng=$(echo $pref | wc -c)

# TODO
if (($pref_leng<5)); then
	echo "pref length required"
	return 0
fi

#echo $pref_leng

declare -i suff_star
suff_star=$pref_leng+4
#echo $suff_star
#return 0

all1="$(ls $fol1)"
all2="$(ls $fol2)"
declare -i coun
cou1="$(echo $all1 | wc -w)"
cou2="$(echo $all2 | wc -w)"
cou2=$cou2/$fpob
declare -i leng
declare -i a
a=0
declare -i end
declare -i field
declare -i b
b=0
while (( $a < $cou1 )); do
	echo "$a of $cou1"
	#b=0
	# TODO
	while (( $b < 10000 )); do
		field=$a+1
		# this file
		# TODO: why does this work without escape characters
		this="$(echo ${all1} | cut -f $field -d " " -)"
		leng="$(echo $this | wc -c)"
		#echo $this
		#echo $leng
		numb=""
		if (( $b < 1000 )); then
			numb=${numb}0
		fi
		if (( $b < 100 )); then
			numb=${numb}0
		fi
		if (( $b < 10 )); then
			numb=${numb}0
		fi
		numb=${numb}$b
		# TODO: think this is working because it clips the end, $leng should subtract beginning
		#newn=${this:0:5}$numb${this:9:$leng}
		# TODO: why does this add 5 zeroes (suff start pref length + 4)
		#newn=${pref}$numb${this:$suff_star-1:$leng}
		newn=${pref}_${numb}${this:$suff_star:$leng}
		#echo $newn

		#return 0
		path=$fol2$newn
		exis=$(ls $path 2> /dev/null)
		if [[ $exis == "" ]]; then
			mv $fol1$this $fol2$newn
			#echo "moving $fol1$this to $fol2$newn"
			break
		fi
		b=$b+1
	done
	a=$a+1
done

