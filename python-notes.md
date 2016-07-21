# Python Tips and Tricks

## Generic Tips
* `__file__` -- reference to current file name
* `print('Bucket name: {}'.format(bucket.name))` -- format method for strings
* `with` statements - <http://effbot.org/zone/python-with-statement.htm> (see [Remote.py gist](https://gist.github.com/dnorton/ad9804f79dcac7804772))
* [Deleting read-only dirs in Windows](http://stackoverflow.com/a/1889686) ([my gist](https://gist.github.com/dnorton/9c9f465a9f458ac095c5f0b9cb74ec58))
* [use **kwargs -- key word args](http://www.saltycrane.com/blog/2008/01/how-to-use-args-and-kwargs-in-python/)

## pip

* [get-pip.py](https://bootstrap.pypa.io/get-pip.py) -- install pip
* `pip install --index-url=http://pypi.python.org/simple/ --trusted-host pypi.python.org  pythonPackage`

## Standard Library

+ [subprocess](https://docs.python.org/2/library/subprocess.html) -- library for making system calls
+ [File and Directory Access](https://docs.python.org/2/library/filesys.html)
+ [re](https://docs.python.org/2/library/re.html) -- regular expressions
 + [Google's Regex Tutorial](https://developers.google.com/edu/python/regular-expressions)
 + [cheatsheet](https://www.debuggex.com/cheatsheet/regex/python)
 

## Python Libraries

* [inspect](https://docs.python.org/2/library/inspect.html#module-inspect) -- `inspect.getmembers(object)`
* [elementtree](https://pypi.python.org/pypi/elementtree/) -- XML parsing
* [httpie](https://github.com/jkbrzt/httpie) -- curl replacement
* [requests](http://docs.python-requests.org/en/master/) -- HTTP(s) requests
* [pandas](http://pandas.pydata.org/) -- big data analysis. Compares to R.
* [flask](https://github.com/pallets/flask) -- microframework/web
* [hug](https://github.com/timothycrosley/hug) -- API generation
 
## Google App Engine
- https://gae-init.appspot.com/
 
## Testing

- [stdlib: unittest](https://docs.python.org/dev/library/unittest.html#module-unittest)
- [3rd party: nose](https://nose.readthedocs.org/en/latest/testing.html)

### More

_My [Python Wiki page](https://github.com/dnorton/dev-notes/wiki/Python)_ :notebook:
