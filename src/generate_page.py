import os
from extract_title import extract_title
from markdown_to_html_node import markdown_to_html_node


def generate_page(from_path: str, template_path: str, dest_path: str, base_path: str) -> None:
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    
    abs_from_path = os.path.abspath(from_path)
    f = open(abs_from_path)
    content = f.read()
    f.close()

    abs_template_path = os.path.abspath(template_path)
    f1 = open(abs_template_path)
    content1 = f1.read()
    f1.close()

    html_str = markdown_to_html_node(content).to_html()
    #print(html_str)

    title_page = extract_title(content)

    content1 = content1.replace("{{ Title }}", title_page).replace("{{ Content }}", html_str).replace('href="/',f'href="{base_path}').replace('src="/',f'src="{base_path}')

    abs_dest_path = os.path.abspath(dest_path)
    f2 = open(abs_dest_path,"w")
    i = f2.write(content1)
    f2.close()

        

