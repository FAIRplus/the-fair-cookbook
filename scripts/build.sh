echo 'Install mermaid via npm'
npm install @mermaid-js/mermaid-cli

echo 'Record mermaid version'
./node_modules/.bin/mmdc -V
find . -iname "*.mmd" > list_of_all_mermaid_files

echo 'Search all mermaid files and record a list of them'
cat list_of_all_mermaid_files

echo 'Convert all mermaid files to pngs and svg'
cat list_of_all_mermaid_files | while read line; do echo $line && ./node_modules/.bin/mmdc -i $line -w 800 -o $line.png ; done
cat list_of_all_mermaid_files | while read line; do echo $line && ./node_modules/.bin/mmdc -i $line -w 1600 -o $line.hi-res.png ; done
cat list_of_all_mermaid_files | while read line; do echo $line && ./node_modules/.bin/mmdc -i $line -w 800 -o $line.lo-res.png ; done
cat list_of_all_mermaid_files | while read line; do echo $line && ./node_modules/.bin/mmdc -i $line -o $line.svg ; done

echo 'Cleanup intermediate files and removed node_modules'
rm list_of_all_mermaid_files
rm -rf ./node_modules

echo '{}' > _static/recipes.json

echo 'Build the book'
jb build . 2>&1 | tee ./build.log
grep "There was an error in building your book. Look above for the cause." ./build.log; test $? -eq 1
sed "s,\x1B\[[0-9;]*[a-zA-Z],,g" ./build.log > ./_build/cleaned_build.log
./scripts/extract-warnings.sh
