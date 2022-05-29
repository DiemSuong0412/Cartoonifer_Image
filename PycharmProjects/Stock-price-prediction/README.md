Trong dự án máy học này, chúng ta sẽ nói về việc dự đoán lợi nhuận từ cổ phiếu. Chúng tôi sẽ phát triển dự án này thành hai phần:
1. Đầu tiên, chúng ta sẽ dự đoán giá cổ phiếu bằng mạng nơ ron LSTM.
2. Sau đó, xây dựng một bảng điều khiển bằng cách sử dụng Plotly dash để phân tích chứng khoán.

## Bộ dữ liệu
1. Để xây dựng mô hình dự đoán giá cổ phiếu, chúng tôi sử dụng bộ dữ liệu NSE TATA GLOBAL. Đây là tập dữ liệu về Đồ uống Tata từ Công ty TNHH Đồ uống toàn cầu Tata, Sở giao dịch chứng khoán quốc gia Ấn Độ: [Tập dữ liệu toàn cầu của Tata](https://github.com/DiemSuong0412/machine_learning_project/blob/main/PycharmProjects/Stock-price-prediction/NSE-TATA.csv)

2. Để phát triển bảng điều khiển cho phân tích cổ phiếu, chúng tôi sẽ sử dụng một tập dữ liệu cổ phiếu khác với nhiều cổ phiếu như Apple, Microsoft, Facebook: [Stocks Dataset](https://github.com/DiemSuong0412/machine_learning_project/blob/main/PycharmProjects/Stock-price-prediction/stock_data.csv)

## Dashboard
![](https://github.com/DiemSuong0412/machine_learning_project/blob/main/PycharmProjects/Stock-price-prediction/stock-price-analysis-dashboard-apple.png)
![](https://github.com/DiemSuong0412/machine_learning_project/blob/main/PycharmProjects/Stock-price-prediction/stock-market-volume-apple.png)
