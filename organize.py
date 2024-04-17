import os
import shutil
from_dir = r"C:\Users\luoli\Downloads\PRO_1-1_C102_AtividadeDoAluno1-main\PRO_1-1_C102_AtividadeDoAluno1-main"
to_dir = r"C:\Users\luoli\OneDrive\Área de Trabalho\ProjetosAnaconda\Aula101e102"
list_of_files = os.listdir(from_dir)
print(list_of_files)
for file_name in list_of_files:
    name, extension = os.path.splitext(file_name)
    #print(name)
    #print(extension)
    if extension == '':
        continue
    if extension in ['.gif','.png','.jpg','.jpeg','.jfif']:
        path1 = from_dir + '/' + file_name
        path2 = to_dir + '/' + "Arquivos_Imagem"
        path3 = to_dir + '/' + "Arquivos_Imagem" + '/' +  file_name
        #print("path1 " , path1)
        #print("path3 " , path3)
        if os.path.exists(path2):
          print("Movendo " + file_name + ".....")
          shutil.move(path1, path3)
        else:
          os.makedirs(path2)
          print("Movendo " + file_name + ".....")
          shutil.move(path1,path3)