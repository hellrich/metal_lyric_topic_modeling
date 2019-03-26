for topic in 4 8 9 38 31 13 22 29 45 39 46 34 48 40 36 16 
do
	echo $topic
	python examples-for-topic.py per_band_results_final_50/doc-topics-1 $topic --format
done
