function SayHello(food) {
  console.log("Hello");
  console.log(`我想要吃${food}`); // 在輸出中塞變數
  // console.log("我想要吃" + food); 這樣也可以
}

let food = "蛋餅";
SayHello(food); // 輸出：我想要吃蛋餅

food = "薯條";
SayHello(food); // 輸出：我想要吃薯條