
import setuptools
import versioneer

if __name__ == "__main__":
    setuptools.setup(
        name='cmspythondev',
        version=versioneer.get_version(),
        description='Example project for the course',
        author='Yi Yao',
        url="https://github.com/yaoyi92/cms-python-dev",
        license='BSD 3-C',
        packages=setuptools.find_packages(),
        install_requires=[
            'jsonschema',
        ],
        extras_require={
            'docs': [
                'sphinx==1.2.3',  # autodoc was broken in 1.3.1
                'sphinxcontrib-napoleon',
                'sphinx_rtd_theme',
                'numpydoc',
            ],
            'tests': [
                'pytest>=3.0',
                'pytest-cov',
            ],
            'develop': [ # extra
                'yapf',
                'versioneer'
            ]
        },

        tests_require=[
            'pytest',
        ],
        zip_safe=True,
    )
