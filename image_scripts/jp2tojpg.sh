#!/bin/bash

input_filename=`basename $1 .jp2`
kdu_expand -i $input_filename.jp2 -o $input_filename.tif
convert $input_filename.tif $input_filename.jpg
