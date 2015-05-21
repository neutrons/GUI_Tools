#!/usr/bin/perl -w
use warnings;
use Getopt::Long qw(GetOptions);

$input_folder = "./";
$output_folder = "./";

# build *.py form *.ui in the same folder
GetOptions('help|h' => \$help
           ) or die "Usage: $0 --help\n";

if ($help) {
    print "MANUAL \n=======\n";
    print "input_folder and output_folder variable \nmust be manually edited in $0\n";
    print "\next:\n";
    print "  $0 --help\n";
    print "  $0 -h\n\n";
    print "FLAGS \n-------\n";
    print "  --help/-h: to display this help\n\n";
    exit 0;
}

$input_folder = "$input_folder/*.ui";
my @files = glob($input_folder);

foreach my $file (@files) {
    $_ = $file;
    ($base_name) = /(.*).ui/;
    system("pyuic4 $file > $output_folder$base_name.py");
    print ">> pyuic4 $file > $output_folder$base_name.py\n";
}

exit 0;


