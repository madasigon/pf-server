The Challenges module has to provide one function "generate_challenges" which will be called once at challenge generation and has to return a list of challenges. Its only parameter is an "AssetStorage" object which has a create_asset method. This takes a file as parameter, saves it to be online available and returns the url at which it's available.

Every challenge has to have a get_html and a get_solution (returning a string) method, as in the example

The create_asset method can be used to upload necessary static files like images and refer to them as in the minimalistic example. Its only parameter is a file creator which can be created using the following functions imported from WebApp.space:
- write_content creates a file from a string
- copy_from copies the file from the given path
 

