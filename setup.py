import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="django-iran",
    version="0.0.1",
    author="Soroush piri zendedel",
    author_email="soroush_zendedel@live.com",
    keywords=["django","Persian","iran","web service","rest api","core","account"],
    description="Django Core app for iranian developers",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/avanditc/django-iran",
    download_url = "https://github.com/avanditc/django-iran",
    project_urls={
        "Bug Tracker": "https://github.com/avanditc/django-iran/issues",
        "Owner": "https://AvandITC.ir",
    },
    classifiers=[
        "Development Status :: 1 - Planning",
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 2.2',
        'Framework :: Django :: 3.0',
        'Framework :: Django :: 3.1',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content'
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: System :: Systems Administration :: Authentication/Directory',
    ],
    license="MIT",
    packages=setuptools.find_packages(),
    include_package_data=True,
    install_requires=[
        'requests'
    ],
    python_requires=">=3.6",
)
