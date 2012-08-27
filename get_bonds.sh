#!/bin/bash

rm -f cn.dat

for file in findmolecules.x???
do

grep -B 1000 "Averages for transition states" $file | grep -A 1000 "Averages for molecules" | awk 'match($0,"C-N"){print substr($0,RSTART-2,1)}' > cn_count.dat
echo -n "$file" | sed s/findmolecules.x/" "/g >> cn.dat
echo -n " " >> cn.dat
blocker cn_count.dat | grep Final | awk '{print $4, $6}' | sed s/-nan/"0.0"/g >> cn.dat
rm cn_count.dat

grep -B 1000 "Averages for transition states" $file | grep -A 1000 "Averages for molecules" | awk 'match($0,"C-C"){print substr($0,RSTART-2,1)}' > cc_count.dat
echo -n "$file" | sed s/findmolecules.x/" "/g >> cc.dat
echo -n " " >> cc.dat
blocker cc_count.dat | grep Final | awk '{print $4, $6}' | sed s/-nan/"0.0"/g >> cc.dat
rm cc_count.dat

done
