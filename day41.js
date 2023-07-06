//Leet Code

//Counter II

var createCounter = function(init) {
    let i = init

    function increment(){
        return ++i
    }

    function decrement(){
        return --i
    }

    function reset(){
        return i = init
    }

    return {increment, decrement, reset}
};
