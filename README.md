# 국내 주식 10종 Streamlit 대시보드

## 실행 방법

```powershell
python -m pip install -r requirements.txt
streamlit run app.py
```

기본 종목은 삼성전자, SK하이닉스, LG에너지솔루션, 현대차, 삼성바이오로직스, 기아, 셀트리온, POSCO홀딩스, NAVER, 카카오입니다.

데이터는 `yfinance`를 통해 Yahoo Finance에서 가져오며, 앱 내부에서 15분간 캐시됩니다.

사이드바에 OpenAI API 키를 입력하면 현재 조회된 주식 데이터를 바탕으로 질문에 답하는 `gpt-4.1-mini` 챗봇을 사용할 수 있습니다. API 키는 앱 세션에서만 사용되며 파일에 저장하지 않습니다.

사이드바의 PDF 업로더로 분석할 PDF를 올리면 PDF에서 추출한 텍스트도 챗봇 답변의 근거로 함께 사용됩니다. 스캔 이미지 PDF는 OCR 처리가 필요합니다.

사이드바에 OpenDART API 키를 입력하면 선택한 기업의 최근 90일 공시를 확인할 수 있습니다. 공시 원문 링크와 함께 공시 정보가 챗봇 문맥에도 포함됩니다.
