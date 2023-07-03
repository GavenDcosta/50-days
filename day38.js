//Leet Code

//Array Prototype Last

Array.prototype.last = function() {
    if(this.length == 0){
        return -1
    }
    else{
        return this[this.length - 1]
    }
};


//Filter Elements from Array

var filter = function(arr, fn) {
    var ans = [];
  for (var i = 0; i < arr.length; i++) {
    if (fn(arr[i], i)) {
      ans.push(arr[i]);
    }
  }
  return ans;
};