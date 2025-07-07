import setuptools

NAME_PACKAGE = "insightify"

setuptools.setup(
    name=NAME_PACKAGE,
    version="0.0.1",
    packages=setuptools.find_namespace_packages(exclude=["build", "container", "data", "docs", "libs", "notebooks", "resources", "scripts"]),
    install_requires=["setuptools"],
    zip_safe=True,
    maintainer="Bertan Karacora",
    license="MIT",
)
