# compile.sh version 2.0.1

# This file searches from the parent directory for 'modinfo.py' in it or in any sub directory.
# Make sure to have only one 'modinfo.py' in your project directory. The first found 'modinfo.py' is used and loaded.
# This file creates Release/ThisModName/* and finally  Release/ThisModName.zip for distribution.
# If extracted properly 'mod_data' and 'mod_documentation' will be folders next to 'Mods'.

# Folder structure:
# TS4-Mods/custom_scripts_for_decompile/
# TS4-Mods/EA/
# TS4-Mods/Libraries/sims4communitylib/
# TS4-Mods/TS4-ThisModName/_compile/compile.sh
# TS4-Mods/TS4-ThisModName/_TS4/(mod_data|mod_documentation|Mods)/ - These folders will be added to the mod.
# TS4-Mods/TS4-ThisModName/this_mod_name/*.py - The mod itself
# TS4-Mods/decomplie_scripts.py + settngs.py - Scripts to update 'custom_scripts_for_decompile' and 'EA'

# ThisModName and this_mod_name should be replaced with useful names.
# compile.sh may be renamed to compile_ThisModName.sh to have unique names for compile scripts.

import re
import os
import sys
import shutil

from Utilities.unpyc3_compiler import Unpyc3PythonCompiler

beta_appendix = "-beta"

modinfo_py = 'modinfo.py'
mi = None
for root, dirs, files in os.walk('..'):
    if modinfo_py in files:
        modinfo = os.path.join(root, modinfo_py)
        print(f"Using '{modinfo}' ...")
        try:
            sys.path.insert(1, root)
            # noinspection PyUnresolvedReferences
            from modinfo import ModInfo
            mi = ModInfo.get()
            print(f"Imported data for '{mi._author}:{mi._name}' from '../{mi._base_namespace}' with version '{mi._version}'")
            modinfo_py = ''
        except Exception as e:
            print(f"Error importing '{modinfo_py}' ({e}).")
        break
if not mi:
    print(f"Error '{modinfo_py}' not found.")
    exit(1)


author = mi._author
mod_name = mi._name
mod_directory = mi._base_namespace
version = mi._version  # All versions 0., x.1, x.3, x.5, x.7, x.9 (also x.1.y, x.1.y.z) will be considered beta and the 'beta_appendix' is appended.

release_directory = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(os.getcwd()))), 'Release')
mod_base_directory = os.path.join(release_directory, mod_name)
ts4_directory = os.path.join(mod_base_directory, 'Mods', f"_{author}_")

# Copy folders
src_folder = os.path.join(os.path.dirname(os.path.abspath(os.getcwd())), '_TS4')
for folder in ['mod_data', 'mod_documentation', 'Mods']:
    try:
        shutil.copytree(os.path.join(src_folder, folder), os.path.join(mod_base_directory, folder))
    except:
        print(f"WARNING: Remove the folder {os.path.join(mod_base_directory, folder)} to update the data.")

zip_file_name = os.path.join(release_directory, f"{mod_name}")
if version:
    zip_file_name = f"{zip_file_name}_v{version}"
    if re.match(r"^(?:0|(?:0|[1-9][0-9]*)\.[0-9]*[13579])(?:\.[0-9]+)*$", version):
        zip_file_name = f"{zip_file_name}{beta_appendix}"


# Compile
os.makedirs(ts4_directory, exist_ok=True)
print(f"{ts4_directory}")

Unpyc3PythonCompiler.compile_mod(
    names_of_modules_include=(mod_directory, ),
    folder_path_to_output_ts4script_to=ts4_directory,
    output_ts4script_name=mod_directory
)

# Zip
shutil.make_archive(os.path.join(release_directory, f"{zip_file_name}"), 'zip', mod_base_directory)
print(f'Created {os.path.join(release_directory, f"{zip_file_name}.zip")}')
