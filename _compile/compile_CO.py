# compile.sh version 2.0.18

# This file searches from the parent directory for 'modinfo.py' in it or in any subdirectory.
# Make sure to have only one 'modinfo.py' in your project directory. The first found 'modinfo.py' is used and loaded.

# Folder structure:
# PyCharm-Folder/_compile/compile.sh
# PyCharm-Folder/_TS4/mod_data|mod_documentation|Mods/ - These folders will be added to the mod.
# If extracted properly 'mod_data' and 'mod_documentation' will folders next to 'Mods'.
#
# PyCharm-Folder/your-mod-name/modinfo.py and other files and folders to be compiled


import os
import re
import ast
import sys
import shutil
from typing import Tuple, Dict, Any

from Utilities.unpyc3_compiler import Unpyc3PythonCompiler


additional_directories: Tuple = ()
include_sources = False
exclude_folders: Tuple = ()
add_readme = True
file_appendix = ''
auto_beta = True
exclude_dependencies = ()
try:
    with open('compile.ini', 'rt') as fp:
        cfg: Dict[str, Any] = ast.literal_eval(fp.read())
        additional_directories = cfg.get('additional_directories', additional_directories)
        include_sources = cfg.get('include_sources', include_sources)
        exclude_folders = cfg.get('exclude_folders', exclude_folders)
        add_readme = cfg.get('add_readme', add_readme)
        file_appendix = cfg.get('file_appendix', file_appendix)
        auto_beta = cfg.get('auto_beta', auto_beta)
        exclude_dependencies = cfg.get('exclude_dependencies', exclude_dependencies)
except:
    pass

beta_appendix = "-beta"  # or "-test-build"

modinfo_py = 'modinfo.py'
init_py = '__init__.py'
init = ''
mi = None
for root, dirs, files in os.walk('..'):
    if '.private' in root:
        continue
    if modinfo_py in files:
        modinfo = os.path.join(root, modinfo_py)
        init = os.path.join(root, init_py)
        if not os.path.exists(init):
            print(f"Found '{modinfo}' but '{init}' is missing. Skipping folder!")
            continue
        else:
            size = os.path.getsize(init)
            if size > 0:
                print(f"Size of '{init}' is {size}.")
        print(f"Using '{modinfo}' ...")
        try:
            sys.path.insert(1, root)
            # noinspection PyUnresolvedReferences
            from modinfo import ModInfo

            mi = ModInfo.get()
            print(
                f"Imported data for '{mi._author}:{mi._name}' from '../{mi._base_namespace}' with version '{mi._version}'")
            break
        except Exception as e:
            print(f"Error importing '{modinfo_py}' ({e}).")
        break

if not mi:
    print(f"Error '{modinfo_py}' not found.")
    exit(1)

author = mi._author
mod_name = mi._name
mod_directory = mi._base_namespace
version = mi._version  # All versions 0., x.1, x.3, x.5, x.7, x.9 (also x.1.y, x.1.y.z) will be considered beta and the 'beta_appendix' gets appended.

try:
    # S4CL_VERSION
    s4cl_modinfo_py = os.path.join('..', '..', 'Libraries', 'sims4communitylib', 'modinfo.py')
    with open(s4cl_modinfo_py, 'rt') as fp:
        s4cl_version = fp.read()
        s4cl_version = s4cl_version.replace('\r', ' ').replace('\n', ' ').replace('\t', ' ')
        s4cl_version = re.sub(r' {2,}', ' ', s4cl_version)
        s4cl_version = re.sub(r".*def _version.*return '([0-9.]*)'.*", r'\g<1>', s4cl_version)
except Exception as e:
    print(f"Error reading S4CL ({e}).")
    exit(1)

if add_readme:
    file_game_version = 'c:' + os.sep + os.path.join(os.environ['HOMEPATH'], 'Documents', 'Electronic Arts',
                                                     'The Sims 4', 'GameVersion.txt')
    with open(file_game_version, 'rb') as fp:
        _game_version = fp.read()
        game_version = _game_version[4:].rsplit(b'.', 1)[0].decode('ASCII')

    file_readme = os.path.join('..', '.private', 'README.md')
    file_footer = os.path.join('..', '..', 'FOOTER.md')
    gitignore = os.path.join('..', '.gitignore')
    file_readme_1 = os.path.join('..', 'README.md')
    file_readme_2 = os.path.join('..', '_TS4', 'mod_documentation', mod_directory, 'README.md')
    if os.path.exists(file_readme) and os.path.exists(file_footer) and os.path.exists(gitignore):
        for file_w in [file_readme_1, file_readme_2]:
            os.makedirs(os.path.dirname(file_w), exist_ok=True)
            with open(file_w, 'wb') as fp_w:
                for file_r in [file_readme, file_footer]:
                    with open(file_r, 'rb') as fp_r:
                        _data = fp_r.read()
                        data = re.sub(r'GAME_VERSION', game_version, _data.decode('UTF-8'))
                        data = re.sub(r'S4CL_VERSION', s4cl_version, data)
                        if exclude_dependencies:
                            for e in exclude_dependencies:
                                data = re.sub(f'. .{e}..[^)]*.\r\n', '', data)
                        fp_w.write(data.encode('UTF-8'))
        with open(gitignore, 'rt') as fp:
            if ".private" not in fp.read():
                fp.close()
                with open(gitignore, 'at', newline='\n') as fp:
                    fp.write('\n#Private data\n.private\n')
    else:
        print(f"Files missing: {file_readme} or {gitignore} or {file_footer}")
        exit(1)

release_directory = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(os.getcwd()))), 'Release')
mod_base_directory = os.path.join(release_directory, mod_name)
mod_base_directory_backup = os.path.join(release_directory, f"{mod_name}.bak")
if os.path.exists(mod_base_directory_backup):
    shutil.rmtree(mod_base_directory_backup)
if os.path.exists(mod_base_directory):
    os.rename(mod_base_directory, mod_base_directory_backup)

ts4_directory = os.path.join(mod_base_directory, 'Mods', f"_{author}_")

src_folder = os.path.join(os.path.dirname(os.path.abspath(os.getcwd())), '_TS4')
for folder in ['mod_data', 'mod_documentation', 'Mods', 'mod_sources']:
    try:
        if os.path.exists(os.path.join(src_folder, folder)):
            try:
                shutil.rmtree(os.path.join(mod_base_directory, folder))
            except:
                pass
            shutil.copytree(os.path.join(src_folder, folder), os.path.join(mod_base_directory, folder))
    except:
        print(f"WARNING: Remove the folder {os.path.join(mod_base_directory, folder)} to update the data.")

zip_file_name = os.path.join(release_directory, f"{mod_name}")
if version:
    zip_file_name = f"{zip_file_name}_v{version}"
    if auto_beta:
        if re.match(r"^(?:0|(?:0|[1-9][0-9]*)\.[0-9]*[13579])(?:\.[0-9]+)*$", version):
            zip_file_name = f"{zip_file_name}{beta_appendix}"
zip_file_name = f"{zip_file_name}{file_appendix}"

# Add source
if include_sources:
    _mod_src_directory = os.path.dirname(os.path.abspath(os.getcwd()))
    for folder in (mod_directory,) + additional_directories:
        try:
            shutil.copytree(os.path.join(_mod_src_directory, folder),
                            os.path.join(mod_base_directory, 'mod_sources', mod_name, folder),
                            ignore=shutil.ignore_patterns('__pycache__', '.*'))
        except Exception as e:
            print(f"{e}")
            print(
                f"WARNING: Remove the folder {os.path.join(mod_base_directory, 'mod_sources', mod_name, folder)} to update the data.")

# Compile
os.makedirs(ts4_directory, exist_ok=True)
print(f"Compiling '{mod_directory}' and {additional_directories} in '{ts4_directory}'")

Unpyc3PythonCompiler.compile_mod(
    names_of_modules_include=(mod_directory,) + additional_directories,
    folder_path_to_output_ts4script_to=ts4_directory,
    output_ts4script_name=mod_directory
)

for exclude_folder in exclude_folders:
    try:
        if os.path.exists(os.path.join(mod_base_directory, exclude_folder)):
            print(f"Excluding (removing) '{exclude_folder}'")
            shutil.rmtree(os.path.join(mod_base_directory, exclude_folder))
    except Exception as e:
        print(f"WARNING: Error {e} deleting the folder")

shutil.make_archive(os.path.join(release_directory, f"{zip_file_name}"), 'zip', mod_base_directory)
print(f'Created {os.path.join(release_directory, f"{zip_file_name}.zip")}')

'''
v2.0.18
    Check for __init__.py and its size.
v2.0.17
    Support also longer S4CL version numbers '([0-9]*)' instead of '(.\..)'
v2.0.16
    Added exclude_dependencies to config.ini to be able to remove these.
    Updated FOOTER.md with 'GAME_VERSION'
    ../Libraries/sims4communitylib/modinfo.py
v2.0.15
    Make a backup of the existing directory and create a full/new build
v2.0.14
    read game-version from game_version.txt
v2.0.13
    Exclude .private/modinfo.py
    compile.ini options:
        'auto_beta': True,  - Set to False to avoid '-beta' naming for the ZIP file
v2.0.12
    compile.ini options:
        'add_readme': True,  - Set to False to avoid creating README.md
        'file_appendix': ''  - Define a custom "-xxx" appendix for the ZIP file
v2.0.11
    Fixed exclude_folders
v2.0.10
    Fix folder-delete issue cause other folders not to be copied
v2.0.9
    Allow to exclude folders to create smaller zip files.
    # compile.ini >> 'exclude_folders': ['mod_documentation', 'Mods'],
v2.0.8
    Merge '../.private/README.md' and '../../FOOTER.md' to '../README.md' and  '../_TS4/mod_documentation/{mod_directory}/README.md'
v2.0.7
    Fix mkdir vs. mkdirs
v2.0.6
    Copy ~/README.md to _T$4/mod_documentation/mod_directory/
v2.0.5
    Moved modinfo.dict to _compile/compile.ini
v2.0.4
    Moved both settings to modinfo.dict so they are not included in the source / compiled.
v2.0.3
    Add 'include_source = True' to 'modinfo.py' to add also the source.
v2.0.2
    Add 'additional_directories = ('foo', )' to 'modinfo.py' to include also other directories ('foo' in this case).
'''
