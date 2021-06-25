# -*- coding: UTF-8 -*-
from sys import argv, exit
import typing

def print_help() -> None:
	print("""
        All Commands:
        
        1. C Commands:
             a. c program :: autogenerates a basic c program file structure
             b. c strlength :: autogenerates a basic function for getting the length of any string
             c. c whitespace :: autogenerates a basic function for checking if a given string contains unwanted keywords and spaces
             d. c strflip :: autogenerates a basic function for reversing the contents of a string
             e. c doequal :: autogenerates a basic function for checking if two strings equal eachother
             f. c strcon :: autogenerates a basic function for concatenating contents to a string
             g. c smart alloc :: autogenerates a basic function for rellocating a given string, while still keeping the current contents
             h. c trim :: autogenerates three basic functions: ltrim (for left trimming), rtrim (for right trimming), and trim (for both)
        
        2. HTML/Bootstrap Commands:
             a. html :: autogenerates a basic HTML 5 file structure with JQuery JS and Bootstrap CDNs linked
             b. top html :: autogenerates the top portion of a basic HTML 5 file structure (with JQuery JS and Bootstrap). Top portion is defined as from the top all the way to the beginning <body> tag.
             c. bottom html :: autogenerates the bottom portion of a basic HTML 5 file structure. The bottom portion is defined as the end body and html tags (</body> and </html>)
             d. table :: autogenerates a basic Bootstrap Table
             e. three columns :: autogenerates a basic Bootstrap three columned row
             f. two columns :: autogenerates a basic Bootstrap two columned row
             g. card :: autogenerates a basic Bootstrap Card
             h. breadcrumb :: autogenerates a basic Bootstrap Breadcrumb
             i. form :: autogenerates a basic Bootstrap Form
        
        3. PHP Commands:
             a. mysql connect :: autogenerates a basic PHP connection to a given Database (MySQL)
             b. mysql select :: autogenerates a basic mysql select statement (must connect to database first)
             c. logg :: autogenerates a useful logg() PHP function for JS console.log() (logging to the console)
             d. sql connect :: autogenerates a basic PHP connection to a given Database (SQL)
             e. sql select :: autogenerates a basic sql select statement (must connect to database first)
             f. sql insert :: autogenerates a basic sql insert statement (must connect to database first)
             g. php json pprint :: autogenerates a pretty print function for JSON
             h. php pprint :: autogenerates a generic pretty print function
        
        4. Bash Commands:
             a. sh header :: autogenerates the bash mandatory header code
             b. sh extract wifi :: autogenerates the getwifi bash script, which can be used to extract wifi passwords from saved passwords
             c. sh portscanner :: autogenerates a set of useful functions for scanning ports and ips on the same network as you (NOTE: nmap needs to be installed in order for this to work. DO NOT perform deep scans on other people's devices without permission!)
             d. sh list color :: autogenerates aliases for listing directories with color :: 'ls' becomes 'lc' and 'ls -a' becomes 'lca'
             e. sh fuckmac drives :: autogenerates aliases and functions that pertain to monitoring external/internal drive processes (and subprocesses). Also includes alternative methods of ejecting drives (such as slightlyMurder and Murder)
        
        5. C++ Commands:
             a. cpp program :: autogenerates a basic C++ program
        
        6. JavaScript Commands:
             a. js goto url :: autogenerates basic JS to change the current URL
             b. js prevent re-post :: autogenerates basic JS to prevent a user from accidentally re-posting a form via refreshing the page
             c. js button :: autogenerates a Bootstrap button that is connected to a JS function
             d. js snackbar :: autogenerates a raw snackbar for error/notice messages (timed messages)
             e. js weep :: autogenerates the anti-cookieware weep script, which can be injected into websites to combat unnecessary cookie tracking (such as google analytics).
        
        7. CSS Commands:
             a. css target firefox :: autogenerates code that allows you to perform CSS only when the user is usning FireFox
        
        8. Swift Commands:
             a. swift transition :: autogenerates the basic code to transition from one view controller to another
             b. swift tempurl :: autogenerates a swift function that can be used to generate temporary files on a target iPhone
        		""")

# Replace all occurances with corresponding replacements:
def replaceAll(line: str, occurances: list, replacements: list) -> str:
	for (occurance, replacement) in zip(occurances, replacements):
		line = line.replace(occurance, replacement)
	return line

# Define all the keywords:
keywords = (
	'$|c program|$', 
	'$|c strlength|$', 
	'$|c whitespace|$', 
	'$|c strflip|$', 
	'$|c doequal|$', 
	'$|c strcon|$', 
	'$|c smart alloc|$', 
	'$|c trim|$', 
	'$|html|$',
	'$|top html|$',
	'$|bottom html|$',
	'$|table|$',
	'$|three columns|$',
	'$|two columns|$',
	'$|card|$', 
	'$|breadcrumb|$',
	'$|form|$',
	'$|mysql connect|$',
	'$|mysql select|$',
	'$|logg|$',
	'$|sql connect|$',
	'$|sql select|$',
	'$|sql insert|$',
	'$|sh header|$',
	'$|sh extract wifi|$',
	'$|sh portscanner|$',
	'$|sh list color|$',
	'$|sh fuckmac drives|$',
	'$|cpp program|$',
	'$|js goto url|$',
	'$|js prevent re-post|$',
	'$|js button|$',
	'$|js snackbar|$',
	'$|js weep|$',
	'$|css target firefox|$',
	'$|swift transition|$',
	'$|swift tempurl|$',
	'$|php pprint|$',
	'$|php json pprint|$'
	)

# Define the replacements:
replacements = (
	'#include <stdio.h>\n#include <stdlib.h>\n\nint main(int argc, char * argv[]){\n\t// Insert code here\n\treturn 0;\n}\n',
	"int strlength(const char * str){\n\tint count = 1;\n\tfor(int x = 0; str[x] != '\\0'; x++)\n\t\tcount++;\n\treturn count - 1;\n}\n",
	"const char blank = ' ';\nconst char new_line = '\\n';\nconst char carraige_return = '\\r';\nconst char tab = '\\t';\nconst char form_feed = '\\f';\nconst char vertical_tab = '\\v';\n\nint check_for_whitespace(const char c){\n\tif(c == blank || c == new_line || c == carraige_return || c == tab || c == form_feed || c == vertical_tab)\n\t\treturn 1;\n\telse\n\t\treturn 0;\n}\n",
	"/** Requires strlength and <stdlib.h> **/\nchar * strflip(char * s){\n\tchar * new_string = (char *)calloc(1, sizeof(char));\n\tint count = 0;\n\tfor(int x = (strlength(s) - 1); x >= 0; x--){\n\t\tif(count != 0){ new_string = (char *)realloc(new_string, count + 1); }\n\t\tnew_string[count++] = s[x];\n\t}\n\treturn new_string;\n}\n",
	"/** Requires strlength **/\nint doequal(char * first_string, char * second_string){\n\tif(strlength(first_string) != strlength(second_string)){\n\t\treturn 0;\n\t} else {\n\t\tfor(int x = 0; x < strlength(first_string); x++){\n\t\t\tif(first_string[x] != second_string[x])\n\t\t\t\treturn 0;\n\t\t}\n\t\treturn 1;\n\t}\n}\n",
	"/** Requires strlength **/\nchar * strcon(char * destination, const char * source){\n\tchar * ptr = destination + strlength(destination);\n\n\twhile (*source != '\\0')\n\t\t*ptr++ = *source++;\n\n\t*ptr = '\\0';\n\n\treturn destination;\n}\n",
	"/** Requires strlength and <stdlib.h> **/\nchar * smart_realloc(char ** string, int new_size){\n\tchar * temp_string = (char *)calloc(strlength(*string), sizeof(char));\n\n\tfor (int x = 0; x < strlength(*string); x++)\n\t\ttemp_string[x] = (*string)[x];\n\n\t*string = (char *)realloc(*string, new_size);\n\n\tfor (int x = 0; x < strlength(temp_string); x++)\n\t\t(* string)[x] = temp_string[x];\n\n\treturn *string;\n}\n",
	"/** Requires strlength and whitespace **/\nchar * rtrim(char * s){\n\tchar * new_string = (char *)calloc(1, sizeof(char));\n\tint count = 0;\n\tint stop_checking = 0;\n\tfor(int x = (strlength(s) - 1); x >= 0; x--){\n\t\tif(stop_checking == 0){\n\t\t\tif(check_for_whitespace(s[x]) == 0){\n\t\t\t\tstop_checking = 1;\n\t\t\t\tif(count != 0){ new_string = (char *)realloc(new_string, count + 1); }\n\t\t\t\tnew_string[count++] = s[x];\n\t\t\t}\n\t\t} else {\n\t\t\tif(count != 0){ new_string = (char *)realloc(new_string, count + 1); }\n\t\t\tnew_string[count++] = s[x];\n\t\t}\n\t}\n\tnew_string = strflip(new_string);\n\treturn new_string;\n}\n\nchar * ltrim(char * s){\n\tchar * new_string = (char *)calloc(1, sizeof(char));\n\tint count = 0;\n\tint stop_checking = 0;\n\tfor(int x = 0; x < strlength(s); x++){\n\t\tif(stop_checking == 0){\n\t\t\tif(check_for_whitespace(s[x]) == 0){\n\t\t\t\tstop_checking = 1;\n\t\t\t\tif(count != 0){ new_string = (char *)realloc(new_string, count + 1); }\n\t\t\t\tnew_string[count++] = s[x];\n\t\t\t}\n\t\t} else {\n\t\t\tif(count != 0){ new_string = (char *)realloc(new_string, count + 1); }\n\t\t\tnew_string[count++] = s[x];\n\t\t}\n\t}\n\treturn new_string;\n}\n\nchar * trim(char * s){\n\ts = ltrim(s);\n\ts = rtrim(s);\n\treturn s;\n}\n",
	"<!DOCTYPE html>\n<html lang=\"en\">\n<head>\n\t<meta charset=\"UTF-8\">\n\t<meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">\n\t<title>Document</title>\n\t<script src=\"https://code.jquery.com/jquery-1.12.4.min.js\"></script>\n\t<link rel=\"stylesheet\" type=\"text/css\" crossorigin=\"anonymous\" href=\"https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/css/bootstrap.min.css\">\n\t<script src=\"https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/js/bootstrap.min.js\" crossorigin=\"anonymous\"></script>\n</head>\n<body>\n\n</body>\n</html>\n",
	"<!DOCTYPE html>\n<html lang=\"en\">\n<head>\n\t<meta charset=\"UTF-8\">\n\t<meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">\n\t<title>Document</title>\n\t<script src=\"https://code.jquery.com/jquery-1.12.4.min.js\"></script>\n\t<link rel=\"stylesheet\" type=\"text/css\" crossorigin=\"anonymous\" href=\"https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/css/bootstrap.min.css\">\n\t<script src=\"https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/js/bootstrap.min.js\" crossorigin=\"anonymous\"></script>\n</head>\n<body>\n",
	"</body>\n</html>\n",
	"<table class=\"table\">\n\t<thead>\n\t\t<tr>\n\t\t\t<th scope=\"col\">#</th>\n\t\t\t<th scope=\"col\">First</th>\n\t\t\t<th scope=\"col\">Last</th>\n\t\t\t<th scope=\"col\">Handle</th>\n\t\t</tr>\n\t</thead>\n\t<tbody>\n\t\t<tr>\n\t\t\t<th scope=\"row\">1</th>\n\t\t\t<td>Mark</td>\n\t\t\t<td>Otto</td>\n\t\t\t<td>@mdo</td>\n\t\t</tr>\n\t\t<tr>\n\t\t\t<th scope=\"row\">2</th>\n\t\t\t<td>Jacob</td>\n\t\t\t<td>Thornton</td>\n\t\t\t<td>@fat</td>\n\t\t</tr>\n\t\t<tr>\n\t\t\t<th scope=\"row\">3</th>\n\t\t\t<td>Larry</td>\n\t\t\t<td>the Bird</td>\n\t\t\t<td>@twitter</td>\n\t\t</tr>\n\t</tbody>\n</table>\n",
	"<div class=\"row\">\n\t<div class=\"col-sm-4\">\n\t\t<!-- Column 1 -->\n\t</div>\n\t<div class=\"col-sm-4\">\n\t\t<!-- Column 2 -->\n\t</div>\n\t<div class=\"col-sm-4\">\n\t\t<!-- Column 3 -->\n\t</div>\n</div>\n",
	"<div class=\"row\">\n\t<div class=\"col-sm-4\">\n\t\t<!-- Column 1 -->\n\t</div>\n\t<div class=\"col-sm-4\">\n\t\t<!-- Column 2 -->\n\t</div>\n</div>\n",
	"<div class=\"card\" style=\"width: 18rem;\">\n\t<img class=\"card-img-top\" src=\"...\" alt=\"Card image cap\">\n\t<div class=\"card-body\">\n\t\t<h5 class=\"card-title\">Card title</h5>\n\t\t<p class=\"card-text\">Some quick example text to build on the card title and make up the bulk of the card's content.</p>\n\t\t<a href=\"#\" class=\"btn btn-primary\">Go somewhere</a>\n\t</div>\n</div>\n",
	"<nav aria-label=\"breadcrumb\">\n\t<ol class=\"breadcrumb\">\n\t\t<li class=\"breadcrumb-item\"><a href=\"#\">Home</a></li>\n\t\t<li class=\"breadcrumb-item\"><a href=\"#\">Library</a></li>\n\t\t<li class=\"breadcrumb-item active\" aria-current=\"page\">Data</li>\n\t</ol>\n</nav>\n",
	"<form action=\"\" method=\"POST\">\n\t<div class=\"form-group\">\n\t\t<label for=\"exampleInputEmail1\">Email address</label>\n\t\t<input type=\"email\" class=\"form-control\" id=\"exampleInputEmail1\" aria-describedby=\"emailHelp\">\n\t\t<small id=\"emailHelp\" class=\"form-text text-muted\">We'll never share your email with anyone else.</small>\n\t</div>\n\t<div class=\"form-group\">\n\t\t<label for=\"exampleInputPassword1\">Password</label>\n\t\t<input type=\"password\" class=\"form-control\" id=\"exampleInputPassword1\">\n\t</div>\n\t<div class=\"form-group form-check\">\n\t\t<input type=\"checkbox\" class=\"form-check-input\" id=\"exampleCheck1\">\n\t\t<label class=\"form-check-label\" for=\"exampleCheck1\">Check me out</label>\n\t</div>\n\t<button type=\"submit\" class=\"btn btn-primary\">Submit</button>\n</form>\n",
	"\t$servername = \"localhost\";\n\t$username = \"username\";\n\t$password = \"password\";\n\t$dbname = \"myDB\";\n\n\t// Create connection\n\t$conn = new mysqli_connect($servername, $username, $password, $dbname);\n\n\t// Check connection\n\tif ($conn->connect_error) {\n\t\tdie(\"Connection failed: \" . $conn->connect_error);\n\t}\n",
	"\ttry {\n\t\t$params = array();\n\t\t$sql = \"SELECT column_name FROM table_name;\";\n\t\t$result = mysqli_query($conn, $sql);\n\t\tif (mysqli_num_rows($result) > 0){\n\t\t\twhile ($row = mysqli_fetch_assoc($result)){\n\t\t\t\t// Do something with the data\n\t\t\t}\n\t\t}\n\t} catch (Exception $e){\n\t\techo $e;\n\t}\n",
	"\tfunction logg($msg,$type = \"normal\"){\n\t\tif(strtolower($type) == \"normal\"){\n\t\t\techo \"<script> console.log('\".$msg.\"'); </script>\";\n\t\t} elseif (strtolower($type) == \"error\"){\n\t\t\techo \"<script> console.error('\".$msg.\"'); </script>\";\n\t\t} else {\n\t\t\techo \"<script> console.error('Type \".$type.\" is not recognized.'); </script>\";\n\t\t}\n\t}\n",
	"\t$serverName = \"serverName\";\n\t$connectionInfo = array(\"Database\"=>\"DatabaseName\", \"UID\"=>\"username\", \"PWD\"=>\"password\");\n\n\t$conn = sqlsrv_connect($server, $connectionInfo);\n\n\tif ($conn === false){\n\t\techo \"Failed.<br />\";\n\t\tdie (print_r(sqlsrv_errors(), true));\n\t}\n",
	"\ttry {\n\t\t$name = \"testName\";\n\t\t$params = array($name);\n\t\t$query = \"SELECT column_name FROM table_name WHERE column_name = ?;\";\n\n\t\t$values = array();\n\t\tif ($result = sqlsrv_query($conn, $query, $params)){\n\t\t\twhile ($row = sqlsrv_fetch_array($result, SQLSRV_FETCH_ASSOC)){\n\t\t\t\tif ($row === false){\n\t\t\t\t\tdie (print_r(sqlsrv_errors(), true));\n\t\t\t\t\t}\n\t\t\t\tarray_push($values, $row['column_name']);\n\t\t\t}\n\t\t}\n\t} catch (Exception $e){\n\t\techo $e;\n\t}\n",
	"\ttry {\n\t\t$a_value = \"BOB\";\n\t\t$another_value = \"BILLY\";\n\t\t$name = \"testName\";\n\t\t$params = array($a_value, $another_value, $name);\n\t\t$query = \"INSERT INTO table_name\n\t\t([column_name]\n\t\t,[another_column_name])\n\t\tVALUES (?, ?) WHERE column_name = ?;\";\n\n\t\tif ($result === false)){\n\t\t\t// Failed\n\t\t} else {\n\t\t\t// Success\n\t\t}\n\t} catch (Exception $e){\n\t\techo $e;\n\t}\n",
	"#!/bin/bash\n",
	"networksetup -listpreferredwirelessnetworks en0\n\nread -p \"Wifi: \" response\nsecurity find-generic-password -wa \"$response\"",
	"function getip() {\n\tif [[ $# -eq 0 ]] ; then\n\t\techo 'getIP Error: Must specify submask IP address.'\n\telse\n\t\tnmap -sP $1\n\tfi\n}\nfunction scanme() {\n\tif [[ $# -eq 0 ]] ; then\n\t\techo 'scanme Error: Must specify number of ports to scan.'\n\telse\n\t\tif [ \"$1\" = \"-a\" ]\n\t\tthen\n\t\t\tnmap -p 1-65535 localhost\n\t\telse\n\t\t\tif [[ $1 -le 65535 ]] ; then\n\t\t\t\tnmap -p 1-$1 localhost\n\t\t\telse\n\t\t\t\techo 'scanme Error: There are only 65,535 ports!'\n\t\t\tfi\n\t\tfi\n\tfi\n}\nfunction scanthem() {\n\tif [ $2 = \"\" ] ; then\n\t\techo 'scanthem Error: Must specify number of ports to scan and the IP address of target.'\n\telse\n\t\tif [ \"$1\" = \"-a\" ]\n\t\tthen\n\t\t\tnmap -p 1-65535 localhost\n\t\telse\n\t\t\tif [[ $1 -le 65535 ]] ; then\n\t\t\t\tnmap -p 1-$1 $2\n\t\t\telse\n\t\t\t\techo 'scanme Error: There are only 65,535 ports!'\n\t\t\tfi\n\t\tfi\n\tfi\n}\nfunction getport() {\n\tif [[ $# -eq 0 ]] ; then\n\t\techo 'getport Error: Must specify port to scan (i.e. tcp:100).'\n\telse\n\t\tsudo lsof -i $1\n\tfi\n}",
	"alias lc='ls -G'\nalias lca='ls -G -a'",
	"alias eject='sudo diskutil unmountDisk '\nalias murder='sudo diskutil unmount force '\nalias listen='sudo lsof '\nalias monitor='sudo lsof | grep '\nalias demolish='sudo kill -9 '\nfunction slightlyMurder() {\n\tif [ \"$1\" != \"\" ] ; then\n\t\twhile IFS= read -r line; do\n\t\t\tpids+=( \"$line\" )\n\t\tdone < <( sudo lsof | grep \"$1\" | awk '{print $2}' )\n\t\tfor i in \"${pids[@]}\"\n\t\tdo\n\t\t\t\tsudo kill -9 $i\n\t\tdone\n\t\techo 'Killed all known processes. Now trying to eject gracefully...'\n\t\teject \"$1\"\n\telse\n\t\techo 'slightlyMurder failed. Target not specified...'\n\tfi\n}",
	"#include <iostream>\n\nint main(int argc, char * argv[]){\n\t// Enter code here!\n\treturn 0;\n}\n",
	"window.location.href = \"someOtherURL.php\";\n",
	"window.history.replaceState(null, null, \"somePage.php\");\n",
	"<a type=\"button\" class=\"btn btn-outline-secondary\" onclick=\"f()\">Click Me</a>\n<script type=\"text/Javascript\">\n\tfunction f(){\n\n\t}\n</script>\n",
	"<!-- Put CSS in <head> -->\n<style>\n#snackbar {\n\tvisibility: hidden;\n\tmin-width: 250px;\n\tmax-width: 500px;\n\tmargin-left: auto;\n\tmargin-right: auto;\n\tbackground-color: #04de07;\n\tcolor: #fff;\n\ttext-align: center;\n\tborder-radius: 2px;\n\tpadding: 16px;\n\tposition: fixed;\n\tz-index: 1;\n\tleft: 0;\n\tright: 0;\n\tbottom: 30px;\n\tfont-size: 17px;\n}\n\n#snackbar.show {\n\tvisibility: visible;\n\t-webkit-animation: fadein 0.5s, fadeout 5s 2.5s;\n\tanimation: fadein 0.5s, fadeout 0.5s 2.5s;\n}\n\n@-webkit-keyframes fadein {\n\tfrom {bottom: 0; opacity: 0;}\n\tto {bottom: 30px; opacity: 1;}\n}\n\n@keyframes fadein {\n\tfrom {bottom: 0; opacity: 0;}\n\tto {bottom: 30px; opacity: 1;}\n}\n\n@-webkit-keyframes fadeout {\n\tfrom {bottom: 30px; opacity: 1;}\n\tto {bottom: 0; opacity: 0;}\n}\n\n@keyframes fadeout {\n\tfrom {bottom: 30px; opacity: 1;}\n\tto {bottom: 0; opacity: 0;}\n}\n</style>\n\t<div id=\"snackbar\"><b>Error 101:</b> This is a timed snackbar.<div style=\"display: inline;\" id=\"countdown\">4</div>s</div>\n\t<script type=\"text/Javascript\">\n\t\tfunction snackbar() {\n\t\t\tvar x = document.getElementById(\"snackbar\");\n\t\t\tx.className = \"show\";\n\t\t\tsetTimeout(function(){ x.className = x.className.replace(\"show\", \"\"); }, 3000);\n\t\t\ttime();\n\t\t}\n\n\t\tfunction time(){\n\t\t\tvar seconds;\n\t\t\tvar temp;\n\n\t\t\tfunction countdown() {\n\t\t\t\tseconds = document.getElementById('countdown').innerHTML;\n\t\t\t\tseconds = parseInt(seconds, 10);\n\n\t\t\t\tif (seconds == 1) {\n\t\t\t\t\ttemp = document.getElementById('countdown');\n\t\t\t\t\ttemp.innerHTML = \"4\";\n\t\t\t\t\treturn;\n\t\t\t\t}\n\n\t\t\t\tseconds--;\n\t\t\t\ttemp = document.getElementById('countdown');\n\t\t\t\ttemp.innerHTML = seconds;\n\t\t\t\ttimeoutMyOswego = setTimeout(countdown, 1000);\n\t\t\t}\n\n\t\t\tcountdown();\n\t\t}\n\t\t// Invoke with snackbar()\n\t</script>\n",
	"function createCookie(name,value,days,domain) {\nif (days) {\nvar date = new Date();\ndate.setTime(date.getTime()+(days*24*60*60*1000));\nvar expires = \"; expires=\"+date.toGMTString();\n}\nelse var expires = \"\";\nif (Array.isArray(domain)){\nfor (var i = 0; i < domain.length; i++){\ndocument.cookie = name+\"=\"+value+expires+\"; domain=\"+domain[i]+\"; path=/\";\n}\n} else {\ndocument.cookie = name+\"=\"+value+expires+\"; domain=\"+domain+\"; path=/\";\n}\n}\n\nfunction eraseCookie(name,domain) {\ncreateCookie(name,\"\",-1,domain);\n}\n\nfunction wage_war(domain){\nvar cookies = document.cookie.split(\";\");\nfor (var i = 0; i < cookies.length; i++){\nlet cookie = cookies[i].split(\"=\")[0];\nconsole.log(\"Attacking cooke = \'\"+cookie+\"\'...\");\neraseCookie(cookie,domain);\n}\nconsole.log(\"Updated Cookies: \");\nconsole.log(document.cookie.split(\";\"));\n}\n\n// By default, it will target google\'s services, but you can add others if you\'de like:\nconst typical_cookie_domains = [\'.accounts.google.com\', \'accounts.google.com\', \'.google.com\', \'.developers.google.com\', \'developers.google.com\', \'.gstatic.google.com\', \'.supersummary.com\'];",
	"@-moz-document url-prefix(){\n\t/* Target FireFox Here */\n}\n",
	"if #available(iOS 13.0, *) {\n\tlet ViewController = self.storyboard?.instantiateViewController(identifier: \"{name of view controller}\") as! UIViewController\n\t//Make the view controller full screen\n\tViewController.modalPresentationStyle = .fullScreen\n\tself.present(ViewController, animated: false, completion: nil)\n}",
	"func tempURL() -> URL? {\n\tlet directory = NSTemporaryDirectory() as NSString\n\n\tif directory != \"\" {\n\t\tlet path = directory.appendingPathComponent(NSUUID().uuidString + \".MOV\")\n\t\tlet urlPath = URL(fileURLWithPath: path)\n\t\tself.lastVideoTempURL = urlPath\n\t\treturn urlPath\n\t}\n\n\treturn nil\n}",
	"""
function prettyPrint($string, $level = 0){
    $formatted_string = "<pre>";
    for ($i = 0; $i < strlen($string); $i++){
        switch ($string[$i]){
            case '[': case '{':
                $level++;
                $formatted_string .= $string[$i]."\\n".appendTabs($level);
                break;
            case ',':
                $formatted_string .= $string[$i]."\\n".appendTabs($level);
                break;
            case ']': case '}':
                $level--;
                $formatted_string .= "\\n".appendTabs($level).$string[$i]."\\n".appendTabs($level);
                break;
            default:
                $formatted_string .= $string[$i];
        }
    }
    return $formatted_string."</pre>";
}

function appendTabs($numOfTabs){
    $string_of_tabs = '';
    for ($_ = 0; $_ < $numOfTabs; $_++){
        $string_of_tabs .= "\\t";
    }
    return $string_of_tabs;
}
	""",
	"""
	function prettyPrint( $json )
            {
                $result = '';
                $level = 0;
                $in_quotes = false;
                $in_escape = false;
                $ends_line_level = NULL;
                $json_length = strlen( $json );

                for( $i = 0; $i < $json_length; $i++ ) {
                    $char = $json[$i];
                    $new_line_level = NULL;
                    $post = "";
                    if( $ends_line_level !== NULL ) {
                        $new_line_level = $ends_line_level;
                        $ends_line_level = NULL;
                    }
                    if ( $in_escape ) {
                        $in_escape = false;
                    } else if( $char === '"' ) {
                        $in_quotes = !$in_quotes;
                    } else if( ! $in_quotes ) {
                        switch( $char ) {
                            case '}': case ']':
                                $level--;
                                $ends_line_level = NULL;
                                $new_line_level = $level;
                                break;

                            case '{': case '[':
                                $level++;
                            case ',':
                                $ends_line_level = $level;
                                break;

                            case ':':
                                $post = " ";
                                break;

                            case " ": case "\t": case "\n": case "\r":
                                $char = "";
                                $ends_line_level = $new_line_level;
                                $new_line_level = NULL;
                                break;
                        }
                    } else if ( $char === '\\' ) {
                        $in_escape = true;
                    }
                    if( $new_line_level !== NULL ) {
                        $result .= "\n".str_repeat( "\t", $new_line_level );
                    }
                    $result .= $char.$post;
                }

                return $result;
            }
          """
	)

try:
	FILE = argv[1] # @Constant
except Exception:
	print_help()
	exit(1)

# Read file and interpret lines:
lines = [] # Buffer
with open(FILE, 'r') as f:
	for line in f:
		line = replaceAll(line, keywords, replacements)
		lines.append(line)

f = open(FILE, 'w')
f.writelines(lines)
f.close()