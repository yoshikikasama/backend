import os
import time
from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from msrest.authentication import CognitiveServicesCredentials
from azure.cognitiveservices.vision.computervision.models import (
    OperationStatusCodes,
)
from azure.cognitiveservices.vision.computervision.models import (
    ComputerVisionOcrErrorException,
)


key = os.environ["ACCOUNT_KEY"]
endpoint = os.environ["END_POINT"]
image_dir = "img/"  # 画像が格納されているディレクトリパス


def main(image_dir):
    computervision_client = ComputerVisionClient(
        endpoint, CognitiveServicesCredentials(key)
    )
    image_files = os.listdir(image_dir)
    txt_files = [
        f for f in os.listdir() if os.path.isfile(f) and f.endswith(".txt")
    ]
    print(txt_files)
    for txt_file in txt_files:
        os.remove(txt_file)
    for i, image_file in enumerate(image_files):
        image_path = os.path.join(image_dir, image_file)
        local_image = open(image_path, "rb")
        try:
            recognize_results = computervision_client.read_in_stream(
                local_image, language="ja", raw=True
            )
        except ComputerVisionOcrErrorException as e:
            print("errors:", e.response)
            raise e
        # 結果を取得するための操作IDを取得
        operation_location_remote = recognize_results.headers[
            "Operation-Location"
        ]
        operation_id = operation_location_remote.split("/")[-1]

        # 結果が利用可能になるまで待つ
        while True:
            get_text_results = computervision_client.get_read_result(
                operation_id
            )
            if get_text_results.status not in ["notStarted", "running"]:
                break
            time.sleep(1)

        # テキストの出力
        if get_text_results.status == OperationStatusCodes.succeeded:
            output_file = f"output_{i + 1}.txt"
            with open(output_file, "w", encoding="utf-8") as f:
                for (
                    text_result
                ) in get_text_results.analyze_result.read_results:
                    for line in text_result.lines:
                        f.write(line.text + "\n")
            print(f"Texts are written to {output_file}")


if __name__ == "__main__":
    main(image_dir)
