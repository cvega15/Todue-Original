export default function turn_to_12(time){
    
    var amorpm;
    var hour = ((time).substr(0, (time).indexOf(':')))
    if(hour > 12){
        amorpm = " pm"
    }else{
        amorpm = " am"
    }
    var first_part = (hour%12) || 12
    var second_part = (time).substr(((time).indexOf(':')) + 1)

    return first_part + ':' + second_part + amorpm
};