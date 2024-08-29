import streamlit as st
from joblib import load
import pandas as pd
import os

# 모델 파일 경로를 상대 경로로 지정
model_path = os.path.join('Seoul_house_project', 'seoul_satisfaction_model.joblib')
model = load(model_path)

# 스트림릿 애플리케이션 타이틀
st.title('서울특별시 주민 만족도 예측 서비스')

st.markdown("""
본 서비스는 **서울특별시 주민들의 만족도를 예측**하는 인터랙티브한 플랫폼입니다.
사용자는 만족도 예측을 위해 원하는 값을 입력하면, 해당 데이터에 기반한 만족도 예측 결과를 실시간으로 확인할 수 있습니다.
본 서비스를 통해 주택 공급 결정 시 시뮬레이션 자료로 활용할 수 있습니다.
            
주요 기능은 다음과 같습니다:
- 여러분의 입력에 따른 **실시간 만족도 예측**
- 간편한 사용자 인터페이스를 통한 **빠른 접근성**
- **데이터 기반**의 정확한 예측 제공
""")

# 사용자 입력 받는 부분들
# 시군구 선택 설명
sigungu_description = """
시군구 선택:
1. 강남구, 2. 강동구, 3. 강북구, 4. 강서구, 5. 관악구, 
6. 광진구, 7. 구로구, 8. 금천구, 9. 노원구, 10. 도봉구, 
11. 동대문구, 12. 동작구, 13. 마포구, 14. 서대문구, 15. 서초구, 
16. 성동구, 17. 성북구, 18. 송파구, 19. 양천구, 20. 영등포구, 
21. 용산구, 22. 은평구, 23. 종로구, 24. 중구, 25. 중랑구
"""
st.markdown(sigungu_description)

# 시군구 목록
sigungu_options = [
    "강남구", "강동구", "강북구", "강서구", "관악구", 
    "광진구", "구로구", "금천구", "노원구", "도봉구", 
    "동대문구", "동작구", "마포구", "서대문구", "서초구", 
    "성동구", "성북구", "송파구", "양천구", "영등포구", 
    "용산구", "은평구", "종로구", "중구", "중랑구"
]

# 사용자에게 시군구 선택 제공, 번호 반환
selected_sigungu_index = st.selectbox('시군구 선택', range(1, 26), format_func=lambda x: f"{x}. {sigungu_options[x-1]}")

# 주거 형태 선택 설명
housing_description = """
주거 형태 선택:
1. 일반단독주택, 2. 다가구단독주택, 3. 영업겸용단독주택, 
4. 아파트, 5. 연립주택, 6. 다세대주택,
7. 비거주용건물(상가ㆍ공장ㆍ여관 등)내 주택, 8. 오피스텔, 
9. 고시원, 10. 판잣집ㆍ비닐하우스ㆍ컨테이너ㆍ움막, 11. 기타
"""
st.markdown(housing_description)

# 주거 형태 목록
housing_options = [
    "일반단독주택", "다가구단독주택", "영업겸용단독주택", 
    "아파트", "연립주택", "다세대주택",
    "비거주용건물(상가ㆍ공장ㆍ여관 등)내 주택", "오피스텔", 
    "고시원", "판잣집ㆍ비닐하우스ㆍ컨테이너ㆍ움막", "기타"
]

# 사용자에게 주거 형태 선택 제공, 번호 반환
selected_housing_index = st.selectbox('주거 형태 선택', range(1, 12), format_func=lambda x: f"{x}. {housing_options[x-1]}")

# 성별 선택 설명
gender_description = """
성별 선택:
1. 남성, 2. 여성, 3. 그외
"""
st.markdown(gender_description)

# 성별 선택을 위한 라디오 버튼, 숫자 반환
gender_options = ["남성", "여성", "그외"]
selected_gender_index = st.radio('성별 입력', range(1, 4), format_func=lambda x: f"{x}. {gender_options[x-1]}")

# 주택 보유 여부 선택 설명
owning_description = """
주택 보유 여부 선택:
0. 미보유, 1. 보유
"""
st.markdown(owning_description)

# 주택 보유 여부 선택을 위한 라디오 버튼, 숫자 반환
owning_options = ["미보유", "보유"]
selected_owning_index = st.radio('주택 보유 여부 선택', range(2), format_func=lambda x: f"{x}. {owning_options[x]}")

# 클러스터 선택을 위한 설명과 라디오 버튼
cluster_description = """
#### 클러스터 설명
: 본 클러스터는 클러스터링 모델을 통해 도출된 클러스터입니다. 
주택 공급 시 원하는 조건의 거주자들을 해당 클러스터를 참고하여 선택할 수 있습니다.

**Cluster 0 - 청년층 1, 2인 가구:**
- **연령대:** 18세~55세, 평균 36세
- **총자산:** 0~15억, 평균 1.7억, 중간값 1억
- **가구원수:** 1~3명, 평균 1.3명

**Cluster 1 - 기혼가구로 사회활동 중인 중장년 가구주를 보유한 중자산층:**
- **연령대:** 26~98세, 평균 60세
- **총자산:** 6.8억~26억, 평균 15억, 중간값 14억
- **가구원수:** 1~7명, 평균 2.9명

**Cluster 2 - 노인가구:**
- **연령대:** 51~101세, 평균 71세
- **총자산:** 0~17억, 평균 3억, 중간값 3억
- **가구원수:** 1~4명, 평균 1.7명, 중간값 2

**Cluster 3 - 저자산층 버전 cluster1:**
- **연령대:** 23~90세, 평균 51세
- **총자산:** 0~20억, 평균 4억, 중간값 3억
- **가구원수:** 3~9명, 평균 3.6명

**Cluster 4 - 고소득층:**
- **연령대:** 33~94세, 평균 64세
- **총자산:** 24억~200억, 평균 36억, 중간값 31억
- **가구원수:** 1~7명, 평균 2.8명
"""

# 클러스터 선택을 위한 라디오 버튼, 숫자 반환
cluster_options = [
    "청년층 1, 2인 가구",
    "기혼가구로 사회활동 중인 중장년 가구주를 보유한 중자산층",
    "노인가구",
    "저자산층 버전 cluster1",
    "고소득층"
]
selected_cluster_index = st.radio("거주자들의 예상 군집을 선택해주세요:", range(1, 6), format_func=lambda x: f"Cluster {x-1}: {cluster_options[x-1]}")

# 점유 형태 선택 설명
occupy_description = """
점유 형태 선택:
1. 자가, 2. 전세, 3. 보증금 있는 월세, 
4. 보증금 없는 월세, 5. 사글세 또는 연세, 6. 일세, 7. 무상
"""
st.markdown(occupy_description)

# 점유 형태 선택을 위한 라디오 버튼, 숫자 반환
occupy_options = [
    "자가", "전세", "보증금 있는 월세", 
    "보증금 없는 월세", "사글세 또는 연세", "일세", "무상"
]
selected_occupy_index = st.radio('점유 형태 선택', range(1, 8), format_func=lambda x: f"{x}. {occupy_options[x-1]}")

num_of_room = st.slider('방 수 입력', 0.0, 10.0, 5.0)

num_of_livingroom = st.slider('거실 수 입력', 0.0, 10.0, 5.0)

num_of_kitchen = st.slider('부엌 수 입력', 0.0, 10.0, 5.0)

area = st.number_input('평수 입력', min_value=0.0, max_value=9999999.0, value=50.0)

income = st.number_input('월 평균 근로/사업 소득', min_value=0, max_value=9999999, value=5000)

# 예측 버튼
if st.button('예측 결과 확인'):
    new_data = pd.DataFrame({
        'SIGUNGU' : [selected_sigungu_index],
        'housing_cat': [selected_housing_index],
        'sex': [selected_gender_index],
        'owning': [selected_owning_index],
        'cluster': [selected_cluster_index],
        'occupy': [selected_occupy_index],
        'num_of_room': [num_of_room],
        'num_of_livingroom': [num_of_livingroom],
        'num_of_kitchen': [num_of_kitchen],
        'area': [area],
        'income': [income]
    })

    # 예측 수행
    prediction = model.predict(new_data)

    # 예측 결과에 대응하는 레이블 매핑
    satisfaction_levels = {
        0: '매우불만족',
        1: '조금불만족',
        2: '만족',
        3: '매우만족'
    }
    predicted_satisfaction = satisfaction_levels[prediction[0]]

# 사용자 입력 요약과 결과 출력
st.write(f"""
선택하신 자치구: {selected_sigungu_index}, 주거 형태: {selected_housing_index}, 성별: {selected_gender_index}, 주택보유 여부: {selected_owning_index}, 
군집: {selected_cluster_index}, 점유 형태: {selected_occupy_index}, 방 수: {num_of_room}, 
거실 수: {num_of_livingroom}, 부엌 수: {num_of_kitchen}, 평수: {area}, 
월 평균 근로/사업 소득: {income}의 만족도 예측 결과입니다.
""")

# 만족도 예측 결과를 굵고 크게 표시
st.markdown(f"**만족도 예측: {predicted_satisfaction}**")