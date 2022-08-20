# coding:utf-8
# author z10mx7
# version : 2.0.0
from setuptools import find_packages, setup
import os

REQUIRES_PYTHON = '>=3.6.0'
VERSION = '2.1.1'
DESCRIPTION="A free and unlimited python tool."
NAME = "gooate"

here = os.path.abspath(os.path.dirname(__file__))


about = {}
if not VERSION:
    project_slug = NAME.lower().replace("-", "_").replace(" ", "_")
    with open(os.path.join(here, project_slug, '__version__.py')) as f:
        exec(f.read(), about)
else:
    about['__version__'] = VERSION

readme = ''
with open('README.md', encoding='utf-8') as f:
    readme = f.read()


setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=readme,
    long_description_content_type="text/markdown",
    author='z10mx7',
    author_email='z10mx7@protonmail.com',
    maintainer='z10mx7',
    maintainer_email='z10mx7@protonmail.com',
    packages=find_packages(),
    platforms=["all"],
    url='https://github.com/z10mx7/gooate',
    include_package_data=True,
    license='MIT',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: MIT License',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Internet',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities',
        'Typing :: Typed',
    ]
)