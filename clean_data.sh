#!/bin/bash -e
###################################################################################
# Script       : clean_data.sh
#
# Purpose      : This script executes the unzipping and cleaning of all reddit data
#
# Authors      : Nathan Anneken, Andrew Ma - 84.51°
#
# Arguments    : None
#
# Date         : 28-July-2016
#
# Example Call : ./clean_data.sh
#
#
###################################################################################

# if [ "${REDDIT_DIRECTORY}" == "" ]
# then
# echo " Error: Environment variable REDDIT_DIRECTORY not set"
# exit 1
# fi

function timer()
{
    if [[ $# -eq 0 ]]; then
        echo $(date '+%s')
    else
        local  stime=$1
        etime=$(date '+%s')

        if [[ -z "$stime" ]]; then stime=$etime; fi

        dt=$((etime - stime))
        ds=$((dt % 60))
        dm=$(((dt / 60) % 60))
        dh=$((dt / 3600))
        printf '%d:%02d:%02d' $dh $dm $ds
    fi
}

cd ./reddit_data;

OVERALL_START_TIME=$(timer)

for filename in *; do
  for filezip in $( ls $filename/*.bz2 ); do
    bzip2 -dk $filezip
  done

  echo -e "De-compression complete\n"

  for fileclean in $( ls $filename --ignore='*.*' ); do
    python ../json_convert.py $filename/$fileclean
  done

  echo -e "Data cleanse complete\n"

  for filetext in $( ls $filename/*.txt ); do
    python ../converter.py -i $filetext -o ../bin/
  done

  echo -e "Data export complete\n"
done

echo -e "\n\n==================================================================================================="
echo -e "\n`date` - Script: ${0} completed successfully - overall Elapsed Time: $(timer ${OVERALL_START_TIME})"

exit 0
