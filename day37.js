//Leet Code

//Apply Transform Over Each Element in Array

var map = function(arr, fn) {
    for(let i=0;i<arr.length;i++){
        arr[i] = fn(arr[i],i)
    } 
    return arr
};


//Sleep

async function sleep(millis) {
    await new Promise(resolve => setTimeout(resolve,millis))
}
