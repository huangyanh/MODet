import warnings
warnings.filterwarnings('ignore')
from ultralytics import YOLO


if __name__ == '__main__':
    model = YOLO('ultralytics/cfg/models/MODet.yaml')
    model.train(data='/home/hjj/Desktop/dataset/dataset_visdrone/data.yaml',
                cache=False,
                imgsz=640,
                epochs=100,
                batch=8,
                close_mosaic=0,
                workers=4,
                # device='0',
                optimizer='AdamW', # using SGD
                # patience=0, # close earlystop
                # resume=True, # 断点续训
                # amp=False, # close amp
                # fraction=0.2,
                project='runs/train',
                name='exp',
                )