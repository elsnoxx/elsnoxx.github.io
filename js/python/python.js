function showCodePWreseni(soubor) {
    var password = prompt('Enter the password to download the file: (date)');
    if (password.toLowerCase() == "15012024") {
      window.open(soubor, "novyRam", "width=1200,height=1000")
    } else {
      alert("incorrect password!! please try again");
    }
  }


function showCodePWopakovani(soubor) {
  var password = prompt('Enter the password to download the file:');
  if (password.toLowerCase() == "opakovani") {
    window.open(soubor, "novyRam", "width=1200,height=1000")
  } else {
    alert("incorrect password!! please try again");
  }
}