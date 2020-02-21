import setuptools

URLs = \
    {
        "Bug Tracker": "https://github.com/rdilweb/mkdocs-plugin-progress/issues",
        "Source Code": "https://github.com/rdilweb/mkdocs-plugin-progress",
        "License": "https://github.com/rdilweb/mkdocs-plugin-progress/blob/master/LICENSE",
    }

setuptools.setup(
    name="mkdocs-plugin-progress",
    version="1.0.2",
    packages=setuptools.find_packages(),
    description="A MkDocs plugin that lets you know exactly what is happening during the build.",
    keywords=["mkdocs", "plugin", "progress", "build", "debugging"],
    author="Reece Dunham",
    author_email="me@rdil.rocks",
    license="Apache 2",
    entry_points={
        "mkdocs.plugins": [
            "progress = mkdocs_plugin_progress:Progress"
        ]
    },
    long_description=open("README.md", "r").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/rdilweb/mkdocs-plugin-progress",
    python_requires=">=3.3",
    include_package_data=True,
    project_urls=URLs,
    install_requires=open("requirements.txt", "r").readlines()
)
