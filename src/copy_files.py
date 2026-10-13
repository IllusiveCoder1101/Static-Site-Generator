import os
import shutil
def copy_files(src_dir: str, dest_dir: str) -> None:
    abs_path_src = os.path.abspath(src_dir)
    abs_path_dest = os.path.abspath(dest_dir)

    if os.path.exists(abs_path_dest):
        shutil.rmtree(abs_path_dest)

    os.mkdir(abs_path_dest)

    if os.path.exists(abs_path_src):
        dir_lst = os.listdir(abs_path_src)

        for i in dir_lst:
            a = os.path.join(abs_path_src, i)
            if os.path.isfile(a):
                shutil.copy(a,abs_path_dest)
            elif os.path.isdir(a):
                os.mkdir(os.path.join(abs_path_dest, i))
                copy_files(a , os.path.join(abs_path_dest, i))
        return
    