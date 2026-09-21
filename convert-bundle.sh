#!/bin/bash
set -euo pipefail

curl "https://s3.amazonaws.com/ds2002-resources/labs/lab3-bundle.tar.gz" | tar -x -z -f -
awk '!/^[[:space:]]*$/' lab3_data.tsv >> cleaned.tsv
sed -i 's/\t/,/g' cleaned.tsv
lines=$(($(wc -l < cleaned.tsv)-1))
echo "lines"
tar -czf converted-archive.tar.gz cleaned.tsv


