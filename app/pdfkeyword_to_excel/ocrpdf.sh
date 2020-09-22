#!/bin/zsh

rm result.txt
touch result.txt

python3 crop.py
ocr ./result/ID.png

for i in `seq 0 29`
do
    ocr ./result/$i.png >> result.txt
done

sed -e 's/。//g' ./result.txt > temp.txt
mv temp.txt result.txt
sed -e 's/、//g' ./result.txt > temp.txt
mv temp.txt result.txt
sed -e '/^$/d' ./result.txt > temp.txt
mv temp.txt result.txt
cat result.txt | tr '\n' ', ' > temp.txt
mv temp.txt result.txt

