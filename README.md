# Mini NPU Simulator

MAC(Multiply-Accumulate) 연산을 직접 구현하여 입력 패턴과 필터의 유사도를 판별하는 Python 콘솔 애플리케이션입니다.

## 개발 환경

- Python 3.8 이상
- 외부 라이브러리 사용 없음
- Python 표준 라이브러리 사용

## 실행 방법

```bash
python3 main.py
```

## 주요 기능

- 3×3 필터 및 패턴 사용자 입력
- MAC 연산을 통한 패턴 판별
- epsilon 기반 동점 처리
- `data.json` 기반 패턴 일괄 분석
- Cross / X 라벨 정규화
- 크기별 MAC 연산 성능 측정
- 테스트 결과 PASS / FAIL 및 결과 요약

## 프로젝트 구조

```text
mini-npu-simulator/
├── main.py
├── data.json
├── README.md
└── .gitignore
```

## 결과 리포트

구현 및 테스트 완료 후 작성 예정입니다.