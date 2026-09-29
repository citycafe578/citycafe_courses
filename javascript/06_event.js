// ==========================================
// 1. 取得 DOM 元素
// ==========================================
const myBtn = document.getElementById("btn");
const myInput = document.getElementById("input");
const myForm = document.getElementById("form");

// ------------------------------------------
// 補充：三種常見的 EventListener 寫法
// ------------------------------------------
// 寫法 A：具名函式（適合邏輯較長、需要重複使用的情境）
function handleClick() {
  alert("這是具名函式處理的點擊事件！");
}
myBtn.addEventListener("click", handleClick);

// 寫法 B：匿名函式（寫在裡面，傳統寫法）
// myBtn.addEventListener("click", function () {
//   alert("這是寫在裡面的方式！");
// });

// 寫法 C：箭頭函式（ES6 簡潔寫法，現代最常用）
// myBtn.addEventListener("click", () => {
//   alert("這是箭頭函式！");
// });


// ==========================================
// 2. 滑鼠事件 (Mouse Events)
// ==========================================

// click：點擊一下
myBtn.addEventListener("click", () => {
  console.log("按鈕被點擊了！");
});

// dblclick：快速連點兩下
myBtn.addEventListener("dblclick", () => {
  console.log("按鈕被連點兩下了！");
});

// mouseenter：滑鼠移入元素範圍
myBtn.addEventListener("mouseenter", () => {
  console.log("滑鼠移進按鈕範圍");
});

// mouseleave：滑鼠移出元素範圍
myBtn.addEventListener("mouseleave", () => {
  console.log("滑鼠移出按鈕範圍");
});


// ==========================================
// 3. 鍵盤事件 (Keyboard Events)
// ==========================================

// keydown：按鍵按下（常用於遊戲控制、快捷鍵）
document.addEventListener("keydown", (event) => {
  console.log(`按下了鍵盤按鍵：${event.key}`);
});

// keyup：按鍵放開
document.addEventListener("keyup", (event) => {
  console.log(`放開了鍵盤按鍵：${event.key}`);
});


// ==========================================
// 4. 表單與輸入事件 (Form & Input Events)
// ==========================================

// input：輸入內容即時變更（邊打字邊觸發，適合即時搜尋、字數計算）
myInput.addEventListener("input", (event) => {
  console.log(`即時輸入內容：${event.target.value}`);
});

// change：內容變更且離開輸入框，或下拉選單切換選項時觸發
myInput.addEventListener("change", (event) => {
  console.log(`最終確認內容：${event.target.value}`);
});

// focus：點進輸入框（取得焦點）
myInput.addEventListener("focus", () => {
  console.log("輸入框被點選，準備打字");
});

// blur：點出輸入框（失去焦點，常拿來做欄位驗證）
myInput.addEventListener("blur", () => {
  console.log("點擊到外面，輸入框失去焦點");
});

// submit：表單送出（通常搭配 event.preventDefault() 避免網頁重新整理）
myForm.addEventListener("submit", (event) => {
  event.preventDefault(); // 阻止瀏覽器預設的重整送出行為
  console.log("表單已攔截送出！");
});


// ==========================================
// 5. 視窗與頁面事件 (Window / Document Events)
// ==========================================

// scroll：滾動頁面（適合做返回頂部按鈕、視差滾動）
window.addEventListener("scroll", () => {
  console.log(`目前垂直滾動位置：${window.scrollY}`);
});

// resize：調整視窗大小（適合響應式介面微調）
window.addEventListener("resize", () => {
  console.log(`視窗尺寸變更為：${window.innerWidth} x ${window.innerHeight}`);
});

// DOMContentLoaded：網頁 HTML 結構載入完成（確保抓得到 DOM 元素）
document.addEventListener("DOMContentLoaded", () => {
  console.log("HTML 結構已解析完成，可以開始安全操作 DOM 了！");
});
```[cite: 2]
