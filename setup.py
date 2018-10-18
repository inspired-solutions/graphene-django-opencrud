from setuptools import find_packages, setup
import os

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    README = readme.read()

tests_require = [
    "coverage",
    "django-filter>=2",
    "djangorestframework",
    "graphene-django",
    "pytest",
    "pytest-cov",
    "pytest-django",
]

setup(
    name="graphene-django-opencrud",
    version="1.0.0",
    description="Opencrud Graphene Django implementation",
    long_description=README,
    url="https://github.com/inspired-solutions/graphene-django-opencrud",
    author="Inspired Solutions",
    author_email="contacto@inspiredsolutions.pe",
    license="MIT",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: Implementation :: PyPy",
    ],
    keywords="api graphql protocol rest relay graphene opencrud",
    packages=find_packages(exclude=["tests"]),
    install_requires=[
        "graphene-django",
        "django-filter>=2",
        "Django>=2",
    ],
    setup_requires=["pytest-runner"],
    tests_require=tests_require,
    extras_require={"test": tests_require},
    include_package_data=True,
    zip_safe=False,
    platforms="any",
)
