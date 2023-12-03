import os
import subprocess

# 対象のディレクトリを設定します。ここでは例として 'my_videos' ディレクトリを使います。
source_directory = 'my_videos'

# 出力ディレクトリ 'out' を作成します。
output_directory = 'out'
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

# 対象ディレクトリ内のすべての mp4 ファイルを検索し、変換を実行します。
for filename in os.listdir(source_directory):
    if filename.endswith('.mp4'):
        # 入力ファイルの完全なパス
        input_path = os.path.join(source_directory, filename)
        
        # 出力ファイルの完全なパス
        output_path = os.path.join(output_directory, filename)

        # ffmpeg コマンドを構築
        command = f'ffmpeg -i "{input_path}" -c:v libx264 -crf 23 "{output_path}"'

        # ffmpeg コマンドを実行
        subprocess.run(command, shell=True)

# スクリプトが完了したことを示すメッセージを表示
print("変換が完了しました。")
