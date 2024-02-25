# try exceptを短く定義する記載方法

def purchase_from_view(request):
    # POSTパラメーター処理
    try:
        product_id = request.POST['product_id']
        purchase_count = request.POST['purchase_count']
    except KeyError as e:
        # 必要なデータがPOSTされていない
        return render(request, 'purchase/purchase.html', {'error': f'{e.args[0]}は必須です。'})
    try:
        purchase_count = int(purchase_count)
        if purchase_count <= 0:
            raise ValueError
    except ValueError:
        # POSTされたデータが不正
        return render(request, 'purchase/purchase.html', {'error': 'purchase_countは不正な値です'})
    try:
        # 在庫確認
        product = get_product_by_id(product_id)
    except DoesNotExist:
        return render(request, 'purchase/purchase.html', {'error': '指定された商品が見つかりません'})
    if purchase_count > product.stock.count:
        # 商品の在庫が不足
        return render(request, 'purchase/purchase.html', {'error': '商品の在庫が不足しています'})

    product.stock.count -= purchase_count
    product.stock.save()
    purchase = create_purchase(
        product=product,
        count=purchase_count,
        amount_price=purchase_count*product.price
    )
    return render(request, 'purchase/result.html', {'purchase': purchase})