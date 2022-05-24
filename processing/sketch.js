let img;
function preload() {
 img = loadImage("./signature.png");
}

function setup() {
  let canvas = createCanvas(500, 500, "webgl");
}

function draw() {
  background("gray");
  
  fill("yellow");
  rotateY(millis()/1000);
  rect(-0, -100, 50, 50);
  rect(-0, 100, 50, 50);


  rotateX(millis()/1000);
  for (let i = 0; i < 1000; i++) {
    let r = random(-50, 50);
    line(50, i, 50 + r, i);
  }
  
  fill("blue");
  rect(-100,-10, 50, 50);
  rect(100, -10, 50, 50);
  
  fill("orange")
  
  rect(0, -10, 50, 50);
  tint(85, 150, 86, 150);
  image(img, 10,10, img.width/10, img.height/10);s
}

//Usar con cuidado sino se guardan en automatico y empieza un loop
function Guardar_Captura() {
saveCanvas(canvas, 'png');
}

