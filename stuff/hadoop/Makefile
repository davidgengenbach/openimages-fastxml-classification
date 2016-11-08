INPUT=/Users/davidgengenbach/Desktop/Open-Images-downloader/download/machine_ann_2016_08/train
#INPUT=input
INPUT2=input2
OUTPUT=output
HADOOP_CLASSPATH=$(shell hadoop classpath)

run-normal: LabelCount.jar
	hadoop jar $< de.david.LabelCount $(INPUT2) $(OUTPUT)

run-clean: clean-input put_input_in_hdfs run-normal

LabelCount.jar: clean
	mkdir -p LabelCount_classes
	javac -classpath $(HADOOP_CLASSPATH) -d LabelCount_classes LabelCount.java  -d LabelCount_classes
	jar -cvf LabelCount.jar -C LabelCount_classes/ .

put_input_in_hdfs: clean
	hdfs dfs -put $(INPUT) $(INPUT2)

clean:
	rm -rf *.class *.jar LabelCount_classes/* output

clean-input:
	rm -rf $(INPUT2)