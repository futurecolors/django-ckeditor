from setuptools import setup, find_packages

setup(
    name='django-ckeditor-fc',
    version='1.1',
    description='Django admin CKEditor integration.',
    long_description=open('README.rst', 'r').read() + open('AUTHORS.rst', 'r').read() + open('CHANGELOG.rst',
                                                                                             'r').read(),
    author='Future Colors (orginal author:Shaun Sephton)',
    author_email='shaunsephton@gmail.com',
    url='https://github.com/futurecolors/django-ckeditor',
    packages=find_packages(),
    dependency_links=[
        'http://dist.plone.org/thirdparty/',
    ],
    install_requires=[
        'Pillow', 'pytils'
    ],
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python",
        "License :: OSI Approved :: BSD License",
        "Development Status :: 4 - Beta",
        "Operating System :: OS Independent",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
    ],
    zip_safe=False,
)
