import streamlit as st
import random


st.title("🎯 猜数字游戏")

# 保存答案
if "secret" not in st.session_state:
    st.session_state.secret = random.randint(1,100)
    st.session_state.count = 0


guess = st.number_input(
    "请输入1~100之间的数字",
    min_value=1,
    max_value=100,
    step=1
)


if st.button("提交猜测"):

    st.session_state.count += 1

    if guess > st.session_state.secret:
        st.warning("大了！")

    elif guess < st.session_state.secret:
        st.warning("小了！")

    else:
        st.success(
            f"恭喜你猜对了！答案是{st.session_state.secret}"
        )

        st.info(
            f"你一共猜了{st.session_state.count}次"
        )