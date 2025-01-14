
import os
import os.path as osp
import zipfile
from .download import download_file

#BASE_REPO_URL='http://storage.insightface.ai/files'
#BASE_REPO_URL='http://insightface.cn-sh2.ufileos.com'
BASE_REPO_URL='http://d1gsb2o3ihr2l5.cloudfront.net'

def download(sub_dir, name, force=False, root='~/.insightface'):
    _root = os.path.expanduser(root)
    dir_path = os.path.join(_root, sub_dir, name)
    if osp.exists(dir_path) and not force:
        return dir_path
    print('download_path:', dir_path)
    zip_file_path = os.path.join(_root, sub_dir, name + '.zip')

    print("zip_file_path", zip_file_path)

    model_url = "%s/%s/%s.zip"%(BASE_REPO_URL, sub_dir, name)
    #model_url = "%s/%s.zip"%(BASE_REPO_URL, name)

    if not os.path.exists(zip_file_path):
        download_file(model_url,
                     path=zip_file_path,
                     overwrite=True)
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
    with zipfile.ZipFile(zip_file_path) as zf:
        zf.extractall(dir_path)
    #os.remove(zip_file_path)
    return dir_path

def ensure_available(sub_dir, name, root='~/.insightface'):
    return download(sub_dir, name, force=False, root=root)

def download_onnx(sub_dir, model_file, force=False, root='~/.insightface', download_zip=False):
    _root = os.path.expanduser(root)
    model_root = osp.join(_root, sub_dir)
    new_model_file = osp.join(model_root, model_file)
    if osp.exists(new_model_file) and not force:
        return new_model_file
    if not osp.exists(model_root):
        os.makedirs(model_root)
    print('download_path:', new_model_file)
    if not download_zip:
        model_url = "%s/%s/%s"%(BASE_REPO_URL, sub_dir, model_file)
        download_file(model_url,
                 path=new_model_file,
                 overwrite=True)
    else:
        model_url = "%s/%s/%s.zip"%(BASE_REPO_URL, sub_dir, model_file)
        zip_file_path = new_model_file+".zip"
        download_file(model_url,
                 path=zip_file_path,
                 overwrite=True)
        with zipfile.ZipFile(zip_file_path) as zf:
            zf.extractall(model_root)
        return new_model_file
