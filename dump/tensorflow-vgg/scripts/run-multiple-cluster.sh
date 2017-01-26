NUM_PROCESSES=2

for i in `seq 1 $NUM_PROCESSES`; do
    STAMP=$(date "+%Y%m%d_%H%M%S")
    echo "Starting process: $i/$NUM_PROCESSES ($STAMP)"
    LOG_PATH="/nfs/cluster_files/dgengenbach/feature_extraction/output/${STAMP}"
    nohup ./run-cluster.sh 2> "${LOG_PATH}.err" > "${LOG_PATH}.log" &
    sleep 50
done