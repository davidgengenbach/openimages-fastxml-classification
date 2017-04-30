#! /bin/sh

#SBATCH -D /nfs/cluster_files/dgengenbach/fast_xml
#SBATCH --time=9:00:00
#SBATCH -c 4
#SBATCH --mem=30G
#SBATCH -o output/job.all.%J.out
#SBATCH -e output/job.all.%J.err

timestamp=$(date +"%F__%R")

alias email="/nfs/cluster_files/dgengenbach/email_notification.sh $@"

email "STARTING_SLURM__($timestamp)"
./run-cluster.sh train
email "FINISHED_SLURM__TRAIN__($timestamp)"

./run-cluster.sh test
email "FINISHED_SLURM__TEST__($timestamp)"

email "FINISHED_SLURM__ALL__($timestamp)"
