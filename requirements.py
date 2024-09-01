import subprocess
import sys
packages = [
    'pandas',
    'matplotlib',
    'wordcloud',
    'seaborn',
    'scikit-learn'
]

def install_packages(package_list):
    for package in package_list:
        try:
            subprocess.check_call([sys.executable, '-m', 'pip', 'install', package])
            print(f"Successfully installed {package}")
        except subprocess.CalledProcessError as e:
            print(f"Failed to install {package}: {e}")

install_packages(packages)
