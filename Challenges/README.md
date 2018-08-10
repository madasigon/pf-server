The Challenges module has to provide one function "generate_challenges" which will be called once at challenge generation and has to return a list of challenges.

Every challenge has to have a get_html and a get_solution (returning a string) method, as in the example

The static_storage object from WebApp.space can be used to upload necessary static files like images and refer to them as in the minimalistic example.

 write_content creates a file from a string
 
 copy_from copies the file from the given path
 
 Both should go as the argument to static_storage.create_file
