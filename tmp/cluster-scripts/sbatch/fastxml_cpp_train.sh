#! /bin/sh

#SBATCH -D /nfs/cluster_files/dgengenbach/fast_xml
#SBATCH --time=5:00:00
#SBATCH -c 4
#SBATCH --mem=30G
#SBATCH -o output/job.train.%J.out
#SBATCH -e output/job.train.%J.err

./run-cluster.sh train
/nfs/cluster_files/dgengenbach/email_notification.sh "FINISHED_SLURM__TRAIN"
