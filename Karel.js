//2022.01.23

//Unit 8 Lesson 5

//Make Karel fill the world
//with beepers
function main() {
   //your code here
   while(leftIsClear()){
      putBeeperLine();
      moveToAnotherLine();
   }
   putBeeperLine();
}

function putBeeperLine(){
   putBeeper();
   while(frontIsClear()) {
      move();
      putBeeper();
   }
}

function moveToAnotherLine(){
   turnAround();
   while(frontIsClear()){
      move();
   }
   turnRight();
   move();
   turnRight();
}

//Unit 9 Lesson 2

//Karel must help rebuild 
//broken columns. Make a 
//column of beepers above
//each beeper you find on
//the first row
function main() {
   while(frontIsClear()){
      move();
      if(beepersPresent()){
         putBeeperColumn();
      }
   }
}

function putBeeperColumn() {
   turnLeft();
   putBeeperLine();
   turnAround();
   moveToWall();
   turnLeft();
}

function putBeeperLine() {
   while(frontIsClear()){
      move();
      putBeeper();
   }
}

function moveToWall() {
   while(frontIsClear()) {
      move();
   }
}



//2022.01.18

//Unit 12 Lesson 1

//Your final task is to teach
//Karel to find the midpoint
//of any world. You can assume
//that all worlds are square.
function main(){
   repeat(2){
      while(frontIsClear()){
         move();
      }
      putBeeper();
      turnAround();
   }
   repeat(4){
      if(frontIsClear()){
         move();
         while(noBeepersPresent()){
            move();
         }
         turnAround();
         move();
         putBeeper();
      }
   }
      


   turnAround();
   while(frontIsClear()){
      move();
   }
   turnAround();
   invertBeepers();

}

function invertBeepers(){
   while(frontIsClear()){
      if(beepersPresent()){
         pickBeeper();
      } else{
         putBeeper();
      }
      move();
   }
   if(beepersPresent()){
         pickBeeper();
      } else{
         putBeeper();
      }
}
