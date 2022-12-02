#!/bin/bash

while getopts d:y:f: flag
do
    case "${flag}" in
        d) day=${OPTARG};;
        y) year=${OPTARG};;
        f) file=${OPTARG};;
    esac
done
source .env

url="https://adventofcode.com/$year/day/${day}/input"

curl --header "$HEADERS" $url -o $file