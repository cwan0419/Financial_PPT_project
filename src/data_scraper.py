import yfinance as yf
import pandas as pd
import os

def get_financial_data(ticker_data):
    """
    main.py에서 호출되는 함수로, 주식 종목 목록(ticker_data)의 최근 영업일 2일치 데이터를 가져옴
    가져온 데이터를 가공하여 CSV 파일로 저장하고, DataFrame을 반환함
    """

    file_path = "data/stock_data.csv"
    if os.path.exists(file_path):
        os.remove(file_path)
        print("📄 기존 CSV 파일 삭제 완료!")
    
    data = pd.DataFrame()
    for i in ticker_data:
        stock = yf.Ticker(i)
        name = stock.info["longName"]
        hist = stock.history(period="5d")
        if len(hist) >= 2:
            previous_close = hist["Close"].iloc[-2]  # 마지막 거래일 전일 종가
            latest_close = hist["Close"].iloc[-1]    # 가장 최근 거래일 종가
            change = latest_close - previous_close
            change_pct = (change / previous_close) * 100
            data = pd.concat([data, pd.DataFrame({
                "종목명": [name],
                "전일 종가": [previous_close],
                "최근 종가": [latest_close],
                "변동": [change],
                "변동률": [change_pct]
            })], ignore_index=True)
        else:
            print("⚠️ 최근 거래일 데이터가 부족합니다.")
    
    data.to_csv(file_path, index=False, encoding='utf-8-sig')
    print(f"✅ 데이터 저장 완료! ({file_path})")

    return data

if __name__ == "__main__":
    df = get_financial_data(ticker_data[0])
    print(df.head())  # 데이터 미리보기