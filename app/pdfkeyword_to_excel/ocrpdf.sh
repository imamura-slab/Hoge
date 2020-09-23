#!/bin/zsh

## $1 : hoge.pdf

## pdf to png
pdftopng $1 ./input/input

## prepare result file
rm result.csv
touch result.csv

## crop keyword
python3 crop.py


## OCR
for i in `seq 0 3`
do
    ID_filename=`printf ./output/ID/%06d.png $i+1`
    echo $ID_filename
    ocr $ID_filename >> result.csv
    for j in `seq 0 29`
    do
	key_filename=`printf ./output/keyword/%06d%06d.png $i+1 $j`
	echo $key_filename
	ocr $key_filename >> result.csv
    done
done

sed -e 's/。//g' ./result.csv > temp.txt
mv temp.txt result.csv
sed -e 's/、//g' ./result.csv > temp.txt
mv temp.txt result.csv
sed -e '/^$/d' ./result.csv > temp.txt
mv temp.txt result.csv
cat result.csv | tr '\n' ', ' > temp.txt
mv temp.txt result.csv

