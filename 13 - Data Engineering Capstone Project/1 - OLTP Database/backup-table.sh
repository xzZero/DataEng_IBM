#!/bin/sh
# The above line tells the interpreter this code needs to be run as a shell script.

# Set the database name to a variable. 
DATABASE='sales'
# Set the table name to a variable. 
TABLE='sales_data'
# This will be printed on to the screen. In the case of cron job, it will be printed to the logs.
echo "Pulling Database: This may take a few minutes"

# Set the folder where the database backup will be stored
backupfolder=/home/theia/backups

# Number of days to store the backup 
keep_day=30

sqlfile=$backupfolder/sales_data-$(date +%d-%m-%Y_%H-%M-%S).sql
zipfile=$backupfolder/sales_data-$(date +%d-%m-%Y_%H-%M-%S).gz

# Create a backup

if mysqldump $DATABASE $TABLE> $sqlfile ; then
   echo 'Sql dump created'
    # Compress backup 
    if gzip -c $sqlfile > $zipfile; then
        echo 'The backup was successfully compressed'
    else
        echo 'Error compressing backupBackup was not created!' 
        exit
    fi
    rm $sqlfile 
else
   echo 'pg_dump return non-zero code No backup was created!' 
   exit
fi

# Delete old backups 
find $backupfolder -mtime +$keep_day -delete