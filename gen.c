#include <stdio.h>
#include <stdlib.h>
typedef const char cc;

/**
 * All Commands:
 * 
 * 1. C Commands:
 *      a. c program :: autogenerates a basic c program file structure
 *      b. c strlength :: autogenerates a basic function for getting the length of any string
 *      c. c whitespace :: autogenerates a basic function for checking if a given string contains unwanted keywords and spaces
 *      d. c strflip :: autogenerates a basic function for reversing the contents of a string
 *      e. c doequal :: autogenerates a basic function for checking if two strings equal eachother
 *      f. c strcon :: autogenerates a basic function for concatenating contents to a string
 *      g. c smart alloc :: autogenerates a basic function for rellocating a given string, while still keeping the current contents
 * 
 * 2. HTML/Bootstrap Commands:
 *      a. html :: autogenerates a basic HTML 5 file structure with JQuery JS and Bootstrap CDNs linked
 *      b. top html :: autogenerates the top portion of a basic HTML 5 file structure (with JQuery JS and Bootstrap). Top portion is defined as from the top all the way to the beginning <body> tag.
 *      c. bottom html :: autogenerates the bottom portion of a basic HTML 5 file structure. The bottom portion is defined as the end body and html tags (</body> and </html>)
 *      d. table :: autogenerates a basic Bootstrap Table
 *      e. three columns :: autogenerates a basic Bootstrap three columned row
 *      f. two columns :: autogenerates a basic Bootstrap two columned row
 *      g. card :: autogenerates a basic Bootstrap Card
 *      h. breadcrumb :: autogenerates a basic Bootstrap Breadcrumb
 *      i. form :: autogenerates a basic Bootstrap Form
 * 
 * 3. PHP Commands:
 *      a. connect database :: autogenerates a basic PHP connection to a given Database
 *      b. mysql select :: autogenerates a basic mysql select statement (must connect to database first)
 **/

cc blank = ' ';
cc new_line = '\n';
cc carraige_return = '\r';
cc tab = '\t';
cc form_feed = '\f';
cc vertical_tab = '\v';

int strlength(cc * str) 
{  
    int count = 1;
    for(int x = 0; str[x] != '\0'; x++)
        count++;
    return count - 1;
} 

int check_for_whitespace(cc c){
    if(c == blank || c == new_line || c == carraige_return || c == tab || c == form_feed || c == vertical_tab)
        return 1;
    else
        return 0;
}

char * strflip(char * s){
    char * new_string = (char *)calloc(1, sizeof(char));
    int count = 0;
    for(int x = (strlength(s) - 1); x >= 0; x--){
        if(count != 0){ new_string = (char *)realloc(new_string, count + 1); }
        new_string[count++] = s[x];
    }
    return new_string;
}

char * rtrim(char * s){
    char * new_string = (char *)calloc(1, sizeof(char));
    int count = 0;
    int stop_checking = 0;
    for(int x = (strlength(s) - 1); x >= 0; x--){
        if(stop_checking == 0){
            if(check_for_whitespace(s[x]) == 0){
                stop_checking = 1;
                if(count != 0){ new_string = (char *)realloc(new_string, count + 1); }
                new_string[count++] = s[x];
            }
        } else {
            if(count != 0){ new_string = (char *)realloc(new_string, count + 1); }
            new_string[count++] = s[x];
        }
    }
    new_string = strflip(new_string);
    return new_string;
}

char * ltrim(char * s){
    char * new_string = (char *)calloc(1, sizeof(char));
    int count = 0;
    int stop_checking = 0;
    for(int x = 0; x < strlength(s); x++){
        if(stop_checking == 0){
            if(check_for_whitespace(s[x]) == 0){
                stop_checking = 1;
                if(count != 0){ new_string = (char *)realloc(new_string, count + 1); }
                new_string[count++] = s[x];
            }
        } else {
            if(count != 0){ new_string = (char *)realloc(new_string, count + 1); }
            new_string[count++] = s[x];
        }
    }
    return new_string;
}

char * trim(char * s){
    s = ltrim(s);
    s = rtrim(s);
    return s;
}

int doequal(char * first_string, char * second_string){
    if(strlength(first_string) != strlength(second_string)){
        return 0;
    } else {
        for(int x = 0; x < strlength(first_string); x++){
            if(first_string[x] != second_string[x])
                return 0;
        }
        return 1;
    }
}

char * strcon(char * destination, const char * source){
    char * ptr = destination + strlength(destination);

    while (*source != '\0')
        *ptr++ = *source++;
    
    *ptr = '\0';

    return destination;
}

char * smart_realloc(char ** string, int new_size){
    char * temp_string = (char *)calloc(strlength(*string), sizeof(char));

    for (int x = 0; x < strlength(*string); x++)
        temp_string[x] = (*string)[x];
    
    *string = (char *)realloc(*string, new_size);

    for (int x = 0; x < strlength(temp_string); x++)
        (* string)[x] = temp_string[x];

    return *string;
}

int main(int argc, char * argv[]){
    if(argc > 1){
        char * target_file = argv[1];
        char file_contents[2000];
        char * auto_gen_code = (char *)calloc(1, sizeof(char));
        
        if (auto_gen_code == NULL){
            printf("ERROR: Failed to allocate auto_gen_code correctly.\n");
            return 1;
        }

        FILE * my_file;
        my_file = fopen(target_file, "r");

        // Check if file was opened correctly
        if (my_file == NULL){
            printf("ERROR: Failed to open file.\n");
            return 1;
        }

        while (fgets (file_contents, 2000, my_file) != NULL){
            if(doequal(trim(file_contents), "html") == 1){
                // basic html structure (with JS and Bootstrap)
                smart_realloc(&auto_gen_code, strlength(auto_gen_code) + 529);
                strcon(auto_gen_code, "<!DOCTYPE html>\n<html lang=\"en\">\n<head>\n\t<meta charset=\"UTF-8\">\n\t<meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">\n\t<title>Document</title>\n\t<script src=\"https://code.jquery.com/jquery-1.12.4.min.js\"></script>\n\t<link rel=\"stylesheet\" type=\"text/css\" crossorigin=\"anonymous\" href=\"https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/css/bootstrap.min.css\">\n\t<script src=\"https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/js/bootstrap.min.js\" crossorigin=\"anonymous\"></script>\n</head>\n<body>\n\n</body>\n</html>\n");
            } else if (doequal(trim(file_contents), "top html") == 1){
                // top portion of html basic structure (with JS and Bootstrap)
                smart_realloc(&auto_gen_code, strlength(auto_gen_code) + 512);
                strcon(auto_gen_code, "<!DOCTYPE html>\n<html lang=\"en\">\n<head>\n\t<meta charset=\"UTF-8\">\n\t<meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">\n\t<title>Document</title>\n\t<script src=\"https://code.jquery.com/jquery-1.12.4.min.js\"></script>\n\t<link rel=\"stylesheet\" type=\"text/css\" crossorigin=\"anonymous\" href=\"https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/css/bootstrap.min.css\">\n\t<script src=\"https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/js/bootstrap.min.js\" crossorigin=\"anonymous\"></script>\n</head>\n<body>\n");
            } else if (doequal(trim(file_contents), "connect database") == 1){
                // php connection to database
                smart_realloc(&auto_gen_code, strlength(auto_gen_code) + 301);
                strcon(auto_gen_code, "\t$servername = \"localhost\";\n\t$username = \"username\";\n\t$password = \"password\";\n\t$dbname = \"myDB\";\n\n\t// Create connection\n\t$conn = new mysqli_connect($servername, $username, $password, $dbname);\n\n\t// Check connection\n\tif ($conn->connect_error) {\n\t\tdie(\"Connection failed: \" . $conn->connect_error);\n\t}\n");
            } else if (doequal(trim(file_contents), "table") == 1){
                // bootstrap table
                smart_realloc(&auto_gen_code, strlength(auto_gen_code) + 491);
                strcon(auto_gen_code, "<table class=\"table\">\n\t<thead>\n\t\t<tr>\n\t\t\t<th scope=\"col\">#</th>\n\t\t\t<th scope=\"col\">First</th>\n\t\t\t<th scope=\"col\">Last</th>\n\t\t\t<th scope=\"col\">Handle</th>\n\t\t</tr>\n\t</thead>\n\t<tbody>\n\t\t<tr>\n\t\t\t<th scope=\"row\">1</th>\n\t\t\t<td>Mark</td>\n\t\t\t<td>Otto</td>\n\t\t\t<td>@mdo</td>\n\t\t</tr>\n\t\t<tr>\n\t\t\t<th scope=\"row\">2</th>\n\t\t\t<td>Jacob</td>\n\t\t\t<td>Thornton</td>\n\t\t\t<td>@fat</td>\n\t\t</tr>\n\t\t<tr>\n\t\t\t<th scope=\"row\">3</th>\n\t\t\t<td>Larry</td>\n\t\t\t<td>the Bird</td>\n\t\t\t<td>@twitter</td>\n\t\t</tr>\n\t</tbody>\n</table>\n");
            } else if (doequal(trim(file_contents), "bottom html") == 1){
                smart_realloc(&auto_gen_code, strlength(auto_gen_code) + 17);
                // end of body and html tags
                strcon(auto_gen_code, "</body>\n</html>\n");
            } else if (doequal(trim(file_contents), "three columns") == 1){
                // bootstrap three columned row
                smart_realloc(&auto_gen_code, strlength(auto_gen_code) + 182);
                strcon(auto_gen_code, "<div class=\"row\">\n\t<div class=\"col-sm-4\">\n\t\t<!-- Column 1 -->\n\t</div>\n\t<div class=\"col-sm-4\">\n\t\t<!-- Column 2 -->\n\t</div>\n\t<div class=\"col-sm-4\">\n\t\t<!-- Column 3 -->\n\t</div>\n</div>\n");
            } else if (doequal(trim(file_contents), "two columns") == 1){
                // bootstrap two columned row
                smart_realloc(&auto_gen_code, strlength(auto_gen_code) + 130);
                strcon(auto_gen_code, "<div class=\"row\">\n\t<div class=\"col-sm-4\">\n\t\t<!-- Column 1 -->\n\t</div>\n\t<div class=\"col-sm-4\">\n\t\t<!-- Column 2 -->\n\t</div>\n</div>\n");
            } else if (doequal(trim(file_contents), "card") == 1){
                // bootstrap card
                smart_realloc(&auto_gen_code, strlength(auto_gen_code) + 359);
                strcon(auto_gen_code, "<div class=\"card\" style=\"width: 18rem;\">\n\t<img class=\"card-img-top\" src=\"...\" alt=\"Card image cap\">\n\t<div class=\"card-body\">\n\t\t<h5 class=\"card-title\">Card title</h5>\n\t\t<p class=\"card-text\">Some quick example text to build on the card title and make up the bulk of the card's content.</p>\n\t\t<a href=\"#\" class=\"btn btn-primary\">Go somewhere</a>\n\t</div>\n</div>\n");
            } else if (doequal(trim(file_contents), "mysql select") == 1){
                // mysql select statement
                smart_realloc(&auto_gen_code, strlength(auto_gen_code) + 282);
                strcon(auto_gen_code, "\ttry {\n\t\t$params = array();\n\t\t$sql = \"SELECT column_name FROM table_name;\";\n\t\t$result = mysqli_query($conn, $sql);\n\t\tif (mysqli_num_rows($result) > 0){\n\t\t\twhile ($row = mysqli_fetch_assoc($result)){\n\t\t\t\t// Do something with the data\n\t\t\t}\n\t\t}\n\t} catch (Exception $e){\n\t\techo $e;\n\t}\n");
            } else if (doequal(trim(file_contents), "breadcrumb") == 1){
                // breadcrumb
                smart_realloc(&auto_gen_code, strlength(auto_gen_code) + 252);
                strcon(auto_gen_code, "<nav aria-label=\"breadcrumb\">\n\t<ol class=\"breadcrumb\">\n\t\t<li class=\"breadcrumb-item\"><a href=\"#\">Home</a></li>\n\t\t<li class=\"breadcrumb-item\"><a href=\"#\">Library</a></li>\n\t\t<li class=\"breadcrumb-item active\" aria-current=\"page\">Data</li>\n\t</ol>\n</nav>\n");
            } else if (doequal(trim(file_contents), "form") == 1){
                // form
                smart_realloc(&auto_gen_code, strlength(auto_gen_code) + 750);
                strcon(auto_gen_code, "<form action=\"\" method=\"POST\">\n\t<div class=\"form-group\">\n\t\t<label for=\"exampleInputEmail1\">Email address</label>\n\t\t<input type=\"email\" class=\"form-control\" id=\"exampleInputEmail1\" aria-describedby=\"emailHelp\">\n\t\t<small id=\"emailHelp\" class=\"form-text text-muted\">We'll never share your email with anyone else.</small>\n\t</div>\n\t<div class=\"form-group\">\n\t\t<label for=\"exampleInputPassword1\">Password</label>\n\t\t<input type=\"password\" class=\"form-control\" id=\"exampleInputPassword1\">\n\t</div>\n\t<div class=\"form-group form-check\">\n\t\t<input type=\"checkbox\" class=\"form-check-input\" id=\"exampleCheck1\">\n\t\t<label class=\"form-check-label\" for=\"exampleCheck1\">Check me out</label>\n\t</div>\n\t<button type=\"submit\" class=\"btn btn-primary\">Submit</button>\n</form>\n");
            } else if (doequal(trim(file_contents), "c strlength") == 1){
                // strlength
                smart_realloc(&auto_gen_code, strlength(auto_gen_code) + 118);
                strcon(auto_gen_code, "int strlength(const char * str){\n\tint count = 1;\n\tfor(int x = 0; str[x] != '\\0'; x++)\n\t\tcount++;\n\treturn count - 1;\n}\n");
            } else if (doequal(trim(file_contents), "c program") == 1){
                // basic C program structure
                smart_realloc(&auto_gen_code, strlength(auto_gen_code) + 118);
                strcon(auto_gen_code, "#include <stdio.h>\n#include <stdlib.h>\n\nint main(int argc, char * argv[]){\n\t// Insert code here\n\treturn 0;\n}\n");
            } else if (doequal(trim(file_contents), "c whitespace") == 1){
                // basic C program structure
                smart_realloc(&auto_gen_code, strlength(auto_gen_code) + 297);
                strcon(auto_gen_code, "const char blank = ' ';\nconst char new_line = '\\n';\nconst char carraige_return = '\\r';\nconst char tab = '\\t';\nconst char form_feed = '\\f';\nconst char vertical_tab = '\\v';\n\nint check_for_whitespace(const char c){\n\tif(c == blank || c == new_line || c == carraige_return || c == tab || c == form_feed || c == vertical_tab)\n\t\treturn 1;\n\telse\n\t\treturn 0;\n}\n");
            } else if (doequal(trim(file_contents), "c strflip") == 1){
                // basic C program structure
                smart_realloc(&auto_gen_code, strlength(auto_gen_code) + 272);
                strcon(auto_gen_code, "char * strflip(char * s){\n\tchar * new_string = (char *)calloc(1, sizeof(char));\n\tint count = 0;\n\tfor(int x = (strlength(s) - 1); x >= 0; x--){\n\t\tif(count != 0){ new_string = (char *)realloc(new_string, count + 1); }\n\t\tnew_string[count++] = s[x];\n\t}\n\treturn new_string;\n}\n");
            } else if (doequal(trim(file_contents), "c doequal") == 1){
                // basic C program structure
                smart_realloc(&auto_gen_code, strlength(auto_gen_code) + 267);
                strcon(auto_gen_code, "int doequal(char * first_string, char * second_string){\n\tif(strlength(first_string) != strlength(second_string)){\n\t\treturn 0;\n\t} else {\n\t\tfor(int x = 0; x < strlength(first_string); x++){\n\t\t\tif(first_string[x] != second_string[x])\n\t\t\t\treturn 0;\n\t\t}\n\t\treturn 1;\n\t}\n}\n");
            } else if (doequal(trim(file_contents), "c strcon") == 1){
                // basic C program structure
                smart_realloc(&auto_gen_code, strlength(auto_gen_code) + 194);
                strcon(auto_gen_code, "char * strcon(char * destination, const char * source){\n\tchar * ptr = destination + strlength(destination);\n\n\twhile (*source != '\\0')\n\t\t*ptr++ = *source++;\n\n\t*ptr = '\\0';\n\n\treturn destination;\n}\n");
            } else if (doequal(trim(file_contents), "c smart realloc") == 1){
                // basic C program structure
                smart_realloc(&auto_gen_code, strlength(auto_gen_code) + 358);
                strcon(auto_gen_code, "char * smart_realloc(char ** string, int new_size){\n\tchar * temp_string = (char *)calloc(strlength(*string), sizeof(char));\n\n\tfor (int x = 0; x < strlength(*string); x++)\n\t\ttemp_string[x] = (*string)[x];\n\n\t*string = (char *)realloc(*string, new_size);\n\n\tfor (int x = 0; x < strlength(temp_string); x++)\n\t\t(* string)[x] = temp_string[x];\n\n\treturn *string;\n}\n");
            } else {
                // if no command found, just re-display the current contents of that line
                smart_realloc(&auto_gen_code, strlength(auto_gen_code) + 2000);
                strcon(auto_gen_code, file_contents);
            }
        }

        fclose(my_file);
        my_file = fopen(target_file, "w");

        // Check if file was opened correctly
        if (my_file == NULL){
            printf("ERROR: Failed to open file.");
            return 1;
        }

        //printf("%s\n", auto_gen_code);
        fprintf(my_file, auto_gen_code, 0);

        fclose(my_file);
    } else {
        printf("ERROR: Must specify file to auto-generate.");
    }

    return 0;
}