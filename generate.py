import os

proyect_dir = None

generator_dir = os.path.dirname(os.path.abspath(__file__)) + '/GraphModels'

apps = ""

def appendApp(app):
    app_dir = proyect_dir + app
    os.system('cp '+app_dir+' '+generator_dir)
    apps.append(app+",")

def isAnApp(app):
    return os.path.exists(proyect_dir + app + 'models.py')

if __name__ == "__main__":

    print('Introduce el directorio completo del projecto: ')
    proyect_dir = input()

    with open(generator_dir+'apps_settings.py', 'w') as f:
        f.write('from GraphModels.settings import *' + os.linesep)
        [appendApp(app=app) for app in os.listdir(proyect_dir) if isAnApp(app=app)]
        f.write('INSTALLLED_APPS += ['+apps+']')

    os.system('cp '+proyect_dir+'/requirements.txt '+generator_dir+'/')

    os.system('source /home/jse/Escritorio/GraphModelsGenerator/venv/bin/activate && \
        pip3 -r install GraphModels/requirements.txt && \
        python3 ' + generator_dir + ' /manage.py graph_models --settings=apps_settings -a -o /home/jse/Escritorio/node.png')

    #clean
