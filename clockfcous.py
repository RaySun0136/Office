# 导入time模块
import time

# 定义专注时钟函数
def focus_timer(minutes):
    # 将分钟转换为秒
    seconds = minutes * 60
    # 循环直到秒数为零
    while seconds > 0:
        # 打印倒计时信息
        print(f"倒计时: {seconds // 60} 分钟 {seconds % 60} 秒")
        # 等待一秒
        time.sleep(1)
        # 减少一秒
        seconds -= 1
    # 打印结束信息
    print("时间到！专注结束。")

# 设置专注时长为25分钟
focus_time = 25
# 调用专注时钟函数
focus_timer(focus_time)
