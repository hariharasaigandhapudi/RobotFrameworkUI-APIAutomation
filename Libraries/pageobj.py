import yaml
import os.path


def load_yaml_pageobj_file(pageobj_file):
    MYDIR = os.path.dirname(__file__)
    path = os.path.join(MYDIR,pageobj_file+".yaml")
    pageobjfile = open(path)
    pageobjfile_parsed = yaml.load(pageobjfile,Loader=yaml.FullLoader)
    return pageobjfile_parsed
