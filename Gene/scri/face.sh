#!/bin/bash
seco="${1}"
declare -i leng
leng=$(echo $seco | wc -c)
leng=$leng-1
if (($leng == 0)); then
	# TODO: numb in cap interferes with numb in purg
	source scri/cap_.sh
	source scri/purg.sh /home/christopher/Documents/prog/gene/face/face_out_ face
	source scri/flat.sh /home/christopher/Documents/prog/gene/face/face_out_ face
else
	python3 scri/purg_fals.py
	source scri/purg.sh /home/christopher/Documents/prog/gene/face/face_out_ face
	source scri/merg.sh /home/christopher/Documents/prog/gene/face/face_out_ /home/christopher/Documents/prog/gene/face/face_libr face
fi
