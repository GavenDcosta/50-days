setInterval(() => {
    var time = new Date()
    var h = time.getHours()
    var m = time.getMinutes()
    var s = time.getSeconds()
    var intr = document.getElementById('intr')

    document.getElementById('hrs').innerHTML= h
    document.getElementById('mins').innerHTML= m
    document.getElementById('secs').innerHTML= s

    if(hrs>12){
        intr.innerHTML = 'PM'
    }
    else{
        intr.innerHTML = 'AM'
    }
}, 10);