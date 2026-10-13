import sys
from copy_files import copy_files
from generate_pages_recursive import generate_pages_recursive
def main():
    var = sys.argv
    base_path = ""
    if len(var) == 2:
        base_path = var[1]
    elif len(var) < 2:
        base_path = "/"

    copy_files("static","docs")
    generate_pages_recursive("docs/content","template.html","docs", base_path)

main()