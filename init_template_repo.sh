echo "running initializatinons"
sleep 1

mkdir theory explorations
touch theory/.gitkeep explorations/explore.txt

for i in {1..5}; do
    echo "This is file $i" > file$i.txt
done
