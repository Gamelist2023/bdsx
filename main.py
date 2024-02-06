import os
import glob
import subprocess
def run_command(command):
    process = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
    output, error = process.communicate()
    return output
# BDSXのデータをダウンロードします
run_command('git clone https://github.com/bdsx/bdsx.git')
# ダウンロードしたデータを解凍します
downloaded_files = glob.glob('*')  # ダウンロードしたファイルのリストを取得
downloaded_file = max(downloaded_files, key=os.path.getctime)  # 最新のファイルを取得
run_command(f'tar xvf {downloaded_file}')  # 最新のファイルを解凍
# 解凍したディレクトリに移動します
directories = next(os.walk('.'))[1]  # ディレクトリのリストを取得
directory_name = max(directories, key=os.path.getctime)  # 最新のディレクトリを取得
os.chdir(directory_name)
# npm iコマンドを実行して依存関係をインストールします
run_command('npm i')
# GitHubから特定のファイルをクローンします
run_command('git clone <クローンしたいGitHubのリポジトリのURL>')
# クローンしたファイルをBDSXのフォルダに上書きします
cloned_directories = next(os.walk('.'))[1]  # クローンしたディレクトリのリストを取得
cloned_directory = max(cloned_directories, key=os.path.getctime)  # 最新のクローンしたディレクトリを取得
run_command(f'cp -r {cloned_directory}/* ./')  # 最新のクローンしたディレクトリの中身を上書き