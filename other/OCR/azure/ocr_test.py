import os
import time
import requests
from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from msrest.authentication import CognitiveServicesCredentials
from azure.cognitiveservices.vision.computervision.models import ComputerVisionOcrErrorException


key = os.environ["ACCOUNT_KEY"]
endpoint = os.environ["END_POINT"]
image_path = "../img/Screenshot 2023-05-20 at 7.40.54.png"  # ローカルの画像パス


def main(image_path):
    computervision_client = ComputerVisionClient(endpoint, CognitiveServicesCredentials(key))
    with open(image_path, "rb") as file:
        try:
            recognize_handw_results = computervision_client.read_in_stream(file, language="ja", raw=True)
        except ComputerVisionOcrErrorException as e:
            print("errors:", e.response)
            print(vars(e))
            raise e
        time.sleep(5)
        result_url = recognize_handw_results.headers.get("Operation-Location")
        result = requests.get(result_url, headers={"Ocp-Apim-Subscription-Key": key})
        print(result.text)


if __name__ == "__main__":
    main(image_path)
