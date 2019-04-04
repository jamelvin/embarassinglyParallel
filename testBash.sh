for i in {1..5} 
do 
  python test.py $i $((i+1)) &  
done 
wait
python sum.py
rm toSum.txt
