import random
import streamlit as st


# 1. 카페인 섭취량 계산 및 상태 분석 함수 (조건문 & 반복문 활용)
def analyze_caffeine(drink_type, count):
    # 음료별 1잔당 평균 카페인 함량 (mg)
    caffeine_per_cup = {
        "아메리카노": 150,
        "라떼": 120,
        "에너지드링크": 100,
        "녹차": 30,
    }

    # 반복문을 사용하여 잔 수만큼 총 카페인 함량 누적 계산
    total_caffeine = 0
    for _ in range(count):
        total_caffeine += caffeine_per_cup[drink_type]

    # 조건문을 사용하여 섭취량에 따른 상태 및 조언 분류 (청소년 권장량 125mg 기준 참고)
    if total_caffeine == 0:
        status = "안전"
        advice = "오늘 카페인을 전혀 섭취하지 않으셨네요! 아주 좋습니다."
    elif total_caffeine <= 125:
        status = "적정"
        advice = "적정 수준의 카페인을 섭취했습니다. 남은 하루는 카페인 없는 음료를 마셔보세요."
    elif total_caffeine <= 250:
        status = "주의"
        advice = (
            "권장량을 조금 넘겼습니다. 수면을 방해할 수 있으니 물을 충분히 마셔주세요."
        )
    else:
        status = "위험"
        advice = "카페인 과다 섭취 상태입니다! 심장 두근거림이나 불면증이 올 수 있으니 즉시 카페인을 중단하세요."

    return total_caffeine, status, advice


# 2. 대체 음료 랜덤 추천 함수 (random 라이브러리 활용)
def recommend_alternative():
    alternatives = [
        "시원한 생수 한 잔 💧",
        "갈증 해소에 좋은 이온 음료 ⚡",
        "달콤하고 카페인 없는 보리차 🌾",
        "상큼한 레몬 디톡스 워터 🍋",
        "따뜻한 캐모마일 허브티 🌼",
    ]
    return random.choice(alternatives)


# --- Streamlit 웹 화면 구성 ---
st.set_page_config(page_title="카페인 섭취량 맞춤 가이드", page_icon="☕")

st.title("☕ 카페인 섭취량 맞춤 가이드")
st.write("오늘 마신 음료를 선택하고 나의 카페인 상태를 확인해 보세요!")

st.divider()

# 사용자 입력 영역
drink = st.selectbox(
    "섭취한 음료 종류를 선택하세요:",
    ["아메리카노", "라떼", "에너지드링크", "녹차"],
)

amount = st.slider("섭취량(잔/캔)을 선택하세요:", min_value=1, max_value=5, value=1)

# 버튼 클릭 시 분석 실행
if st.button("카페인 분석하기 🔍", use_container_width=True):
    # 함수 호출
    total_mg, status, message = analyze_caffeine(drink, amount)
    recommended_drink = recommend_alternative()

    st.subheader("📊 분석 결과")
    st.metric(
        label=f"{drink} {amount}잔의 총 카페인 함량", value=f"{total_mg} mg"
    )

    # 상태에 따라 다른 색상 박스로 결과 출력 (조건문)
    if status == "적정":
        st.success(f"**[상태: {status}]** {message}")
    elif status == "주의":
        st.warning(f"**[상태: {status}]** {message}")
    else:
        st.error(f"**[상태: {status}]** {message}")

    # 대체 음료 추천 결과 출력
    st.info(f"💡 **추천 대체 음료:** 오늘은 대신 **{recommended_drink}** 어때요?")
