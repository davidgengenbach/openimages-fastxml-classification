#! /bin/sh

#SBATCH -D /nfs/cluster_files/dgengenbach/fast_xml
#SBATCH --time=9:00:00
#SBATCH -c 4
#SBATCH --mem=30G
#SBATCH -o output/job.all.%J.out
#SBATCH -e output/job.all.%J.err

timestamp=$(date +"%F__%R")

alias notify="echo $@"

notify "STARTING_SLURM__($timestamp)"
./run-cluster.sh train
notify "FINISHED_SLURM__TRAIN__($timestamp)"

./run-cluster.sh test
notify "FINISHED_SLURM__TEST__($timestamp)"

notify "FINISHED_SLURM__ALL__($timestamp)"
