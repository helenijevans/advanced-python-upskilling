import os
import zipfile


def zip_up(input_path, output_path):
    zf = zipfile.ZipFile(output_path, "w")
    for dirname, subdirs, files in os.walk(input_path):
        zf.write(dirname)
        for filename in files:
            zf.write(os.path.join(dirname, filename))
    zf.close()


zip_up("./Challenge Files", "zippy.zip")

"""
GIVEN SOLUTION
"""
import os
from zipfile import ZipFile


def zip_all(search_dir, extension_list, output_path):
    with ZipFile(output_path, 'w') as output_zip:
        for root, dirs, files in os.walk(search_dir):
            rel_path = os.path.relpath(root, search_dir)
            for file in files:
                name, ext = os.path.splitext(file)
                if ext.lower() in extension_list:
                    output_zip.write(os.path.join(root, file),
                                     arcname=os.path.join(rel_path, file))

## REFLECTION
# Solutions quite similar, I adapted the requirements of the function as there seemed to be parameter redundancy
# Could have just been that the summary wasn't adequate at describing desired functionality in this function.
# For example, I always assumed relative path, and the given solution doesn't and then does a conversion

