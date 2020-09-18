import os

proyect_dir = '/home/jse/Escritorio/intech-node'

generator_dir = os.path.dirname(os.path.abspath(__file__))

apps = ""

def appendApp(app):
    app_dir = proyect_dir + app
    os.system('cp '+app_dir+' '+generator_dir)
    apps.append(app+",")

def isAnApp(app):
    return os.path.exists(proyect_dir + app + 'models.py')

if __name__ == "__main__":

    print('Introduce el directorio completo del projecto: ')
    input = input()
    if input is not None and input is not '': proyect_dir = input 

    with open(generator_dir+'/GraphModels/apps_settings.py', 'w') as f:
        f.write('from GraphModels.settings import *' + os.linesep)
        [appendApp(app=app) for app in os.listdir(proyect_dir) if isAnApp(app=app)]
        f.write('INSTALLLED_APPS += ['+apps+']')

    os.system('cp '+proyect_dir+'/requirements.txt '+generator_dir+'/GraphModels/')

    os.system(generator_dir+'/_generate.sh '+generator_dir+' '+proyect_dir)

   # clean()
