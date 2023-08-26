#!/bin/bash
dir=$(pwd)
echo $dir
for n in {1..7}
	do
	cd $dir/launchers/type-$n 
	pwd
	num=$(ls -l *style* | wc -l)
	rofi -show drun -theme launchers/type-$n/style-5.rasi
	#for i in $(seq 1 $num)
		#do
		#rofi -show drun -theme launchers/type-$n/style-$i.rasi
		#echo "launchers/type-$n/style-$i.rasi"
		#read -n1 -r -p "Press any key to continue..." key
		#done
done
