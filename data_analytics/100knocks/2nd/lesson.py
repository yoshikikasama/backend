# pip install openpyxl
from matplotlib.pyplot import axis
import pandas as pd


def main():
    uriage_data = pd.read_csv('files/uriage.csv')
    kokyaku_data = pd.read_excel('files/kokyaku_daicho.xlsx')
    # print(uriage_data.head())
    # print(kokyaku_data.head())
    # item_nameの重複を除いた値のcount
    # print(len(pd.unique(uriage_data.item_name)))
    # 小文字を大文字に
    uriage_data['item_name'] = uriage_data['item_name'].str.upper()
    uriage_data['item_name'] = uriage_data['item_name'].str.replace(' ','')
    uriage_data['item_name'] = uriage_data['item_name'].str.replace('　','')
    # print(uriage_data.sort_values(by=['item_name'], ascending=True))
    # print(pd.unique(uriage_data.item_name))
    # print(len(pd.unique(uriage_data.item_name)))

    # 金額の欠損値の補完
    # 列ごとにnullがあるか確認
    # print(uriage_data.isnull().any(axis=0))
    flg_is_null = uriage_data['item_price'].isnull()
    # print(flg_is_null)
    # list()変数の値をlist形式に変換
    # loc('条件', '条件に合致したデータの列')
    # unique()重複の削除
    # item_priceがnoneの行のitem_nameをuniqueで取得し、list化
    for trg in list(uriage_data.loc[flg_is_null, 'item_name'].unique()):
        # ~flg_is_nullは「flg_is_nullは「 == Falseと同義
        # 欠損を起こしていないitem_name==trgとなるデータのitem_price最大値を抽出
        price = uriage_data.loc[(~flg_is_null) & (uriage_data['item_name'] == trg), 'item_price'].max()
        uriage_data['item_price'].loc[(flg_is_null) & (uriage_data['item_name'] == trg)] = price
    # print(uriage_data.head())
    # print(uriage_data.isnull().any(axis=0))

    # 顧客名の揺れ
    # print(kokyaku_data['顧客名'].head())
    kokyaku_data['顧客名'] = kokyaku_data['顧客名'].str.replace(' ', '')
    kokyaku_data['顧客名'] = kokyaku_data['顧客名'].str.replace('　', '')
    # print(kokyaku_data['顧客名'].head())
    # 日付の揺れ
    flg_is_serial = kokyaku_data['登録日'].astype('str').str.isdigit()
    print(flg_is_serial.sum())


if __name__ == '__main__':
    main()
