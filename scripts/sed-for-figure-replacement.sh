find test -type f -name "*.md" -exec 
perl -0777  -pe 's/```{figure} (.*)\n---\nwidth: (.*)px\nalt: (.*)\nname: (.*)\n---\n(.*)\n```/```{figure} $1\nalt: $2\n```/igs' alpha.txt
{} \;

perl -ne 'print $_ if /```{figure} \.\/broads-duos.png/' ~/git/the-fair-cookbook/content/recipes/reusability/expressing-data-use.md

perl -p0e 's/```{figure} \.\/broads-duos.png\n--/figurereplace/smg' ~/git/the-fair-cookbook/content/recipes/reusability/expressing-data-use.md |less