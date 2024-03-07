import os
import markdown
from jinja2 import Environment, FileSystemLoader, select_autoescape

def main():

    # Configuration
    posts_directory = 'posts'
    output_directory = 'output'
    templates_directory = 'templates'

    # Ensure the output directory exists
    os.makedirs(output_directory, exist_ok=True)

    # Setup Jinja2 environment
    env = Environment(
        loader=FileSystemLoader(templates_directory),
        autoescape=select_autoescape(['html', 'xml'])
    )

    # Load templates
    index_template = env.get_template('index.html')
    post_template = env.get_template('post.html')

    # Process posts
    posts = []
    for post_md_file in os.listdir(posts_directory):
        post_path = os.path.join(posts_directory, post_md_file)
        with open(post_path, 'r') as file:
            content = file.read()
            html_content = markdown.markdown(content)
            post_title = post_md_file.replace('.md', '')
            posts.append({'title': post_title, 'content': html_content})
            # Generate post HTML file
            post_html = post_template.render(title=post_title, content=html_content)
            with open(os.path.join(output_directory, post_title + '.html'), 'w') as output_file:
                output_file.write(post_html)

    # Generate index HTML file
    index_html = index_template.render(posts=posts)
    with open(os.path.join(output_directory, 'index.html'), 'w') as index_file:
        index_file.write(index_html)

    print("Blog generation complete.")

if __name__ == "__main__":
    main()
