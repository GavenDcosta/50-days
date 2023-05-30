//Leet Code

//Chunk Array

/**
 * @param {Array} arr
 * @param {number} size
 * @return {Array[]}
 */
var chunk = function(arr, size) {
    var chunkarr = []
    var i = 0
    for(i=0;i<arr.length; i+=size){
        chunkarr.push(arr.slice(i,i+size))
    }
    return chunkarr

};