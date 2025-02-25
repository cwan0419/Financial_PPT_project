

from data_scraper import get_financial_data
from report_generator import create_ppt_report

def main():
    print("📊 금융 보고서 생성 시작...")

    # 1. 금융 데이터 수집
    ticker_data = ["^GSPC", "^IXIC", "^DJI", "^TNX", "USDKRW=X", "^KS11"]
    # ^GSPC: S&P500, ^IXIC: 나스닥, ^DJI: 다우존스, ^TNX: 10년 국채, USDKRW=X: 환율, ^KS11: 코스피
    data = get_financial_data(ticker_data)

    # 2. PPT 보고서 생성
    create_ppt_report(data)

    print("✅ 보고서 생성 완료! output/financial_report.pptx")

if __name__ == "__main__":
    main()
