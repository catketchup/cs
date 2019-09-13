#!/bin/bash
echo "Hello World!"
my_name="ketchup"
echo ${my_name}

str="Hello, my name is \"$my_name\"! \n"
echo -e ${str}
# what is echo -e?

echo ${#my_name}
echo ${my_name:1:3}

# array
array_name=(1 2 3 4)
array_name[4]=5
echo ${array_name[4]}
echo ${array_name[@]}

for i in {1..5}; do
    echo "for $i"
done  

:<<EOF
This is the first comment.
This is the second comment.
EOF

echo "shell pass variables";
echo "the name of file: $0"
echo "the first parameter: $1"
echo "the second parameter: $2"
echo -e "the third parameter: $3 \n"

echo -e "the number of parameters: $# \n"
echo -e "print the parameters as a string: $* \n"


echo "-- \$* 演示 ---"
for i in "$*"; do
    echo $i
done

echo "-- \$@ 演示 ---"
for i in "$@"; do
    echo $i
done

echo -e "\n"
echo "${1}"

val=`expr 2 + 2`
echo "the sum of the two numbers: $"

a=10
b=20

val=`expr $a + $b`
echo "a + b: $val"

if [ $a == $b ]
then
    echo "a equals b"
fi
if [ $a != $b ]
then
    echo "a doesn't equals b "
fi    
