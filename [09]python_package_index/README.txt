##------####------####------####------####------####------####------####------##

The videos within this section are:

1. PyPI
2. Pip
3. Virtual Enviornments
4. Pipenv
5. Virtual Enviornments in VSCode
6. Pipfile
7. Managing Dependencies
8. Publishing Packages
9. Docstrings
10. Pydoc

None of them contain 'code', per se. But, in video #8, we do go through a full
package creation - and ultimately, how to publish that package. So, for that
particular video, a folder will be created - I'll call it the name of the video,
which is "Publishing Packages" (dir name = 'publishing_packages').

To be brief, ALL packages - to be publishes or otherwise - should all have the 
following directory/file structure:

package_name/
    data/
    tests/
    package_name/
        __init__.py
        some_file.py
        some_other_file.py
        etc_etc_etc.py
    LICENSE
    README.md
    setup.py

Once your package structure is formed, and you have all the necessary code for
your project written, go to the terminal; location = project ROOT. Then, run:

```
python3 setup.py sdist bdist_wheel
```

With this command, you will generate TWO packages:
1. A SOURCE distribution
2. A BUILT distribution

That command will generate TWO NEW DIRECTORIES within your ROOT directory:
1. dist/
2. build/

Within the 'build' directory, you'll have 2 zipped (compressed) files. If you
are feeling totally adventurous, you can upzip them and check their contents.
If not, we move to the final step, which is uploading to the official PyPI 
repository. To do that, go back to the terminal and run the following command:

* again, from your package's ROOT directory!
```
twine upload dist/*
```

What that command is doing is uploading ALL files from within our new 'dist'
directory to 'http://pypi.org'.
NOTE: You will be prompted for your Username and Password! This will be your 
credentials for your PyPI account (Video #8 will instruct you to do so, if you
do not already have a PyPI account. It's easy and quick!)

Thanks.