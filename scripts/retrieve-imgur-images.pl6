###################################################################
#Description	: the-fair-cookbook project on GitHub. This script
#           	: parses the recipes directory and look for images
#           	: with imgur URLs. Using these URLs, we get a local
#           	: copy in the images directory and change the URLs in
#           	: the concerned files to the local images.
#Author     	: vassilios ioannidis
#Email      	: vassilios.ioannidis@sib.swiss
#Date        	: 22 September 2021
#Version     	: version 1.0
###################################################################

##### Task: transfer the images of recipes from imgur back to github
#1 - Get the imgur images urls from various GitHub files in 'the-fair-cookbook/content/recipes' and save them into a file
# Parse the files from the directory "the-fair-cookbook/content/recipes"
# >>grep -Ri 'https://i.imgur.com/' * > 20210922-imgur-images.txt
#
#2 - retrieve the images from imgur
#running the current raku (perl6) script will
## parse the above created file,
## download a local copy of every image into the 'images' directory and
## change all the links of the concerned recipes
#
#Notes:
#we look for URLs using https://i.imgur.com/XXX.[png|jpg|jpeg] where XXX is the filename and png, jpg and jpeg the format of the 'images'
#recipes files are assumed to be in MarkDown format

#adapt accordingly the two following variables
my $path = '/Users/vioannid/work/CURRENT/github/the-fair-cookbook/content/recipes/';
my $file = '20210922-imgur-images.txt';


my $io  = open $path~$file, :r;
my @fichier = "$io".IO.lines;

my $output_dir = $path~'images';
mkdir($output_dir);

my @imgur_urls;

for @fichier -> $line {
# add new image format if necessary - check the output for 'No url found for: '
  if ($line ~~ /.*(https\:\/\/i\.imgur\.com\/.*\.[png|jpg|jpeg]).*/) {
    my $image_url = $0.Str;
    push(@imgur_urls,$image_url);
  }
  else {
    say "No url found for: "~$line;
  }
}

get_imgur_images(@imgur_urls);


my @files_to_edit;

for @fichier -> $line {
  if ($line ~~ /^(.*\.md)\:.*/ ) {
    my $github_filename = $0.Str;
    push(@files_to_edit,$github_filename);
  }
}

for @files_to_edit.unique -> $f {
  slurp($path~$f).subst('https://i.imgur.com/', '/images/', :g) ==> spurt($path~$f)
}

sub get_imgur_images(@array_in) {
  my @imgur_urls_in = @array_in.unique;
  for @imgur_urls_in -> $url {
    my $filename = $url.IO.basename;
    # curl $url -o $output_dir/$filename
    my $query = "$url -o $output_dir" ~ '/' ~ $filename;
    qqx{curl $query};
  }
}

exit;
