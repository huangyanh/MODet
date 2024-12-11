from ultralytics import YOLO


if __name__ == '__main__':
    model = YOLO('ultralytics/cfg/models/MODet.yaml')
    model.train(**{'cfg': 'ultralytics/cfg/default.yaml', 'data': 'G:\zuomian\MODet\dataset\seagull.yaml'})  #data/SeaDronesSee.yaml

