import pyupbit
import numpy as np

# OHLCV (open, high, low, close, volume) 당일 시가,고가,저가,종가,거래량
df = pyupbit.get_ohlcv("KRW-BTC", count=7) #count : 일 수


#변동성 돌파 전략
# 변동폭 * k 계산, (고가 - 저가) * k값
df['range'] = (df['high'] - df['low']) * 0.5
# target(매수가), range 컬럼을 한칸씩 밑으로 내림(.shift(1))
df['target'] = df['open'] + df['range'].shift(1)
print(df)
# fee = 0.0032
# ror(수익율), np.where(조건문, 참일때 값, 거짓일때 값)
df['ror'] = np.where(df['high'] > df['target'],
                     df['close'] / df['target'], #- fee,
                     1)
# 누적 수익률 : 누적 곱 계산(cumprod)
df['hpr'] = df['ror'].cumprod()

# Draw Down 계산 ( 누적 최대 값과 현재 hpr 차이 / 누적최대값 * 100 )
df['dd'] = (df['hpr'].cummax() - df['hpr']) / df['hpr'].cummax() * 100
# MDD ( 하락폭 )
print("MDD(%): ", df['dd'].max())

#엑셀로 출력
df.to_excel("dd.xlsx")