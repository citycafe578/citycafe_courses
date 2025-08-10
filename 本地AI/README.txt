下載 ollama https://ollama.com/
mac : https://ollama.com/download/Ollama-darwin.zip 
win : https://ollama.com/download/OllamaSetup.exe
linux : curl -fsSL https://ollama.com/install.sh | sh
docker : docker run -d -v ollama:/root/.ollama -p 11434:11434 --name ollama ollama/ollama
打開 terminal 輸入 ollama 就可以知道所有指令

ollama pull <模型名稱> --> 下載模型
ollama list --> 查看模型名稱
ollama show --license <模型名稱> --> 查看模型的 license
ollama show --template <模型名稱> --> 查看模型除了 license 以外的所有訊息
ollama run <模型名稱> --> 執行模型
ollama rm <模型名稱> --> 刪除模型
/bye --> 離開 ollama

推薦模型 : 
gemma (中文正常溝通)(8.5B)
codellama (meta 研發拿來寫程式用的)(6.7B)
mistral (非常快，應該不強的電腦也能跑?)(7.2B)
TinyLlama(超級小，i5 3350也能順跑)


避坑模型 : 
llama3 : 正常的話僅限英文溝通
phi3 : 完全不知道在公三小，唬爛產生器