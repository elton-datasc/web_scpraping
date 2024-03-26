import os
import shutil
import timeit

#https://pt.stackoverflow.com/questions/323786/verificar-tamanho-de-cada-arquivo-em-uma-pasta-em-python-com-os

'''def path_size():

    dir_path = 'C:/Users/Acer/OneDrive/Área de Trabalho/web_scrap_livro'
    files = os.listdir(dir_path)
    for file in files:
        f_path = os.path.join(dir_path, file)
        f_path_size = os.path.getsize(f_path)
        f_path_size_kb = f_path_size/1024
        print(f_path, f_path_size_kb)

    disk_usage = shutil.disk_usage('C:/Users/Acer/OneDrive/Área de Trabalho/web_scrap_livro\produtos_funko')

    print(disk_usage.used/1024)

exec_time = timeit.timeit(path_size, number=1)
print(exec_time)'''

import subprocess

# Substitua 'teste_csv' pelo caminho do diretório que você deseja listar
'''command = 'dir /B /O:G /A:-D produtos_funko'
result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, text=True)

print(result.stdout)'''

folder_path = 'C:/Users/Acer/OneDrive/Área de Trabalho/web_scrap_livro\produtos_funko'
command = f'powershell -command "Get-ChildItem -Path \'{folder_path}\' -Recurse -ErrorAction SilentlyContinue | Measure-Object -Property Length -Sum | Select-Object -ExpandProperty Sum"'
result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, text=True)

# Agora, o resultado deve conter apenas o valor numérico, então podemos convertê-lo diretamente para int
size_in_bytes = int(result.stdout.strip())
print(f"Tamanho da pasta \produtos_funko: {size_in_bytes/1024:5.2f} MB")
