# AI神経衰弱

AI神経衰弱とは？
近年話題である画像生成AIで画像を作成。その画像を使用し、神経衰弱を行うというものである。今までの神経衰弱では、数字を覚えるというものだったのに対し、AI神経衰弱では、画像を覚える必要がある。
## 画像で神経衰弱を行うメリット
瞬間記憶力を鍛える練習ができる。(瞬間記憶能力を鍛えるための練習法として連想結合法というものがあります。例:橋、米、車、泥という単語を単体で覚えるのは難しい。しかし、「橋の上で米を食べていると、車が後ろを通り、泥が飛んできた。」と物語で覚えることで容易に記憶できる。)

# DEMO映像

![AIgif](https://github.com/user-attachments/assets/e8cd72ec-bf65-4dac-8ada-43267d6c2661)

![AIGif (2)](https://github.com/user-attachments/assets/03806e1f-6f9b-42c0-9841-e3094d6b3d4b)



# Features

## 既存のものとの差別化
Webサイト上でできるため、不要なインストールや登録を行わなくてよい。
画像の生成を一定期間で行えるため、同じ絵柄にならず、毎回新鮮なゲーム体験ができる。
PC画面とスマホ画面に対応している。（PC画面では横長、スマホ画面では、縦長となっている。）

# Requirement

* Python:3.10
* Pytorch:2.0.0-cuda11.7-cudnn8-devel
* WebSocketServer madoi

# Installation

Requirementで列挙したライブラリなどのインストール方法

```bash

pip install diffusers --upgrade transformers accelerate scipy safetensors
pip install invisible_watermark transformers accelerate safetensors ftfy
pip install diffusers[torch]==0.21.0 controlnet_aux==0.0.7
pip install Flask
pip install Redis
pip install mysql-connector-python
pip install flask-socketio

```

# Usage

DEMOの実行方法など、"hoge"の基本的な使い方を説明する

```bash
git clone https://github.com/hoge/~
画像生成を行う場合の指示
cd sdsample
bash createImage.sh
画像を切り替える場合の指示
bash changeImage.sh
```

# Note


画像がない場合、ゲームをすることができない。
画像は例として複数枚入れているが、自身でpythonを動かし、生成してください。

# Documents
Diffusers0.21.0 
https://github.com/huggingface/diffusers/releases/tag/v0.21.0

Flask
https://palletsprojects.com/p/flask/

flask-socketio
https://flask-socketio.readthedocs.io/en/latest/

mysql-connector-python
https://pypi.org/project/mysql-connector-python/



