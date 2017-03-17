function canIWatch(age) {

  var newAge = parseInt(age);

  if(isNaN(newAge) || newAge <= 0){
    return "Invalid age.";
  } else{
    if(newAge < 6) {
      return "You are not allowed to watch Deadpool after 6.00pm.";
    }else if(newAge >= 6 && newAge < 17){
      return "You must be accompanied by a guardian who is 21 or older.";
    }else if(newAge >=17 && newAge < 25){
      return "You are allowed to watch Deadpool, right after you show some ID.";
    }else{
      return "Yay! You can watch Deadpool with no strings attached!";
    }
  }
}
