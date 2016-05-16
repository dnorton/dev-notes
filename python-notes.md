# Python Tips and Tricks

* `__file__` -- reference to current file name
* `print('Bucket name: {}'.format(bucket.name))` -- format method for strings
* [get-pip.py](https://raw.github.com/pypa/pip/master/contrib/get-pip.py) -- install pip
* `pip --proxy {proxy_url} install {your lib}` -- run pip using a proxy
* `pip install --index-url=http://pypi.python.org/simple/ --trusted-host pypi.python.org  pythonPackage`
* `with` statements - <http://effbot.org/zone/python-with-statement.htm> (see [Remote.py gist](https://gist.github.com/dnorton/ad9804f79dcac7804772))
* [Filesystem structure of a Python project](http://as.ynchrono.us/2007/12/filesystem-structure-of-python-project_21.html) :star2:
  * <http://docs.python-guide.org/en/latest/writing/structure/>
* [Deleting read-only dirs in Windows](http://stackoverflow.com/a/1889686) ([my gist](https://gist.github.com/dnorton/9c9f465a9f458ac095c5f0b9cb74ec58))

## Standard Library

+ [subprocess](https://docs.python.org/2/library/subprocess.html) -- library for making system calls
+ [File and Directory Access](https://docs.python.org/2/library/filesys.html)

## Python Libraries

* [inspect](https://docs.python.org/2/library/inspect.html#module-inspect) -- `inspect.getmembers(object)`
* [elementtree](https://pypi.python.org/pypi/elementtree/) -- XML parsing
* [httpie](https://github.com/jkbrzt/httpie) -- curl replacement
* [requests](http://docs.python-requests.org/en/master/) -- HTTP(s) requests
 
## Google App Engine
- https://gae-init.appspot.com/

 
## Testing

- [stdlib: unittest](https://docs.python.org/dev/library/unittest.html#module-unittest)
- [3rd party: nose](https://nose.readthedocs.org/en/latest/testing.html)

### More

_My [Python Wiki page](https://github.com/dnorton/dev-notes/wiki/Python)_ :notebook:
