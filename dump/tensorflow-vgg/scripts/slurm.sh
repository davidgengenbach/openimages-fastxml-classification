#! /bin/sh

#SBATCH -D /nfs/cluster_files/dgengenbach/feature_extraction
#SBATCH --time=2:00:00
#SBATCH -c 2
#SBATCH -N 1-1
#SBATCH -o output/job.%J.out
#SBATCH -e output/job.%J.err
#SBATCH --mail-type=ALL
#SBATCH --mail-user=davidgengenbach@gmx.de

cd tensorflow-vgg
./run-cluster.sh
