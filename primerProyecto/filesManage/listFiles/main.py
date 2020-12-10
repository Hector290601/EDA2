from pathlib import Path 
from os import scandir, getcwd, walk
import time

def lsPath(ruta = Path.cwd()): 
    return [arch.name for arch in Path(ruta).iterdir() if arch.is_file()]

def lsOsScandir(ruta = getcwd()):
    return [arch.name for arch in scandir(ruta) if arch.is_file()]

def lsWalk(ruta = '.'):
    dir, subdirs, archivos = next(walk(ruta))
    print("Actual: ", dir)
    print("Subdirectorios: ", subdirs)
    print("Archivos: ", archivos)
    return archivos

if __name__ == '__main__':
    start = time.time()
    print("lsPath: ", lsPath())
    end = time.time()
    print(end - start)
    start = time.time()
    print("lsOsScandir: ", lsOsScandir())
    end = time.time()
    print(end - start)
    start = time.time()
    print("IGNORAR", lsWalk())
    end = time.time()
    print(end - start)

