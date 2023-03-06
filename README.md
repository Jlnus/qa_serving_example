
```
├── README.md
├── requirements.txt
└── app
    ├── __main__.py
    ├── confirm_button_hack.py
    ├── front_streamlit.py : Streamlit으로 작성한 프론트엔드
    ├── main.py : backend.py 라고 생각해도 무방합니다(편의상 main.py라고 명명)
    └── model_inference.py : 딥러닝 모델
```

# FastAPI & Streamlit
FastAPI와 streamlit을 이용한 모델 온라인 서빙

1. 프로젝트의 의존성을 설치
    - Using Poetry
    ```shell
    > poetry install
    ```
    - 나머지
    ```shell
    > pip install -r requirements.txt
    ```

2-1. 애플리케이션 실행

    ```python
    python3 -m app
    ```

2-2. Frontend와 server 동시 실행

    ```python
    make -j 2 run_app
    # or
    python3 -m app
    # in other shell
    python3 -m streamlit run app/frontend.py
    ```

# Reference
https://github.com/zzsza/Boostcamp-AI-Tech-Product-Serving/tree/main/part3/01-fastapi