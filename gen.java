package autogenerate;
import java.io.FileWriter;
import java.io.File;
import java.io.IOException;
import java.util.Scanner;

class gen {
    public static void main(String[] args){
        String help_str = "/**"
 + "\n* All Commands:"
 + "\n* "
 + "\n* 1. C Commands:"
 + "\n*      a. c program :: autogenerates a basic c program file structure"
 + "\n*      b. c strlength :: autogenerates a basic function for getting the length of any string"
 + "\n*      c. c whitespace :: autogenerates a basic function for checking if a given string contains unwanted keywords and spaces"
 + "\n*      d. c strflip :: autogenerates a basic function for reversing the contents of a string"
 + "\n*      e. c doequal :: autogenerates a basic function for checking if two strings equal eachother"
 + "\n*      f. c strcon :: autogenerates a basic function for concatenating contents to a string"
 + "\n*      g. c smart alloc :: autogenerates a basic function for rellocating a given string, while still keeping the current contents"
 + "\n*      h. c trim :: autogenerates three basic functions: ltrim (for left trimming), rtrim (for right trimming), and trim (for both)"
 + "\n* "
 + "\n* 2. HTML/Bootstrap Commands:"
 + "\n*      a. html :: autogenerates a basic HTML 5 file structure with JQuery JS and Bootstrap CDNs linked"
 + "\n*      b. top html :: autogenerates the top portion of a basic HTML 5 file structure (with JQuery JS and Bootstrap). Top portion is defined as from the top all the way to the beginning <body> tag."
 + "\n*      c. bottom html :: autogenerates the bottom portion of a basic HTML 5 file structure. The bottom portion is defined as the end body and html tags (</body> and </html>)"
 + "\n*      d. table :: autogenerates a basic Bootstrap Table"
 + "\n*      e. three columns :: autogenerates a basic Bootstrap three columned row"
 + "\n*      f. two columns :: autogenerates a basic Bootstrap two columned row"
 + "\n*      g. card :: autogenerates a basic Bootstrap Card"
 + "\n*      h. breadcrumb :: autogenerates a basic Bootstrap Breadcrumb"
 + "\n*      i. form :: autogenerates a basic Bootstrap Form"
 + "\n* "
 + "\n* 3. PHP Commands:"
 + "\n*      a. mysql connect :: autogenerates a basic PHP connection to a given Database (MySQL)"
 + "\n*      b. mysql select :: autogenerates a basic mysql select statement (must connect to database first)"
 + "\n*      c. logg :: autogenerates a useful logg() PHP function for JS console.log() (logging to the console)"
 + "\n*      d. sql connect :: autogenerates a basic PHP connection to a given Database (SQL)"
 + "\n*      e. sql select :: autogenerates a basic sql select statement (must connect to database first)"
 + "\n*      f. sql insert :: autogenerates a basic sql insert statement (must connect to database first)"
 + "\n* "
 + "\n* 4. Bash Commands:"
 + "\n*      a. sh header :: autogenerates the bash mandatory header code"
 + "\n* "
 + "\n* 5. C++ Commands:"
 + "\n*      a. cpp program :: autogenerates a basic C++ program"
 + "\n* "
 + "\n* 6. JavaScript Commands:"
 + "\n*      a. js goto url :: autogenerates basic JS to change the current URL"
 + "\n*      b. js prevent re-post :: autogenerates basic JS to prevent a user from accidentally re-posting a form via refreshing the page"
 + "\n*      c. js button :: autogenerates a Bootstrap button that is connected to a JS function"
 + "\n*      d. js snackbar :: autogenerates a raw snackbar for error/notice messages (timed messages)"
 + "\n**/";
        if (args.length != 0){
            String auto_gen_code = "";
            if (args[0].toLowerCase().trim().equals("help")){
                System.out.print(help_str);
                System.exit(0);
            }
            try {
                File my_file = new File(args[0]);
                Scanner contents = new Scanner(my_file);

                while (contents.hasNextLine()){
                    String line_info = contents.nextLine();

                    if (line_info.toLowerCase().trim().equals("html")){
                        // Basic HTML structure with Bootstrap and JS (JQuery JS)
                        auto_gen_code += "<!DOCTYPE html>\n<html lang=\"en\">\n<head>\n\t<meta charset=\"UTF-8\">\n\t<meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">\n\t<title>Document</title>\n\t<script src=\"https://code.jquery.com/jquery-1.12.4.min.js\"></script>\n\t<link rel=\"stylesheet\" type=\"text/css\" crossorigin=\"anonymous\" href=\"https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/css/bootstrap.min.css\">\n\t<script src=\"https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/js/bootstrap.min.js\" crossorigin=\"anonymous\"></script>\n</head>\n<body>\n\n</body>\n</html>\n";
                    } else if (line_info.toLowerCase().trim().equals("top html")){
                        auto_gen_code += "<!DOCTYPE html>\n<html lang=\"en\">\n<head>\n\t<meta charset=\"UTF-8\">\n\t<meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">\n\t<title>Document</title>\n\t<script src=\"https://code.jquery.com/jquery-1.12.4.min.js\"></script>\n\t<link rel=\"stylesheet\" type=\"text/css\" crossorigin=\"anonymous\" href=\"https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/css/bootstrap.min.css\">\n\t<script src=\"https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/js/bootstrap.min.js\" crossorigin=\"anonymous\"></script>\n</head>\n<body>\n";
                    } else if (line_info.toLowerCase().trim().equals("mysql connect")){
                        auto_gen_code += "\t$servername = \"localhost\";\n\t$username = \"username\";\n\t$password = \"password\";\n\t$dbname = \"myDB\";\n\n\t// Create connection\n\t$conn = new mysqli_connect($servername, $username, $password, $dbname);\n\n\t// Check connection\n\tif ($conn->connect_error) {\n\t\tdie(\"Connection failed: \" . $conn->connect_error);\n\t}\n";
                    } else if (line_info.toLowerCase().trim().equals("table")){
                        auto_gen_code += "<table class=\"table\">\n\t<thead>\n\t\t<tr>\n\t\t\t<th scope=\"col\">#</th>\n\t\t\t<th scope=\"col\">First</th>\n\t\t\t<th scope=\"col\">Last</th>\n\t\t\t<th scope=\"col\">Handle</th>\n\t\t</tr>\n\t</thead>\n\t<tbody>\n\t\t<tr>\n\t\t\t<th scope=\"row\">1</th>\n\t\t\t<td>Mark</td>\n\t\t\t<td>Otto</td>\n\t\t\t<td>@mdo</td>\n\t\t</tr>\n\t\t<tr>\n\t\t\t<th scope=\"row\">2</th>\n\t\t\t<td>Jacob</td>\n\t\t\t<td>Thornton</td>\n\t\t\t<td>@fat</td>\n\t\t</tr>\n\t\t<tr>\n\t\t\t<th scope=\"row\">3</th>\n\t\t\t<td>Larry</td>\n\t\t\t<td>the Bird</td>\n\t\t\t<td>@twitter</td>\n\t\t</tr>\n\t</tbody>\n</table>\n";
                    } else if (line_info.toLowerCase().trim().equals("bottom html")){
                        auto_gen_code += "</body>\n</html>\n";
                    } else if (line_info.toLowerCase().trim().equals("three columns")){
                        auto_gen_code += "<div class=\"row\">\n\t<div class=\"col-sm-4\">\n\t\t<!-- Column 1 -->\n\t</div>\n\t<div class=\"col-sm-4\">\n\t\t<!-- Column 2 -->\n\t</div>\n\t<div class=\"col-sm-4\">\n\t\t<!-- Column 3 -->\n\t</div>\n</div>\n";
                    } else if (line_info.toLowerCase().trim().equals("two columns")){
                        auto_gen_code += "<div class=\"row\">\n\t<div class=\"col-sm-4\">\n\t\t<!-- Column 1 -->\n\t</div>\n\t<div class=\"col-sm-4\">\n\t\t<!-- Column 2 -->\n\t</div>\n</div>\n";
                    } else if (line_info.toLowerCase().trim().equals("card")){
                        auto_gen_code += "<div class=\"card\" style=\"width: 18rem;\">\n\t<img class=\"card-img-top\" src=\"...\" alt=\"Card image cap\">\n\t<div class=\"card-body\">\n\t\t<h5 class=\"card-title\">Card title</h5>\n\t\t<p class=\"card-text\">Some quick example text to build on the card title and make up the bulk of the card's content.</p>\n\t\t<a href=\"#\" class=\"btn btn-primary\">Go somewhere</a>\n\t</div>\n</div>\n";
                    } else if (line_info.toLowerCase().trim().equals("breadcrumb")){
                        auto_gen_code += "<nav aria-label=\"breadcrumb\">\n\t<ol class=\"breadcrumb\">\n\t\t<li class=\"breadcrumb-item\"><a href=\"#\">Home</a></li>\n\t\t<li class=\"breadcrumb-item\"><a href=\"#\">Library</a></li>\n\t\t<li class=\"breadcrumb-item active\" aria-current=\"page\">Data</li>\n\t</ol>\n</nav>\n";
                    } else if (line_info.toLowerCase().trim().equals("form")){
                        auto_gen_code += "<form action=\"\" method=\"POST\">\n\t<div class=\"form-group\">\n\t\t<label for=\"exampleInputEmail1\">Email address</label>\n\t\t<input type=\"email\" class=\"form-control\" id=\"exampleInputEmail1\" aria-describedby=\"emailHelp\">\n\t\t<small id=\"emailHelp\" class=\"form-text text-muted\">We'll never share your email with anyone else.</small>\n\t</div>\n\t<div class=\"form-group\">\n\t\t<label for=\"exampleInputPassword1\">Password</label>\n\t\t<input type=\"password\" class=\"form-control\" id=\"exampleInputPassword1\">\n\t</div>\n\t<div class=\"form-group form-check\">\n\t\t<input type=\"checkbox\" class=\"form-check-input\" id=\"exampleCheck1\">\n\t\t<label class=\"form-check-label\" for=\"exampleCheck1\">Check me out</label>\n\t</div>\n\t<button type=\"submit\" class=\"btn btn-primary\">Submit</button>\n</form>\n";
                    } else if (line_info.toLowerCase().trim().equals("c strlength")){
                        auto_gen_code += "int strlength(const char * str){\n\tint count = 1;\n\tfor(int x = 0; str[x] != '\\0'; x++)\n\t\tcount++;\n\treturn count - 1;\n}\n";
                    } else if (line_info.toLowerCase().trim().equals("c program")){
                        auto_gen_code += "#include <stdio.h>\n#include <stdlib.h>\n\nint main(int argc, char * argv[]){\n\t// Insert code here\n\treturn 0;\n}\n";
                    } else if (line_info.toLowerCase().trim().equals("c whitespace")){
                        auto_gen_code += "const char blank = ' ';\nconst char new_line = '\\n';\nconst char carraige_return = '\\r';\nconst char tab = '\\t';\nconst char form_feed = '\\f';\nconst char vertical_tab = '\\v';\n\nint check_for_whitespace(const char c){\n\tif(c == blank || c == new_line || c == carraige_return || c == tab || c == form_feed || c == vertical_tab)\n\t\treturn 1;\n\telse\n\t\treturn 0;\n}\n";
                    } else if (line_info.toLowerCase().trim().equals("c strflip")){
                        auto_gen_code += "/** Requires strlength and <stdlib.h> **/\nchar * strflip(char * s){\n\tchar * new_string = (char *)calloc(1, sizeof(char));\n\tint count = 0;\n\tfor(int x = (strlength(s) - 1); x >= 0; x--){\n\t\tif(count != 0){ new_string = (char *)realloc(new_string, count + 1); }\n\t\tnew_string[count++] = s[x];\n\t}\n\treturn new_string;\n}\n";
                    } else if (line_info.toLowerCase().trim().equals("c doequal")){
                        auto_gen_code += "/** Requires strlength **/\nint doequal(char * first_string, char * second_string){\n\tif(strlength(first_string) != strlength(second_string)){\n\t\treturn 0;\n\t} else {\n\t\tfor(int x = 0; x < strlength(first_string); x++){\n\t\t\tif(first_string[x] != second_string[x])\n\t\t\t\treturn 0;\n\t\t}\n\t\treturn 1;\n\t}\n}\n";
                    } else if (line_info.toLowerCase().trim().equals("c strcon")){
                        auto_gen_code += "/** Requires strlength **/\nchar * strcon(char * destination, const char * source){\n\tchar * ptr = destination + strlength(destination);\n\n\twhile (*source != '\\0')\n\t\t*ptr++ = *source++;\n\n\t*ptr = '\\0';\n\n\treturn destination;\n}\n";
                    } else if (line_info.toLowerCase().trim().equals("c smart realloc")){
                        auto_gen_code += "/** Requires strlength and <stdlib.h> **/\nchar * smart_realloc(char ** string, int new_size){\n\tchar * temp_string = (char *)calloc(strlength(*string), sizeof(char));\n\n\tfor (int x = 0; x < strlength(*string); x++)\n\t\ttemp_string[x] = (*string)[x];\n\n\t*string = (char *)realloc(*string, new_size);\n\n\tfor (int x = 0; x < strlength(temp_string); x++)\n\t\t(* string)[x] = temp_string[x];\n\n\treturn *string;\n}\n";
                    } else if (line_info.toLowerCase().trim().equals("c trim")){
                        auto_gen_code += "/** Requires strlength and whitespace **/\nchar * rtrim(char * s){\n\tchar * new_string = (char *)calloc(1, sizeof(char));\n\tint count = 0;\n\tint stop_checking = 0;\n\tfor(int x = (strlength(s) - 1); x >= 0; x--){\n\t\tif(stop_checking == 0){\n\t\t\tif(check_for_whitespace(s[x]) == 0){\n\t\t\t\tstop_checking = 1;\n\t\t\t\tif(count != 0){ new_string = (char *)realloc(new_string, count + 1); }\n\t\t\t\tnew_string[count++] = s[x];\n\t\t\t}\n\t\t} else {\n\t\t\tif(count != 0){ new_string = (char *)realloc(new_string, count + 1); }\n\t\t\tnew_string[count++] = s[x];\n\t\t}\n\t}\n\tnew_string = strflip(new_string);\n\treturn new_string;\n}\n\nchar * ltrim(char * s){\n\tchar * new_string = (char *)calloc(1, sizeof(char));\n\tint count = 0;\n\tint stop_checking = 0;\n\tfor(int x = 0; x < strlength(s); x++){\n\t\tif(stop_checking == 0){\n\t\t\tif(check_for_whitespace(s[x]) == 0){\n\t\t\t\tstop_checking = 1;\n\t\t\t\tif(count != 0){ new_string = (char *)realloc(new_string, count + 1); }\n\t\t\t\tnew_string[count++] = s[x];\n\t\t\t}\n\t\t} else {\n\t\t\tif(count != 0){ new_string = (char *)realloc(new_string, count + 1); }\n\t\t\tnew_string[count++] = s[x];\n\t\t}\n\t}\n\treturn new_string;\n}\n\nchar * trim(char * s){\n\ts = ltrim(s);\n\ts = rtrim(s);\n\treturn s;\n}\n";
                    } else if (line_info.toLowerCase().trim().equals("sh header")){
                        auto_gen_code += "#!/bin/bash\n";
                    } else if (line_info.toLowerCase().trim().equals("cpp program")){
                        auto_gen_code += "#include <iostream>\n\nint main(int argc, char * argv[]){\n\t// Enter code here!\n\treturn 0;\n}\n";
                    } else if (line_info.toLowerCase().trim().equals("js goto url")){
                        auto_gen_code += "window.location.href = \"someOtherURL.php\";\n";
                    } else if (line_info.toLowerCase().trim().equals("js prevent re-post")){
                        auto_gen_code += "window.history.replaceState(null, null, \"somePage.php\");\n";
                    } else if (line_info.toLowerCase().trim().equals("logg")){
                        auto_gen_code += "\tfunction logg($msg,$type = \"normal\"){\n\t\tif(strtolower($type) == \"normal\"){\n\t\t\techo \"<script> console.log('\".$msg.\"'); </script>\";\n\t\t} elseif (strtolower($type) == \"error\"){\n\t\t\techo \"<script> console.error('\".$msg.\"'); </script>\";\n\t\t} else {\n\t\t\techo \"<script> console.error('Type \".$type.\" is not recognized.'); </script>\";\n\t\t}\n\t}\n";
                    } else if (line_info.toLowerCase().trim().equals("js button")){
                        auto_gen_code += "<a type=\"button\" class=\"btn btn-outline-secondary\" onclick=\"f()\">Click Me</a>\n<script type=\"text/Javascript\">\n\tfunction f(){\n\n\t}\n</script>\n";
                    } else if (line_info.toLowerCase().trim().equals("sql connect")){
                        auto_gen_code += "\t$serverName = \"serverName\";\n\t$connectionInfo = array(\"Database\"=>\"DatabaseName\", \"UID\"=>\"username\", \"PWD\"=>\"password\");\n\n\t$conn = sqlsrv_connect($server, $connectionInfo);\n\n\tif ($conn === false){\n\t\techo \"Failed.<br />\";\n\t\tdie (print_r(sqlsrv_errors(), true));\n\t}\n";
                    } else if (line_info.toLowerCase().trim().equals("sql select")){
                        auto_gen_code += "\ttry {\n\t\t$name = \"testName\";\n\t\t$params = array($name);\n\t\t$query = \"SELECT column_name FROM table_name WHERE column_name = ?;\";\n\n\t\t$values = array();\n\t\tif ($result = sqlsrv_query($conn, $query, $params)){\n\t\t\twhile ($row = sqlsrv_fetch_array($result, SQLSRV_FETCH_ASSOC)){\n\t\t\t\tif ($row === false){\n\t\t\t\t\tdie (print_r(sqlsrv_errors(), true));\n\t\t\t\t\t}\n\t\t\t\tarray_push($values, $row['column_name']);\n\t\t\t}\n\t\t}\n\t} catch (Exception $e){\n\t\techo $e;\n\t}\n";
                    } else if (line_info.toLowerCase().trim().equals("sql insert")){
                        auto_gen_code += "\ttry {\n\t\t$a_value = \"BOB\";\n\t\t$another_value = \"BILLY\";\n\t\t$name = \"testName\";\n\t\t$params = array($a_value, $another_value, $name);\n\t\t$query = \"INSERT INTO table_name\n\t\t([column_name]\n\t\t,[another_column_name])\n\t\tVALUES (?, ?) WHERE column_name = ?;\";\n\n\t\tif ($result === false)){\n\t\t\t// Failed\n\t\t} else {\n\t\t\t// Success\n\t\t}\n\t} catch (Exception $e){\n\t\techo $e;\n\t}\n";
                    } else if (line_info.toLowerCase().trim().equals("js snackbar")){
                        auto_gen_code += "<!-- Put CSS in <head> -->\n<style>\n#snackbar {\n\tvisibility: hidden;\n\tmin-width: 250px;\n\tmax-width: 500px;\n\tmargin-left: auto;\n\tmargin-right: auto;\n\tbackground-color: #04de07;\n\tcolor: #fff;\n\ttext-align: center;\n\tborder-radius: 2px;\n\tpadding: 16px;\n\tposition: fixed;\n\tz-index: 1;\n\tleft: 0;\n\tright: 0;\n\tbottom: 30px;\n\tfont-size: 17px;\n}\n\n#snackbar.show {\n\tvisibility: visible;\n\t-webkit-animation: fadein 0.5s, fadeout 5s 2.5s;\n\tanimation: fadein 0.5s, fadeout 0.5s 2.5s;\n}\n\n@-webkit-keyframes fadein {\n\tfrom {bottom: 0; opacity: 0;}\n\tto {bottom: 30px; opacity: 1;}\n}\n\n@keyframes fadein {\n\tfrom {bottom: 0; opacity: 0;}\n\tto {bottom: 30px; opacity: 1;}\n}\n\n@-webkit-keyframes fadeout {\n\tfrom {bottom: 30px; opacity: 1;}\n\tto {bottom: 0; opacity: 0;}\n}\n\n@keyframes fadeout {\n\tfrom {bottom: 30px; opacity: 1;}\n\tto {bottom: 0; opacity: 0;}\n}\n</style>\n\t<div id=\"snackbar\"><b>Error 101:</b> This is a timed snackbar.<div style=\"display: inline;\" id=\"countdown\">4</div>s</div>\n\t<script type=\"text/Javascript\">\n\t\tfunction snackbar() {\n\t\t\tvar x = document.getElementById(\"snackbar\");\n\t\t\tx.className = \"show\";\n\t\t\tsetTimeout(function(){ x.className = x.className.replace(\"show\", \"\"); }, 3000);\n\t\t\ttime();\n\t\t}\n\n\t\tfunction time(){\n\t\t\tvar seconds;\n\t\t\tvar temp;\n\n\t\t\tfunction countdown() {\n\t\t\t\tseconds = document.getElementById('countdown').innerHTML;\n\t\t\t\tseconds = parseInt(seconds, 10);\n\n\t\t\t\tif (seconds == 1) {\n\t\t\t\t\ttemp = document.getElementById('countdown');\n\t\t\t\t\ttemp.innerHTML = \"4\";\n\t\t\t\t\treturn;\n\t\t\t\t}\n\n\t\t\t\tseconds--;\n\t\t\t\ttemp = document.getElementById('countdown');\n\t\t\t\ttemp.innerHTML = seconds;\n\t\t\t\ttimeoutMyOswego = setTimeout(countdown, 1000);\n\t\t\t}\n\n\t\t\tcountdown();\n\t\t}\n\t\t// Invoke with snackbar()\n\t</script>\n";
                    } else if (line_info.toLowerCase().trim().equals("mysql select")){
                        auto_gen_code += "\ttry {\n\t\t$params = array();\n\t\t$sql = \"SELECT column_name FROM table_name;\";\n\t\t$result = mysqli_query($conn, $sql);\n\t\tif (mysqli_num_rows($result) > 0){\n\t\t\twhile ($row = mysqli_fetch_assoc($result)){\n\t\t\t\t// Do something with the data\n\t\t\t}\n\t\t}\n\t} catch (Exception $e){\n\t\techo $e;\n\t}\n";
                    } else {
                        // Just keep current file contents if no command found
                        auto_gen_code += line_info;
                    }
                }

                contents.close();
            } catch (IOException e){
                System.out.println("ERROR: File not found.");
            }

            try {
                FileWriter my_file = new FileWriter(args[0]);
                my_file.write(auto_gen_code);
                my_file.close();
            } catch (IOException e){
                System.out.println("ERROR: File not found.");
            }
        } else {
            System.out.println("ERROR: File name was not given.");
        }
    }
}