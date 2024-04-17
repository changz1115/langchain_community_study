// 使用JavaScript画一个房子，兰色的顶，红色的墙，两个窗户 
const canvas = document.getElementById("canvas");
const ctx = canvas.getContext("2d");

// 画房子
ctx.beginPath();
ctx.moveTo(50, 50);
ctx.lineTo(250, 50);
ctx.lineTo(250, 250);
ctx.lineTo(50, 250);
ctx.closePath();
ctx.fillStyle = "#FFD700";
ctx.fill();

// 画墙
ctx.beginPath();
ctx.moveTo(100, 50);
ctx.lineTo(100, 250);
ctx.lineTo(150, 250);
ctx.lineTo(150, 50);
ctx.closePath();
ctx.fillStyle = "#FF0000";
ctx.fill();

// 画窗户
ctx.beginPath();
ctx.moveTo(125, 125);
ctx.lineTo(125, 175);
ctx.lineTo(175, 175);
ctx.lineTo(175, 125);
ctx.closePath();
ctx.fillStyle = "#0000FF";
ctx.fill();

// 画窗户
ctx.beginPath();
ctx.moveTo(175, 125);
ctx.lineTo(175, 175);
ctx.lineTo(225, 175);
ctx.lineTo(225, 125);
ctx.closePath();
ctx.fillStyle = "#0000FF";
ctx.fill();

// 画窗户
ctx.beginPath();
ctx.moveTo(125, 175);
ctx.lineTo(125, 225);
ctx.lineTo(175, 225);
ctx.lineTo(175, 175);
ctx.closePath();
ctx.fillStyle = "#0000FF";
ctx.fill();

// 画窗户
ctx.beginPath();
ctx.moveTo(175, 175);
ctx.lineTo(175, 225);
ctx.lineTo(225, 225);
ctx.lineTo(225, 175);
ctx.closePath();
ctx.fillStyle = "#0000FF";
ctx.fill();





