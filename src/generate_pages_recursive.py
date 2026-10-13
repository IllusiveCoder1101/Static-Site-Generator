
import os
import shutil
from generate_page import generate_page
def generate_pages_recursive(dir_path_content: str, template_path: str, dest_dir_path: str) -> None:
    abs_path_src = os.path.abspath(dir_path_content)
    abs_path_dest = os.path.abspath(dest_dir_path)
     
    if os.path.exists(abs_path_src):
        dir_lst = os.listdir(abs_path_src)
    
        for i in dir_lst:
            a = os.path.join(abs_path_src, i)
            if os.path.isfile(a):
                generate_page(from_path=a,template_path=template_path, dest_path=os.path.join(abs_path_dest,"index.html"))
            elif os.path.isdir(a):
                os.mkdir(os.path.join(abs_path_dest, i))
                generate_pages_recursive(a ,template_path ,os.path.join(abs_path_dest, i))
        return
        
