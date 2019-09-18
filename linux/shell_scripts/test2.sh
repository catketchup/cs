#!/bin/bash

echo "It is a test"
echo "\"It is a test\""

read name
echo "$name it is a test"
echo -e "OK! \n" # -e 开启转义
echo "It is a test"
echo -e "OK! \c" # -e 开启转义 \c 不换行
echo "It is a test"

echo "output to this file" > myfile
echo `date`

printf "Hello, Shell\n"
