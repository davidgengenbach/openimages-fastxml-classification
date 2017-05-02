
# Tests
for i in in/*test_results.txt; do
    echo "############################## $i"
    ./metrics.py --in1 "in/classes.real.test.txt" --in2 "$i" | grep 'Precision'
    echo
    echo
done