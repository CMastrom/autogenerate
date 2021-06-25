# Autogenerate
This tiny but efficient C program allows you to autogenerate code in your program files. 

## Usage
- Add alias to profile file (.bash_profile for bash, .zsh for zshell, etc): alias gen='python3 {path_to_gen}/autogenerate/gen.py'
- Run gen: 
**%**  gen some_file.extension

### Basic Example
**%** nano test.c  
$|c program|$  
**%** gen test.c  
**%** cat test.c  
#include <stdio.h>  
#include <stdlib.h>  
  
int main(int argc, char * argv[]){  
	// Insert code here  
	return 0;  
}

