#!/usr/bin/env bash


printfoldercontent()
{
    echo "DIR is $1"

    let count=0
    for f in "$1"/*
    do
        echo $(basename $f)
        let count=count+1
    done
    echo ""
    echo "Count: $count"

}


extractFile()
{
    echo "filepath is $1"

    case $(file $1) in
        *"Zip"*)
            command="unzip $1";;
        *"bzip2"*)
            command="pbzip2 -d $1";;
        *"7-zip"*)
            command="7za e $1";;
        *"gzip"*)
            command="gunzip -rf $1";;
         *"MAR"*)
            command="$(echo unknown command $1)";;
        *)
        echo "INVALID FILE";;
    esac

    echo $command

}


target="/home/marcman/PycharmProjects/cybersecuritychallenge102018/matrioska3"
#printfoldercontent $target

startfile="$target/matrioska"
#extractFile $startfile


echo "running test for extractFile"
test7z="$target/testdata/7z"
testbzip="$target/testdata/bzip"
testgzip="$target/testdata/gzip"
testmar="$target/testdata/mar"
testzip="$target/testdata/zip"

extractFile $test7z
extractFile $testbzip
extractFile $testgzip
extractFile $testmar
extractFile $testzip