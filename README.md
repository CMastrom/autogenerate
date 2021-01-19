# autogenerate
This tiny but efficient C program allows you to autogenerate code in your program files. It can be used to autogenerate PHP, HTML 5, Bootstrap, C, and others very soon! 

Create an alias to wherever you put the gen executable (not the gen.c file) called 'gen', and whenever you want to generate some code in a given file, just simply navigate to the files directory in Terminal and run 'gen file_name.file_extension'.
If you are a windows user, you might have to re-compile the source C code to be able to use, and then create an alias pointing to that gen executable. That is why I uploaded the gen executable (potentially only compiled for MAC) and gen.c source file (can be compiled to anything).


Instructions:
If using bash:
    Insert this into your .bash_profile file located ~/.bash_profile: alias gen='/{full_path_to_this_cloned_repository}/autogenerate/./gen'
If using zshell (if your terminal displays:
    Insert this into your .zshrc file located ~/.zshrc: alias gen='/{full_path_to_this_cloned_repository}/autogenerate/./gen'

Am I using Bash or Zshell?
    If your Terminal shows a '$' at the end of the paths, then it is using bash, while if it is a '%' then it is probably using zshell. Type in an incorrect command (such as 'thisistotallynotacommand') and take not if the returned error is 'sh: unrecognized syntax' or 'zsh: unrecognized syntax': zsh is zshell and sh is bash.
  
To manually run:
    /{full_path_to_this_cloned_repository}/autogenerate/./gen file_name

If you setup the alias:
    gen file_name

For help:
    gen help
  
If you install Java, you can use a better version of gen that utilizes more commands!
Same idea as above, but instead of aliasing './gen' do: alias jen='java /{full_path}/autogenerate/gen.java'

For help:
    jen help
