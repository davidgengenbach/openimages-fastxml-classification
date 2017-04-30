#! /bin/sh

#SBATCH -D /nfs/cluster_files/dgengenbach/fast_xml
#SBATCH --time=5:00:00
#SBATCH -c 4
#SBATCH --mem=30G
#SBATCH -o output/job.test.%J.out
#SBATCH -e output/job.test.%J.err

./run-cluster.sh test
/nfs/cluster_files/dgengenbach/email_notification.sh "FINISHED_SLURM__TEST"
