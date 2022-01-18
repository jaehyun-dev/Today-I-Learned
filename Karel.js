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
