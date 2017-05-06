#!/usr/bin/env bash

images_count=$(wc -l < images.txt)

while true; do
	if [ "`which squeue`" != '' ]; then
		job_count=$(squeue --noheader -u dgengenbach | wc -l)
	else
		job_count="(not on slurm cluster)"
	fi

	done_count=$(wc -l < done.txt)
	percent_done=`python3 -c "print(round($done_count / $images_count * 100, 1))"`
	py_count=$(pgrep python3 | wc -l)
	time_left="$(./scripts/get_time_left.py)"
	clear
	echo -e "Jobs\t$job_count"
	echo -e "py3\t$py_count"
	echo
	echo -e "Done\t$done_count"
	echo -e "Total\t$images_count"
	echo -e "Done %\t$percent_done"
	echo
	echo "$time_left"
	sleep 5
done
