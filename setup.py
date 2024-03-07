from setuptools import setup, find_packages

setup(
    name='markdown_blog_generator',
    version='0.1.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'markdown',
        'jinja2'
    ],
    entry_points={
        'console_scripts': [
            'markdown-blog-generator=markdown_blog_generator.generator:main',
        ],
    },
    author='John Doe',
    author_email='tadeemanuel9@gmail.com',
    description='A simple static blog generator that converts Markdown files to HTML using Jinja2 templates.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    license='MIT',
    keywords='blog generator markdown static-site jinja2',
    url='https://github.com/yourusername/markdown_blog_generator',
    project_urls={
        "Source": "https://github.com/JohnDoe2332/MarkDownBlogGenerator",
        "Bug Tracker": "https://github.com/JohnDoe2332/MarkDownBlogGenerator",
    } # Your project's main homepage.
)
