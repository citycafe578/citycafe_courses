const myBtn = document.getElementById("btn");

function handleClick() {
  alert("這是具名函式處理的點擊事件！");
}
myBtn.addEventListener("click", handleClick);

// myBtn.addEventListener("click", function(){
//     alert("這是寫在裡面的方式！");
// });

// myBtn.addEventListener("click", () => {
//   alert("這事箭頭函式！");
// });
