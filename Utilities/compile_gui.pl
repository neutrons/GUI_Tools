#!/usr/bin/perl -w
use warnings;
use Getopt::Long qw(GetOptions);

my $input_folder = ".";
my $output_folder = ".";

# build *.py form *.ui 
GetOptions('file=s' => \$file,
           'input_folder=s' => \$input_folder,
           'ouput_folder=s' => \$output_folder,
           'help|h' => \$help,
           'verbose|v' => \$verbose
           ) or die "Usage: $0 -i=ui_folder -o=py_folder -v --help\n";

if ($help) {
    print "MANUAL \n=======\n";
    print " This script allows to compile a given ui file (if specified) all the UI files automatically\n\n";
    print "Examples:\n";
    print "  $0 -f=iu_file -o=py_folder\n";
    print "  $0 -i=ui_folder -o=py_folder\n";
    print "  $0 -i=ui_folder\n";
    print "  $0 --output_folder=py_folder -v\n";
    print "  $0 --help\n";
    print "  $0 -h\n\n";
    print "FLAGS \n-------\n";
    printf("  %-19s ui file created by Designer\n", "--file/-f:");
    printf("  %-19s folder that contains the ui files created with Desiger\n" ,"--input_folder/-i:");
    printf("  %-19s folder that will contain the py files created by pyuic4\n" ,"--output_folder/-o:");
    print "  --verbose-v: to display list of commands executed\n";
    print "  --help/-h: to display this help\n\n";
    exit 0;
}

if ($file) {

    check_file($file, "doesn't exist!");
    check_folder($output_folder);
    $_ = $file;
    ($full_base_name) = /(.*).ui/;
    @base_name = split('/', $full_base_name);
    $base_name = $base_name[-1];
    system("pyuic4 $file > $output_folder/$base_name.py");
    if ($verbose) { 
        print ">> pyuic4 $file > $output_folder/$base_name.py\n";

    }

} else {

    check_folders($input_folder, $output_folder);
    
    $input_folder = "$input_folder/*.ui";
    my @files = glob($input_folder);
    
    foreach my $file (@files) {
        $_ = $file;
        ($full_base_name) = /(.*).ui/;
        @base_name = split('/', $full_base_name);
        $base_name = $base_name[-1];
        system("pyuic4 $file > $output_folder/$base_name.py");
        if ($verbose) { 
            print ">> pyuic4 $file > $output_folder/$base_name.py\n";
        }
    }

}

exit 0;

sub check_folders
{
    my ($input_folder, $output_folder) = @_;
    check_folder($input_folder, "doesn't exist!");
    check_folder($output_folder, "doesn't exist and must be created first!");

#    -d $input_folder or die "$input_folder doesn't exist!";
#    -d $output_folder or die "$output_folder doesn't exist and must be created first!";
}

sub check_folder
{
    my ($folder, $message) = @_;
    -d $folder or die "$folder " . $message
}

sub check_file
{
    my ($file, $message) = @_;
    -e $file or die "$file" . $message;
}