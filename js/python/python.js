function showCodePW(soubor) {
    var password = prompt('Enter the password to download the file:');
    if (password.toLowerCase() == "teacher") {
      window.open(soubor, "novyRam", "width=1200,height=1000")
    } else {
      alert("incorrect password!! please try again");
    }
  }