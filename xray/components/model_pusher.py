import sys
from xray.cloud_storage.s3_ops import S3Operation

from xray.entity.config_entity import ModelPusherConfig
from xray.exception import XRayException
from xray.logger import logging


class ModelPusher:
    def __init__(self,model_pusher_config: ModelPusherConfig):

        self.model_pusher_config = model_pusher_config
        self.s3 = S3Operation() ## 新增


    
    def initiate_model_pusher(self):

        """
        Method Name :   initiate_model_pusher

        Description :   This method initiates model pusher. 
        
        Output      :    Model pusher artifact 
        """
        logging.info("Entered initiate_model_pusher method of Modelpusher class")
        try:
            # Uploading the best model to s3 bucket
            self.s3.upload_file(
                "model/model.pt", # 來源地檔案
                "model.pt",       # 目的地檔案
                "lungxray24",     # bucket 名稱
                remove=False,     # boolean 
            ) ## 新增
            logging.info("Uploaded best model to s3 bucket")
            logging.info("Exited initiate_model_pusher method of ModelTrainer class")


        except Exception as e:
            raise e
