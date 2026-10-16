# OpenAI Streamlit 챗봇

`gpt-4o-mini`를 사용하는 간단한 스트리밍 챗봇입니다.

## Streamlit Community Cloud 배포

1. 이 폴더를 GitHub 저장소에 올립니다.
2. Streamlit Community Cloud에서 저장소를 선택하고 `app.py`를 메인 파일로 지정합니다.
3. 앱의 **Settings → Secrets**에 아래 내용을 등록합니다.

```toml
OPENAI_API_KEY = "sk-여기에-OpenAI-API-키"
```

4. `requirements.txt`가 자동으로 설치되면 앱을 실행합니다.

API 키는 소스 코드나 GitHub 저장소에 직접 입력하지 마세요.

## 로컬 실행

```powershell
python -m pip install -r requirements.txt
streamlit run app.py
```

로컬에서는 `.streamlit/secrets.toml` 파일에 같은 `OPENAI_API_KEY`를 넣어 사용할 수 있습니다. 이 파일은 Git에 커밋하지 마세요.
