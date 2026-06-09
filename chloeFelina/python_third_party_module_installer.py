import sys,subprocess,importlib

pip_functional = True

try:
    modules_installed = {dist.name for dist in importlib.metadata.distributions()}
except Exception:
    pip_functional = False

if pip_functional:
    # arcpy deliberately excluded.
    for current_dependency in ('openpyxl','pypdf','docx','docx2python','pillow','tqdm'):
        try:
            if not current_dependency in modules_installed:
                subprocess.check_call([sys.executable,'-m','pip','install',item])
        except Exception:
            pass
