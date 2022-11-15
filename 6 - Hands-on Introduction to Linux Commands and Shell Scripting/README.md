## Description
In this assignment, I act as a lead linux developer at ABC company. ABC currently suffers from a huge bottleneck - each day, interns must painstakingly access encrypted password files on core servers, and backup those that were updated within the last 24-hours. This introduces human error, lowers security, and takes an unreasonable amount of work.

As ABC INC's most trusted linux developer, I have been tasked with creating a script backup.sh which automatically backs up any of these files that have been updated within the past 24 hours.
## Objectives
- The objective of this lab is to incorporate much of the shell scripting you've learned over this course into a single script.
- You will schedule your shell script to run every 24 hours using crontab.
## Answer
```bash
#!/bin/bash

# This checks if the number of arguments is correct
# If the number of arguments is incorrect ( $# != 2) print error message and exit
if [[ $# != 2 ]]
then
  echo "backup.sh target_directory_name destination_directory_name"
  exit
fi

# This checks if argument 1 and argument 2 are valid directory paths
if [[ ! -d $1 ]] || [[ ! -d $2 ]]
then
  echo "Invalid directory path provided"
  exit
fi

# [TASK 1]
targetDirectory=$1
destinationDirectory=$2

# [TASK 2]
echo "$1"
echo "$2"

# [TASK 3]
currentTS=`date +%s`

# [TASK 4]
backupFileName="backup-[$currentTS].tar.gz"

# We're going to:
  # 1: Go into the target directory
  # 2: Create the backup file
  # 3: Move the backup file to the destination directory

# To make things easier, we will define some useful variables...

# [TASK 5]
origAbsPath=`pwd`

# [TASK 6]
cd $destinationDirectory # <-
destDirAbsPath=`pwd`

# [TASK 7]
cd $origAbsPath # <-
cd $targetDirectory # <-

# [TASK 8]
yesterdayTS=$(($currentTS - 24 * 60 * 60))

declare -a toBackup

for file in $(ls) # [TASK 9]
do
  # [TASK 10]
  if ((`date -r $file +%s` > $yesterdayTS))
  then
    # [TASK 11]
    toBackup+=($file)
  fi
done

# [TASK 12]
tar -czvf $backupFileName ${toBackup[@]}
# [TASK 13]
mv $backupFileName $destDirAbsPath
# Congratulations! You completed the final project for this course!

```
For the original file, please refer to [backup.sh](https://github.com/xzZero/DataEng_IBM/blob/main/6%20-%20Hands-on%20Introduction%20to%20Linux%20Commands%20and%20Shell%20Scripting/week4/backup.sh)
List crontab's tasks
```bash
crontab -l 
```
Open crontab in editor 
```bash
crontab -e 
```
Edit the crontab editor as follow to schedule the backup task to run every 24h\
![alt text](https://github.com/xzZero/DataEng_IBM/blob/main/6%20-%20Hands-on%20Introduction%20to%20Linux%20Commands%20and%20Shell%20Scripting/week4/17-crontab.jpg "cron")

## [Cron Cheatsheet](https://devhints.io/cron) 