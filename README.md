Program introduction:
I want to build a new language based on Python
This new language has not been named yet
I hope that the new language will inherit Python's simplicity and huge library
and add automatic commenting and code compression functions
Automatic commenting will analyze the code and write comments when special symbols are entered
The comments will explain the meaning of the code and mark the referenced variables, parameters, and functions
I also hope that the generated comments can be in different languages, such as Chinese It is convenient for people who are not good at English to use programming.
Code compression helps the program to reduce the size of redundant code. 
I want to design it manually, but it can also be done automatically when saving or uploading the code. 
It will delete the automatically generated special comments (different comments will not be deleted) to save space. 
If you need these special comments, just let the program automatically generate special comments again. 
---------------------------------------------------------------------------------------------------------------
Program logic: I want to let the program generate automatic comments when the user uses the special symbol "///". 
After the automatic comment is generated, "///" will be replaced by "/#/". 
Then the code compression step will delete all the content after "/#/". And "/#/" will be replaced by "///".
I haven't thought of the program for automatically generating comments yet. 
I hope to generate comments with the help of AI.
---------------------------------------------------------------------------------------------------------------
Example:
text = "Hello" /#/creating a variable "text" set to string "Hello"
print(text) ///
When automatically generating comments:
text = "Hello" /#/creating a variable "text" set to string "Hello"
print(text) /#/ptint a variable "text"("Hello")
When compressing the code manually:
text = "Hello" ///
print(text) ///
