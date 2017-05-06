for i in `seq 1 100`; do
	sbatch < tensorflow-vgg/scripts/slurm.sh
	sleep 0.4
done
