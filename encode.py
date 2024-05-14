import chardet
import pandas as pd

# CSV 파일 경로
input_file = 'apartment_2024_01.csv'
output_file = 'output.csv'

# 파일의 인코딩을 감지하는 함수
def detect_encoding(file_path):
    with open(file_path, 'rb') as file:
        raw_data = file.read(10000)  # 파일의 앞부분만 읽어서 인코딩 감지
        result = chardet.detect(raw_data)
        return result['encoding']

# 입력 파일의 인코딩 감지
encoding = detect_encoding(input_file)
print(f"Detected encoding: {encoding}")

# CSV 파일을 읽고 상단 15줄을 제거한 후 다시 저장
with open(input_file, 'r', encoding=encoding) as file:
    # 모든 줄을 읽음
    lines = file.readlines()

# 15줄을 제거하고 나머지를 다시 저장
with open('temp.csv', 'w', encoding=encoding) as temp_file:
    temp_file.writelines(lines[15:])

# pandas를 사용하여 CSV 파일 읽기
df = pd.read_csv('temp.csv', encoding=encoding)

# "transaction_amount" 컬럼을 수정하는 부분
# 여기에서 'transaction_amount' 컬럼을 수정하세요.
# 예: df['transaction_amount'] = df['transaction_amount'] * 2
# 사용자가 원하는 대로 수정하면 됩니다.
df['거래금액(만원)'] = df['거래금액(만원)'].str.replace(',', '').astype(int)
# 사용자 지정 수정 코드 삽입

# 새로운 CSV 파일로 저장
df.to_csv(output_file, index=False, encoding='utf-8')

print(f"Processed CSV file saved as {output_file}")
