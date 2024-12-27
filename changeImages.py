import torch
from diffusers import DiffusionPipeline, DPMSolverMultistepScheduler
import mysql.connector
import os
from PIL import Image

base = DiffusionPipeline.from_pretrained(
    "stabilityai/stable-diffusion-xl-base-1.0", torch_dtype=torch.float16, variant="fp16", use_safetensors=True
)
base.to("cuda")
refiner = DiffusionPipeline.from_pretrained(
    "stabilityai/stable-diffusion-xl-refiner-1.0",
    text_encoder_2=base.text_encoder_2,
    vae=base.vae,
    torch_dtype=torch.float16,
    use_safetensors=True,
    variant="fp16",
)
refiner.to("cuda")


n_steps = 40
high_noise_frac = 0.8


card =   ["queen", "rabbit", "sun", "tree",
    "umbrella", "violin", "watermelon", "xylophone", "yacht",
    "zebra", "computer", "keyboard", "television", "book",
    "lamp", "shoes", "socks", "chair", "table",
    "window", "clock", "mirror", "painting", "umbrella",
    "hat", "shirt", "pants", "shovel", "ball",
    "doll", "bicycle", "bus", "train", "carriage", "Desk",
    "Chair", "Computer", "Lamp", "Book", "Phone",
    "Table", "Window", "Door", "Keyboard", "Mouse",
    "Monitor", "Clock", "Notebook", "Pen", "Pencil",
    "Eraser", "Globe", "Globe", "Backpack", "Headphones",
    "Microphone", "Sunglasses", "Wallet", "Mirror",
    "Calendar", "Chair", "Plant", "Refrigerator", "Oven",
    "Microwave", "Coffee maker", "Blender", "Plate",
    "Fork", "Spoon", "Knife", "Cup", "Television", "Sofa",
    "Carpet", "Curtains", "Painting", "Easel", "Sculpture",
    "Globe", "Refrigerator", "Heater", "Air conditioner",
    "Trash can", "Recycling bin", "Soap", "Towel", "Toothbrush",
    "Toothpaste", "Shampoo", "Conditioner", "Hairdryer", "Razor",
    "Scale", "Gym bag", "Dumbbell", "Yoga mat", "Running shoes",
    "Bicycle", "Helmet", "Backpack", "Tent", "Sleeping bag",
    "Campfire", "Telescope", "Microscope", "Laboratory",
    "Petri dish", "Bunsen burner", "Test tube", "Flask",
    "Graduated cylinder", "Pipette", "Erlenmeyer flask", "Centrifuge",
    "Laboratory coat", "Goggles", "Safety gloves", "Fire extinguisher",
    "Emergency exit", "Exit sign", "Fire alarm", "Fire escape", "Fire hydrant",
    "Fire truck", "Police car", "Ambulance", "Stop sign", "Traffic light",
    "Crosswalk", "Speed bump","Parking meter", "Streetlamp"
]

#NSFWを無視する
def null_safety(images, **kwargs):
    return images, False
# pipeline.safety_checker = null_safety

def conn_db():
      conn = mysql.connector.connect(
              host = 'mysql_host',      #localhostでもOK
              port='3306',
              user = 'root',
              passwd = 'root',
              db = 'ai_trump'
      )
      return conn

dir_path = "./static/images/"

file_list = os.listdir(dir_path)
id_last = int(len(file_list) / 2)


for i in range(len(card)): 
    for alpha in ('s','d'):
        prompt = card[i]
        negative_prompt ="black and white, worst quality, low quality, normal quality, ugly, bad anatomy, jpeg artifacts, lowres, error" 
        # image = pipe(prompt).images[0]
        image = base(
            prompt=prompt,
            negative_prompt=negative_prompt,
            num_inference_steps=n_steps,
            denoising_end=high_noise_frac,
            output_type="latent",
        ).images
        image = refiner(
            prompt=prompt,
            negative_prompt=negative_prompt,
            num_inference_steps=n_steps,
            denoising_start=high_noise_frac,
            image=image,
        ).images[0]
        
        if(alpha == 's'):
            #画像ファイル名指定
            path1 = str(dir_path) + str(alpha) + str(id_last + i + 1) + '.png'
            image.save(path1)   
        else:
            path2 = str(dir_path) + str(alpha) + str (id_last + i + 1) + '.png'
            image.save(path2)   
    try:
        conn = conn_db()              #ここでDBに接続
        cursor = conn.cursor()       #カーソルを取得
        sql = ('''INSERT INTO CARD (path1,path2,theme_name) VALUES('{}','{}','{}');'''.format(path1,path2,card[i]))
        cursor.execute(sql)
        conn.commit()
        # rows = cursor.fetchall()      #selectの結果を全件タプルに格納
    except(mysql.connector.errors.ProgrammingError) as e:
        print('エラーだぜ')
        print(e)
