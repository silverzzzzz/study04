import pprint
## 商品クラス
class Item:
    def __init__(self,item_code,item_name,price):
        self.item_code=item_code
        self.item_name=item_name
        self.price=price
    
    def get_itemcode(self):
        return self.item_code

    def get_price(self):
        return self.price

    def get_itemname(self):
        return self.item_name

### オーダークラス
class Order:
    def __init__(self,item_master):
        self.item_order_list=[]
        self.item_master=item_master
    
    def add_item_order(self,item_code):
        self.item_order_list.append(item_code)
        
    def view_item_list(self):
        for item in self.item_order_list:
            print("商品コード:{}".format(item))
            #商品名・価格を表示
            for w in self.item_master:
                if w.get_itemcode() == item:
                    name = w.get_itemname() 
                    print("商品名:{0}\n価格:{1}".format(w.get_itemname(),w.get_price()))
    
### メイン処理
def main():
    # マスタ登録
    item_master=[]
    item_master.append(Item("001","りんご",100))
    item_master.append(Item("002","なし",120))
    item_master.append(Item("003","みかん",150))
    
    # オーダー登録
    order=Order(item_master)
    iorder = input("オーダーする商品のコードを入力してください>>")
    order.add_item_order(iorder)
    
    # オーダー表示
    order.view_item_list()

    
if __name__ == "__main__":
    main()