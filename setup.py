from distutils.core import setup

VERSION = '0.9.5'

setup(
    name = 'finder_colors',
    py_modules = ['finder_colors'],
    scripts = ['finder_colors.py'],
    version = VERSION,
    description = 'Get/Set the Colors set on files by OSX Finder',
    long_description=open('README.rst','r').read(),
    author = 'Daniel Fairhead',
    author_email = 'danthedeckie@gmail.com',
    url = 'https://github.com/danthedeckie/finder_colors',
    download_url = 'https://github.com/danthedeckie/finder_colors/tarball/' + VERSION,
    keywords = ['OSX', 'OS X', 'Finder', 'Colors', 'Utility', 'Colours'],
    install_requires = ['xattr', ],
    classifiers = ['Development Status :: 4 - Beta',
                   'License :: OSI Approved :: MIT License',
                   'Intended Audience :: Developers',
                   'Programming Language :: Python :: 2.7',
                   'Environment :: Console',
                   'Environment :: MacOS X',
                   'Intended Audience :: System Administrators',
                   'Operating System :: MacOS :: MacOS X',
                   'Topic :: Desktop Environment :: File Managers',
                   'Topic :: Software Development :: Libraries',
                   'Topic :: System :: Systems Administration',
                   'Topic :: Utilities',
                  ],
    )
