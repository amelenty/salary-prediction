#!/bin/bash

mkdir output
CSV_HEADER="date,median_salary\n"

for file in $( ls data ); do
	echo Processing $file
	echo -e $CSV_HEADER > output/"${file%.*}-J.csv"
	echo -e  $CSV_HEADER > output/"${file%.*}-M.csv"
	echo -e  $CSV_HEADER > output/"${file%.*}-S.csv"
	gawk -f parse.awk $file
	echo Done.
done
