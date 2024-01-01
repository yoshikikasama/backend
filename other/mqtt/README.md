# mqtt with mac

## mosquitto install

```
brew install mosquitto
brew services start mosquitto
echo 'export PATH="/usr/local/sbin:$PATH"' >> ~/.zshrc
source ~/.zshrc
brew services list
brew services stop mosquitto
pyenv versions
poetry env list
poetry shell
```

```
poetry add paho-mqtt
poetry add pytest
poetry add pytest-mock
poetry add coverage
coverage run -m pytest
coverage report
coverage html
index.htmlを開く
```

```
pytest -s
mosquitto_pub -h localhost -t "drone/001" -m '{"status": "running"}'
```

## 参考

https://qiita.com/hsgucci/items/6461d8555ea1245ef6c2
https://marketplace.visualstudio.com/items?itemName=LittleFoxTeam.vscode-python-test-adapter
https://marketplace.visualstudio.com/items?itemName=LittleFoxTeam.vscode-python-test-adapter
https://github.com/eclipse/paho.mqtt.python/tree/master
https://github.com/audreyfeldroy/cookiecutter-pypackage

1. mid (Message ID)
   用途: mid（Message ID）は、特定の MQTT メッセージに対して一意に割り当てられる識別子です。on_publish コールバック関数では、送信されたメッセージの mid が渡されます。これにより、どのメッセージが送信されたかを追跡することができます。
   使用例: メッセージが正常にブローカーに送信されたことを確認するために使用されます。ログ出力やデバッグに有用です。
2. flag
   用途: flag は、on_connect コールバック関数において、接続応答フラグを表します。これには、セッションが持続しているかどうかを示す情報が含まれます（セッションプレゼントフラグ）。
   使用例: クライアントが新しいセッションを開始したのか、既存のセッションを再開したのかを識別するために使用されます。通常、このフラグはクライアントのセッション管理に関連しています。

3. rc (Return Code)
   用途: rc（Return Code）は、on_connect および on_disconnect コールバック関数で使用され、接続や切断の結果を示すステータスコードです。on_connect では、接続の成否を示し、on_disconnect では切断の原因を示します。
   使用例: rc が 0 の場合は接続や切断が成功したことを意味します。非ゼロの場合は、何らかのエラーが発生したことを示し、エラーの種類を識別するために使用されます。
   これらのパラメータは、MQTT プロトコルにおける重要な情報を提供し、MQTT クライアントの動作を正確に制御および監視するために使用されます。
