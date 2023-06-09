from setuptools import setup, find_packages


if __name__ == "__main__":
    setup(
        name='m3_project',
        version='1.0.0',
        packages=find_packages(),
        install_requires=[
            "django==2.2.2",
            "m3-django-compat==1.9.2",
            "m3-objectpack==2.2.47"
        ],
        classifiers=[
            'Development Status :: 5 - Production/Stable',
            'Environment :: Web Environment',
            'Framework :: Django',
            'Intended Audience :: Developers',
            'License :: OSI Approved :: MIT License',
            'Operating System :: OS Independent',
            'Programming Language :: Python',
            'Programming Language :: Python :: 3',
            'Programming Language :: Python :: 3.6',
            'Topic :: Internet :: WWW/HTTP',
            'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        ],
    )

