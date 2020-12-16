import pandas as pd
import datetime
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
        self.item_number = 0
        self.item_order_list=[]
        self.item_master=item_master
    
    def add_item_order(self,item_code):
        self.item_order_list.append(item_code)

    def add_item_number(self,item_number):
        self.item_number = item_number
        
    def view_item_list(self):
        exp_list = []
        for item in self.item_order_list:
            print("商品コード:{}\n個数:{}".format(item,self.item_number))
            #商品名・価格を表示
            for w in self.item_master:
                if w.get_itemcode() == item:
                    name = w.get_itemname()
                    total_order_price = int(w.get_price())*int(self.item_number)
                    print("商品名:{0}\n価格:{1}\n合計金額は{2}円です。".format(w.get_itemname(),w.get_price(),total_order_price))
                    exp_list = [w.get_itemcode(),w.get_itemname(),w.get_price(),self.item_number,total_order_price]
        return exp_list
    
### メイン処理
def main():
    # CSVからマスタ登録
    item_master=[]
    df = pd.read_csv("itemlist.csv", dtype=object,encoding="utf-8_sig")
    #データからクラスを作成
    for i in range(len(df)):
        item_master.append(Item(df["商品コード"][i],df["商品名"][i],df["価格"][i]))
    
    # オーダー登録
    order=Order(item_master)
    iorder_code = input("オーダーする商品のコードを入力してください>>")
    order.add_item_order(iorder_code)
    iorder_number = input("オーダーする商品の個数を入力してください>>")
    order.add_item_number(iorder_number)
    
    # オーダー表示
    result_list = order.view_item_list()
    #お釣りの計算
    cash = input("お支払い金額を入力して下さい>>")
    oturi = int(cash) - result_list[4]
    print("お釣りは{}円です。".format(str(oturi)))

    #テキストで書き出し
    c_time =datetime.date.today()
    current_time = "{0:%Y%m%d-%H%M%S}".format(c_time)
    with open(current_time+".txt",mode="w") as f:
        f.write("商品コード:{}\n商品名:{}\n商品価格:{}円\n商品個数:{}個\n商品合計金額:{}円\nお預かり:{}円\nお釣り:{}円".format(result_list[0],result_list[1],result_list[2],result_list[3],result_list[4],cash,oturi))


    
if __name__ == "__main__":
    main()