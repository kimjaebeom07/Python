import tkinter as tk
from tkinter import messagebox
import time

# ----------------------------
# 스톱워치 변수
# ----------------------------
running = False
start_time = 0
elapsed_time = 0


# ----------------------------
# 스톱워치 함수
# ----------------------------
def update_stopwatch():
    if running:
        current_time = time.perf_counter()
        elapsed = elapsed_time + (current_time - start_time)

        hours = int(elapsed // 3600)
        minutes = int((elapsed % 3600) // 60)
        seconds = int(elapsed % 60)
        centiseconds = int((elapsed * 100) % 100)

        stopwatch_label.config(
            text=f"{hours:02}:{minutes:02}:{seconds:02}.{centiseconds:02}"
        )

        window.after(10, update_stopwatch)


def start_stopwatch():
    global running, start_time

    if not running:
        running = True
        start_time = time.perf_counter()
        update_stopwatch()


def stop_stopwatch():
    global running, elapsed_time

    if running:
        elapsed_time += time.perf_counter() - start_time
        running = False


def reset_stopwatch():
    global running, elapsed_time

    running = False
    elapsed_time = 0

    stopwatch_label.config(text="00:00:00.00")


# ----------------------------
# 타이머 변수
# ----------------------------
timer_running = False
timer_seconds = 0


# ----------------------------
# 타이머 함수
# ----------------------------
def update_timer():
    global timer_seconds, timer_running

    if timer_running:

        if timer_seconds > 0:
            timer_seconds -= 1

            minutes = timer_seconds // 60
            seconds = timer_seconds % 60

            timer_label.config(
                text=f"{minutes:02}:{seconds:02}"
            )

            window.after(1000, update_timer)

        else:
            timer_running = False
            timer_label.config(text="00:00")

            messagebox.showinfo(
                "타이머 종료",
                "설정한 시간이 모두 지났습니다!"
            )


def start_timer():
    global timer_seconds, timer_running

    try:
        minutes = int(timer_entry.get())

        if minutes <= 0:
            timer_label.config(text="1분 이상 입력")
            return

        timer_seconds = minutes * 60
        timer_running = True

        update_timer()

    except ValueError:
        timer_label.config(text="숫자 입력")


def stop_timer():
    global timer_running
    timer_running = False


def reset_timer():
    global timer_running, timer_seconds

    timer_running = False
    timer_seconds = 0

    timer_label.config(text="00:00")
    timer_entry.delete(0, tk.END)


# ----------------------------
# GUI 생성
# ----------------------------
window = tk.Tk()
window.title("타이머 & 스톱워치")
window.geometry("450x500")
window.resizable(False, False)

# ----------------------------
# 스톱워치 영역
# ----------------------------
title1 = tk.Label(
    window,
    text="스톱워치",
    font=("맑은 고딕", 18, "bold")
)
title1.pack(pady=10)

stopwatch_label = tk.Label(
    window,
    text="00:00:00.00",
    font=("Consolas", 30)
)
stopwatch_label.pack(pady=10)

start_btn = tk.Button(
    window,
    text="시작",
    width=15,
    command=start_stopwatch
)
start_btn.pack(pady=3)

stop_btn = tk.Button(
    window,
    text="정지",
    width=15,
    command=stop_stopwatch
)
stop_btn.pack(pady=3)

reset_btn = tk.Button(
    window,
    text="초기화",
    width=15,
    command=reset_stopwatch
)
reset_btn.pack(pady=3)

# ----------------------------
# 구분선
# ----------------------------
divider = tk.Label(
    window,
    text="──────────────────",
    font=("맑은 고딕", 12)
)
divider.pack(pady=15)

# ----------------------------
# 타이머 영역
# ----------------------------
title2 = tk.Label(
    window,
    text="타이머",
    font=("맑은 고딕", 18, "bold")
)
title2.pack()

info_label = tk.Label(
    window,
    text="시간(분)을 입력하세요"
)
info_label.pack(pady=5)

timer_entry = tk.Entry(
    window,
    justify="center",
    width=15
)
timer_entry.pack()

timer_label = tk.Label(
    window,
    text="00:00",
    font=("Consolas", 30)
)
timer_label.pack(pady=10)

timer_start_btn = tk.Button(
    window,
    text="타이머 시작",
    width=15,
    command=start_timer
)
timer_start_btn.pack(pady=3)

timer_stop_btn = tk.Button(
    window,
    text="타이머 정지",
    width=15,
    command=stop_timer
)
timer_stop_btn.pack(pady=3)

timer_reset_btn = tk.Button(
    window,
    text="타이머 초기화",
    width=15,
    command=reset_timer
)
timer_reset_btn.pack(pady=3)

# ----------------------------
# 실행
# ----------------------------
window.mainloop()