function plzwork() {
  var word = document.getElementById("input1").value;
  word = word.toLowerCase();
  var firstletter = word.charAt(0);
  var restof = word.slice(1)
  let capitalize = restof.charAt(0).toUpperCase() + restof.slice(1)
  var finalword = capitalize +  firstletter + "ay"
  document.getElementById("para").innerHTML = finalword;
}
