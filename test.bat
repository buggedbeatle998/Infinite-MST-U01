@echo off
echo Unmerged:
gcc prims.c -o prims
prims 2000
echo _
echo Merged
gcc primsmerged.c -o prims
prims 2000