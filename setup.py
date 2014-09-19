try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name='pymegacli',
    version='0.1',
    author='James Brown',
    author_email='jbrown@uber.com',
    url='http://github.com/uber/pymegacli',
    description='object-oriented API around the MegaCLI tool for administrating LSI RAID cards',
    classifiers=[
        'Programming Language :: Python',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: GNU Lesser General Public License v2 (LGPLv2)',
        'Topic :: System :: Hardware',
        'Topic :: System :: Monitoring',
        'Topic :: System :: Systems Administration',
        'Intended Audience :: System Administrators',
        'Development Status :: 4 - Beta',
    ],
    packages=['pymegacli'],
    long_description=open('README.md', 'r').read().split('\n'),
)
