# OCR

## Azure OCR

RES_GROUP=<resourcegroup-name>
ACCT_NAME=<computervision-account-name>

export ACCOUNT_REGION=$(az cognitiveservices account show \
 --resource-group $RES_GROUP \
 --name $ACCT_NAME \
 --query location \
 --output tsv)

export ACCOUNT_KEY=$(az cognitiveservices account keys list \
 --resource-group $RES_GROUP \
 --name $ACCT_NAME \
 --query key1 \
 --output tsv)

export ACCOUNT_REGION=japaneast
export ACCOUNT_KEY=${ACCOUNT_KEY}
export END_POINT=${END_POINT}

https://learn.microsoft.com/en-us/python/api/azure-cognitiveservices-vision-computervision/azure.cognitiveservices.vision.computervision.operations.computervisionclientoperationsmixin?view=azure-python

## Tesseract OCR

- そのまま実行
  image_path = "../img/PXL_20230521_022935737.MP.jpg" # ローカルの画像パス
