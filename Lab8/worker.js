
var i = 0;
var j = 1;
var FibNumber = 0;

//obliczanie kolejnych liczb ciagu fibonaciego
function timedCountFibNumber() {
  FibNumber = i + j;
  i=j;
  j=FibNumber;
  postMessage(FibNumber);
  setTimeout("timedCount()",1000);
}

timedCountFibNumber();
