from setuptools import setup

__version__ = '1.1dev'

setup(
    name='five.globalrequest',
    version=__version__,
    description="Zope integration for zope.globalrequest",
    long_description=(open("README.rst").read() + "\n" +
                      open("CHANGES.rst").read()),
    classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
    ],
    keywords='zope global request',
    author='Zope Foundation and Contributors',
    author_email='zope-dev@zope.org',
    url='http://pypi.python.org/pypi/five.globalrequest',
    license='ZPL',
    packages=['five', 'five.globalrequest'],
    package_dir={'': 'src'},
    namespace_packages=['five'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'setuptools',
        'zope.globalrequest',
        'Zope2',
    ],
)
