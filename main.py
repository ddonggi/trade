import pyupbit

#exchange API
#Access Key와 Sercret Key를 사용해서 Upbit 객체를 생성합니다. 이는 웹페이지에서 로그인하는 것과 같습니다.

access = "ispYBg7aHn906gd1XXWlclMzVCoO0IIreDXr2oCZ"          # 본인 값으로 변경
secret = "uPzw9HonEVdWpjhlx5dFMxZ23q7v7Biwx5uSn9hq"          # 본인 값으로 변경
upbit = pyupbit.Upbit(access, secret)

#잔고 조회
#get_balance 메서드는 입력받은 티커의 보유 수량 정보를 조회합니다.

print('XRP : ', upbit.get_balance("KRW-XRP"))     # KRW-XRP 조회
print('BTC : ', upbit.get_balance("KRW-BTC"))     # KRW-XRP 조회
print('My WON : ', upbit.get_balance("KRW"))         # 보유 현금 조회