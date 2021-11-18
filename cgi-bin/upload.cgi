#!/usr/bin/perl -w
 
my $buffer;
my $pair;
read (STDIN, $buffer, $ENV{'CONTENT_LENGTH'});
@pairs = split(/&/, $buffer);
foreach $pair (@pairs) 
{
    ($name, $value) = split(/=/, $pair);
    $value =~ tr/+/ /;
    $value =~ s/%([a-fA-F0-9] [a-fA-F0-9])/pack("C", hex($1))/eg;
    $value =~ s/~!/ ~!/g;
    $FORM{$name} = $value;
}
   
if($FORM{python}) 
{
   $python_flag ="YES";
} 
else 
{
   $python_flag ="NO";
}
   
if($FORM{java}) 
{
   $java_flag ="YES";
}
else 
{
   $java_flag ="NO";
}
   
if($FORM{kotlin})
{
   $kotlin_flag ="YES";
} 
else
{
   $kotlin_flag ="NO";
}
   
if($FORM{perl}) 
{
   $perl_flag ="YES";
} 
else 
{
   $perl_flag ="NO";
}
   
if($FORM{c}) 
{
   $c_flag ="YES";
} 
else
{
   $c_flag ="NO";
}
   
$name= $FORM{'first_name'};
$mail= $FORM{'last_name'};
$work_location= $FORM{'payment'};
$Accept_to_adjust= $FORM{'first_time'};
$self_introduce= $FORM{'feedback'};
   
print "Content-type:text/html;charset=utf-8\r\n\r\n";
print "<html>";
print "<head>";
print "<title>GeeksForGeeks - Post Method</title>";
print "</head>";
print "<body>";
print "<h3>Hello $name $mail</h3>";
print "<h3>这是你的基本信息!</h3>";
print "<h3>Python: $python_flag</h3>";
print "<h3>Java: $java_flag</h3>";
print "<h3>Kotlin: $kotlin_flag</h3>";
print "<h3>Perl: $perl_flag</h3>";
print "<h3>C: $c_flag</h3>";
print "<h3>工作地点: $work_location</h3>";
print "<h3>是否接受调剂: $Accept_to_adjust</h3>";
print "<h3>自我介绍: $self_introduce</h3>";
print "</body>";
print "</html>";
   
1;
