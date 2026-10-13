from copy_files import copy_files
from generate_pages_recursive import generate_pages_recursive
def main():
    copy_files("static","public")
    generate_pages_recursive("public/content","template.html","public")

main()