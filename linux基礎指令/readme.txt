sudo apt update 取得升級
sudo apt upgrade 安裝升級
whoami 看使用者名稱

cd 地點   前往某資料夾
cd ..    返回上一個資料夾
pwd   取得當前路徑

ls 查看檔案
ls -a 查看所有檔案
   -S 按照檔案大小排序
   -t 按照時間排序
ls -l 查看詳細資料
內容會有十個英文代號
第一個是文件型態
後面三個三個一組分別代表擁有者 組用戶 其他用戶
資料內容 https://github.com/samonxian/common-usage/issues/14

mkdir 創建資料夾
touch 創造檔案
nano 編輯檔案
ctr + O 儲存
ctr + X 離開

rm 刪除檔案
cp 檔案名稱 目標地點   複製檔案
mv 檔案名稱 目標地點   移動檔案

下載檔案: 
curl 選項 檔案網址
curl -fsSL https://ollama.com/install.sh | sh

wget 檔案網址
wget http://ftp.gnu.org/gnu/wget/wget-1.19.tar.gz

curl不只是下載工具還是一個檔案的收發器，curl還可以傳送JSON API資料傳輸 送出POST請求
wget是下載工具，可以用來寫簡易腳本讓系統自動下載資料(因為簡單好用)，網路不好的時候如果下載東西下載到一半，網路恢復後不用全部重新下載，接回上次的斷點就好