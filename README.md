##WebscrapeScript

### Project
Create script to take url input and return comma-delimited genre listing

1. Takes a title_url (as listed below) as input from Wikipedia. 
2. Fetches the content of the title.
3. Parses the title's content to extract genre(s) as found in the title.
4. Displays the list of genres associated with the title in the following form: genre1, genre2, ...


Sample test data:

http://en.wikipedia.org/wiki/Pretty_Little_Liars_(TV_series)
http://en.wikipedia.org/wiki/The_big_bang_theory
http://en.wikipedia.org/wiki/Good_Wife
http://en.wikipedia.org/wiki/Doctor_Who
http://en.wikipedia.org/wiki/The_big_bang_teory
http://en.wikipedia.org/wiki/Elementary_(TV_series)

Testing:
Add suitable error handling as needed.
Include error checking against the url fetched. E.g. what happens in the following cases:
url not found - e.g. http://en.wikipedia.org/TheBigBangTheor
the page returns an error such as a 404

### TODOs
* write code.
* write tests.
* be awesome.
