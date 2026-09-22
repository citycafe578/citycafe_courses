// 隨機產生 1 ~ 100 的整數
const targetNumber = Math.floor(Math.random() * 100) + 1;
let isGuessed = false;

while(!isGuessed){
    const input = prompt("請猜一個 1 到 100 之間的數字：");

  // 使用者點選取消時中斷遊戲
    if(input === null){
        alert("遊戲結束！");
        break;
    }

    const guess = Number(input);

  // 檢查是否為有效數字
    if(isNaN(guess) || input.trim() === ""){
        alert("請輸入有效的數字！");
        continue;
    }

  // 判斷邏輯
    if(guess < targetNumber){
        alert("猜小了喔！！");
    }else if(guess > targetNumber){
        alert("太大了！");
    }else{
        alert("答對了！");
        isGuessed = true;
    }
}