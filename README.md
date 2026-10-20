# citycafe_courses 課程總整理

這個 repo 是我過去教過的所有課程的整理合集。

這些課程原本分散在不同的社群與活動中,現在把 **ZLCSC21、ZLCSC23、Study For Hour、GDGoC NTNU、GDGoC NCUE** 的所有課程教材、範例程式與筆記,全部集中放在這裡,方便學員回頭複習,也方便之後自己查找。

## 課程列表


| 資料夾                             | 主題               | 內容簡介                                                                                                                |
| ---------------------------------- | ------------------ | ----------------------------------------------------------------------------------------------------------------------- |
| [`linux基礎指令`](./linux基礎指令) | Linux 基礎指令     | `cd`、`ls`、`mkdir`、`cp`、`mv`、`rm`、`nano`、`curl` / `wget` 下載、檔案權限等常用指令筆記                             |
| [`爬蟲`](./爬蟲)                   | Python 爬蟲        | 基礎 Python、`requests` 爬蟲初體驗、下載圖片與 PDF、HTML 介紹、BeautifulSoup 解析、用 Python 操作 Excel、爬蟲結合 Excel |
| [`javascript`](./javascript)       | JavaScript 基礎    | 3 小時入門工作坊:輸出、變數與型別、使用者輸入、運算、迴圈、小遊戲、函式、事件監聽;附課堂簡報與課程規劃                  |
| [`NodeJS`](./NodeJS)               | Node.js 入門       | Hello JS、Buffer、`fs` 檔案系統(讀寫、複製、重新命名、刪除、資料夾操作)、`path`、HTTP 服務、模組化、Express             |
| [`flask`](./flask)                 | Flask 網頁開發     | 共 7 天:基本路由、模板(Jinja2 / base template)、表單、Session、登入登出、Flash 訊息、SQLite 使用者資料                  |
| [`WebSocket`](./WebSocket)         | WebSocket 即時通訊 | 使用 Flask-SocketIO 做出即時多人互動的範例                                                                              |
| [`本地AI`](./本地AI)               | 本地 AI(Ollama)    | 安裝 Ollama、模型下載與管理指令、推薦模型與避坑模型,以及貪吃蛇與 AI 的小範例                                            |
| [`本地AI實作`](./本地AI實作)       | 本地 AI 實作       | 用 Ollama 串接 Python 程式,比較一般版與 AI 版的應用實作                                                                 |
| [`單目測距`](./單目測距)           | 電腦視覺:單目測距  | 使用 OpenCV 搭配 YOLOv8,以單一鏡頭估算物體距離                                                                          |

## 課程來源

這個 repo 整合了我在以下社群 / 活動 / 社團的課程:

- **ZLCSC21**
- **ZLCSC23**
- **Study For Hour**
- **GDGoC NTNU**
- **GDGoC NCUE**

## 如何使用

1. 把整個 repo 下載下來:

   ```bash
   git clone https://github.com/citycafe578/citycafe_courses.git
   ```

   或是直接在 GitHub 頁面點選 **Code → Download ZIP**。
2. 進入想複習的課程資料夾,依檔名編號順序(例如 `01_`、`02_`、`day_01`、`day_02`)由前往後閱讀與執行。
3. 各課程需要的環境:


   | 課程                            | 建議環境                                                                                        |
   | ------------------------------- | ----------------------------------------------------------------------------------------------- |
   | JavaScript                      | VS Code + Live Server 擴充套件 + Chrome                                                         |
   | Node.js                         | [Node.js](https://nodejs.org/);Express 範例需先執行 `npm install`                               |
   | Python 爬蟲 / Flask / WebSocket | Python 3,並安裝所需套件(`requests`、`beautifulsoup4`、`openpyxl`、`flask`、`flask-socketio` 等) |
   | 本地 AI                         | [Ollama](https://ollama.com/)、`ollama` Python 套件                                             |
   | 單目測距                        | `opencv-python`、`ultralytics`,以及一支網路攝影機                                               |

## 備註

- 部分資料夾內有各自的筆記或說明檔(如 `readme.txt`、`javascript.md`),建議先閱讀。
- 程式碼為教學用途,以簡單易懂為主,歡迎自由參考與修改。
- 如果發現錯誤或有建議,歡迎開 Issue 或 Pull Request。
