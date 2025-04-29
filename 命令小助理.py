# 小助理工具 - 終端機版

# 顯示功能選單
def show_menu():
    print("\n========== 小助理選單 ==========")
    print("1. 新增事件")
    print("2. 查詢事件")
    print("3. 問個問題")
    print("4. 離開")
    print("================================")

# 新增事件到事件檔案
def add_event(date, event):
    with open("events.txt", "a", encoding="utf-8") as file:
        file.write(f"{date}: {event}\n")
    print("✅ 事件已新增！")

# 顯示所有事件
def view_events():
    try:
        with open("events.txt", "r", encoding="utf-8") as file:
            content = file.read()
            if content.strip() == "":
                print("📂 沒有任何事件紀錄。")
            else:
                print("\n📅 已記錄事件：")
                print(content)
    except FileNotFoundError:
        print("⚠️ 尚未有事件紀錄喔～")

# 回答使用者問題
def respond_to_question(text):
    if "你是誰" in text:
        return "我是你寫出來的助理呀～"
    elif "天氣" in text:
        return "我雖然不會查天氣，但希望今天是好天氣！"
    elif "你好" in text or "hi" in text.lower():
        return "哈囉你好呀 😊"
    else:
        return "這個我還不會回答呢～"

# 儲存事件的資料結構
events = {}

# 顯示主選單
def show_menu():
    print("\n📋 小助手選單")
    print("1. 新增事件")
    print("2. 查看事件")
    print("3. 問我一個問題")
    print("4. 離開程式")

# 新增事件
def add_event(date, event):
    if date in events:
        events[date].append(event)
    else:
        events[date] = [event]
    print(f"✅ 已新增事件：{date} - {event}")

# 查看事件
def view_events():
    if not events:
        print("📭 目前還沒有事件喔～")
    else:
        print("📅 所有事件：")
        for date, event_list in events.items():
            print(f"{date}:")
            for idx, event in enumerate(event_list, 1):
                print(f"  {idx}. {event}")

# 回答問題
def respond_to_question(question):
    responses = {
        "你好": "哈囉！有什麼我可以幫忙的嗎？",
        "你是誰": "我是你的智慧小助手 🤖",
        "天氣": "我不會看天氣預報，但你可以看看氣象 app～",
        "幾點": "你可以看看右下角的時間或用手機看看喔⏰",
    }
    for key in responses:
        if key in question:
            return responses[key]
    return "這個問題我現在還不會回答，但我會努力學習的！"

# 主程式執行區
def main():
    while True:
        show_menu()
        choice = input("請輸入選項（1-4）：")

        if choice == "1":
            date = input("輸入事件日期（例如 2025-04-22）：")
            event = input("請輸入事件內容：")
            add_event(date, event)

        elif choice == "2":
            view_events()

        elif choice == "3":
            question = input("請問我一個問題：")
            answer = respond_to_question(question)
            print("🤖 助理回答：" + answer)

        elif choice == "4":
            print("👋 掰掰！謝謝使用小助理～")
            break

        else:
            print("⚠️ 請輸入有效的選項（1～4）")

# 啟動程式
main()


