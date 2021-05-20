cat _build/cleaned_build.log | 
grep "WARNING" | 
grep -vE "\.md:: WARNING: No footnote definitions found for label: '(.*)' \[myst\.footnote\]" |
grep -vE "WARNING: image file not readable: (.*)\.mmd\.png"